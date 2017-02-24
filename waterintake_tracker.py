import sys
import os
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QIcon, QDialog
from PySide.QtCore import QThread, SIGNAL, Qt, QTime
import settings
import datetime
import sqlite3
from time import sleep
from ui_water_intake import Ui_WaterIntakeWindow
from ui_water_intake_settings import Ui_Dialog


__version__ = '0.3'


class Sqlite:
    def __init__(self):
        self.connect_to_db()

    def connect_to_db(self):
        dbname = os.path.join(settings.homedir, 'waterintake.db')
        self.conn = sqlite3.connect(dbname, check_same_thread=False)
        self.schemacheck()

    def db_select(self, sql_query):
        if not self.conn:
            self.connect_to_db()
        curr = self.conn.cursor()
        curr.execute(sql_query)
        header = list(map(lambda x: x[0], curr.description))
        data = curr.fetchall()
        return header, data

    def db_insert(self, sql_query):
        if not self.conn:
            self.connect_to_db()
        curr = self.conn.cursor()
        curr.execute(sql_query)
        self.conn.commit()

    def schemacheck(self):
        with open(os.path.join(settings.appdir, 'sql.schema'), 'rt') as f:
            schema = f.read()
        self.conn.executescript(schema)

    def get_curr_day_glass_count(self):
        sql_query = "SELECT count(*) FROM waterlist where date(updatetime) = date('now');"
        _, d = self.db_select(sql_query)
        return d[0][0]

    def glass_consumed(self):
        sql_query = "INSERT into waterlist (event_type, updatetime) values ('water_drunk', datetime('now'));"
        self.db_insert(sql_query)


class WaterMeterThread(QThread):
    def __init__(self, parent=None):
        super(WaterMeterThread, self).__init__(parent)
        self.sql = Sqlite()
        self.must_run = True
        self.popup_active = False

    def get_bucket_times(self, start, end, number):
        try:
            delta = (end - start) / number
        except:
            return []
        else:
            return [i * delta + start for i in range(number)]

    def calculate_drink_times(self):
        remaining_buckets = int(settings.WATER_GOAL) - int(self.sql.get_curr_day_glass_count())
        if remaining_buckets != 0:
            self.popup_active = False
        now = datetime.datetime.now()
        start_time = datetime.datetime.strptime(settings.START_TIME, '%H:%M:%S').replace(year=now.year, month=now.month, day=now.day)
        if start_time < now:
            start_time = now
        end_time = datetime.datetime.strptime(settings.END_TIME, '%H:%M:%S').replace(year=now.year, month=now.month, day=now.day)
        self.drink_buckets = self.get_bucket_times(start_time, end_time, remaining_buckets)
        self.update_drink_time()
        self.reload_form()

    def ask_again_in_5(self):
        self.drink_buckets[0] = self.drink_buckets[0] + datetime.timedelta(minutes=5)
        self.update_drink_time()
        self.popup_active = False

    def update_drink_time(self):
        try:
            next_drink_time = self.drink_buckets[0].strftime('%H:%M:%S')
        except:
            self.emit(SIGNAL("DrinkTimeUpdate(QString)"), "Tomorrow")
        else:
            self.emit(SIGNAL("DrinkTimeUpdate(QString)"), next_drink_time)

    def reload_form(self):
        self.emit(SIGNAL("ReloadForm()"))

    def glass_consumed(self):
        self.drink_buckets.pop(0)
        self.sql.glass_consumed()
        self.reload_form()
        self.update_drink_time()
        self.popup_active = False

    def run(self):
        sleep(15)
        self.calculate_drink_times()
        while self.must_run:
            now = datetime.datetime.now()
            if len(self.drink_buckets) > 0:
                if now > self.drink_buckets[0]:
                    if not self.popup_active:
                        self.emit(SIGNAL("TimeToDrink()"))
                        self.popup_active = True
            if now > datetime.datetime.strptime(settings.START_TIME, '%H:%M:%S').replace(year=now.year,
                                                                                         month=now.month,
                                                                                         day=now.day) and len(self.drink_buckets) == 0:
                self.calculate_drink_times()
            self.emit(SIGNAL("CheckAchieved()"))
            sleep(5)


class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.setupUi(self)
        self.finished.connect(self._do_accepted)
        self.setup_form()

    def setup_form(self):
        self.sbGlassCount.setValue(int(settings.WATER_GOAL))
        self.teStartTime.setTime(QTime.fromString(settings.START_TIME))
        self.teEndTime.setTime(QTime.fromString(settings.END_TIME))

    def _do_accepted(self, button):
        if self.accept:
            settings.update_settings(self.sbGlassCount.text(), self.teStartTime.text(), self.teEndTime.text())
            self.emit(SIGNAL("settingsUpdated()"))


class MainWindow(QMainWindow, Ui_WaterIntakeWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.actionSettings.triggered.connect(self.open_settings_dialog)
        self.settings_frame = SettingsDialog(self)
        self.connect(self.settings_frame, SIGNAL("settingsUpdated()"), self.load_settings, Qt.QueuedConnection)
        self.w = WaterMeterThread(self)
        self.connect(self.w, SIGNAL("ReloadForm()"), self.load_form, Qt.QueuedConnection)
        self.connect(self.w, SIGNAL("TimeToDrink()"), self.drink_dialog, Qt.QueuedConnection)
        self.connect(self.w, SIGNAL("CheckAchieved()"), self.check_achieved, Qt.QueuedConnection)
        self.connect(self.w, SIGNAL("DrinkTimeUpdate(QString)"), self.set_drink_time, Qt.QueuedConnection)
        self.sql = Sqlite()
        self.load_settings()

        self.btnConsumedGlass.clicked.connect(self.force_drink)

    def load_form(self):
        self.lblGoalVal.setText(str(settings.WATER_GOAL))
        self.lblAcheivedVal.setText(str(self.sql.get_curr_day_glass_count()))

    def load_settings(self):
        reload(settings)
        if not settings.WATER_GOAL or not settings.START_TIME or not settings.END_TIME:
            self.statusbar.showMessage('Please check settings')
        else:
            self.statusbar.showMessage('Settings Successfully Loaded', 5000)
            self.w.calculate_drink_times()
            self.w.start()
        self.load_form()

    def open_settings_dialog(self):
        self.settings_frame.show()

    def set_drink_time(self, drink_time):
        self.lblNextVal.setText(drink_time)

    def check_achieved(self):
        if int(self.sql.get_curr_day_glass_count()) == int(settings.WATER_GOAL):
            if not self.w.popup_active:
                self.w.popup_active = True
                QMessageBox.information(self,
                                        "Legend",
                                        """You dominated today, well done on drinking so much water.""",
                                        QMessageBox.Ok,
                                        WindowModility=True)

    def drink_dialog(self):
        res = QMessageBox.warning(self,
                                  "Drink Now",
                                  """You must drink now.\nCan I record this task as completed?""",
                                  QMessageBox.Yes | QMessageBox.No,
                                  WindowModility=True)
        if res == QMessageBox.StandardButton.Yes:
            self.w.glass_consumed()
            self.check_achieved()
        else:
            self.w.ask_again_in_5()

    def force_drink(self):
        res = QMessageBox.warning(self,
                                  "Are you sure",
                                  """Can I record this task as completed?""",
                                  QMessageBox.Yes | QMessageBox.No,
                                  WindowModility=True)
        if res == QMessageBox.StandardButton.Yes:
            self.w.glass_consumed()
            self.check_achieved()


def main():
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    if getattr(sys, 'frozen', False):
        # frozen
        appdir = os.path.dirname(sys.executable)
    else:
        # unfrozen
        appdir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QIcon(os.path.join(appdir, 'watericon.ico')))
    app.exec_()

if __name__ == '__main__':
    main()
