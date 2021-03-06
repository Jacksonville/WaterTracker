# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\h2ointake.ui'
#
# Created: Fri Feb 24 07:39:40 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_WaterIntakeWindow(object):
    def setupUi(self, WaterIntakeWindow):
        WaterIntakeWindow.setObjectName("WaterIntakeWindow")
        WaterIntakeWindow.resize(364, 182)
        self.centralwidget = QtGui.QWidget(WaterIntakeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblGoalDesc = QtGui.QLabel(self.layoutWidget)
        self.lblGoalDesc.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblGoalDesc.setFont(font)
        self.lblGoalDesc.setObjectName("lblGoalDesc")
        self.horizontalLayout.addWidget(self.lblGoalDesc)
        self.lblGoalVal = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lblGoalVal.setFont(font)
        self.lblGoalVal.setText("")
        self.lblGoalVal.setObjectName("lblGoalVal")
        self.horizontalLayout.addWidget(self.lblGoalVal)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblAcheivedDesc = QtGui.QLabel(self.layoutWidget1)
        self.lblAcheivedDesc.setMaximumSize(QtCore.QSize(140, 16777215))
        self.lblAcheivedDesc.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblAcheivedDesc.setFont(font)
        self.lblAcheivedDesc.setObjectName("lblAcheivedDesc")
        self.horizontalLayout_2.addWidget(self.lblAcheivedDesc)
        self.lblAcheivedVal = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lblAcheivedVal.setFont(font)
        self.lblAcheivedVal.setText("")
        self.lblAcheivedVal.setObjectName("lblAcheivedVal")
        self.horizontalLayout_2.addWidget(self.lblAcheivedVal)
        self.btnConsumedGlass = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConsumedGlass.sizePolicy().hasHeightForWidth())
        self.btnConsumedGlass.setSizePolicy(sizePolicy)
        self.btnConsumedGlass.setMinimumSize(QtCore.QSize(50, 50))
        self.btnConsumedGlass.setMaximumSize(QtCore.QSize(50, 50))
        self.btnConsumedGlass.setSizeIncrement(QtCore.QSize(50, 50))
        self.btnConsumedGlass.setBaseSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setBold(True)
        self.btnConsumedGlass.setFont(font)
        self.btnConsumedGlass.setObjectName("btnConsumedGlass")
        self.horizontalLayout_2.addWidget(self.btnConsumedGlass)
        self.layoutWidget2 = QtGui.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblNextDesc = QtGui.QLabel(self.layoutWidget2)
        self.lblNextDesc.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblNextDesc.setFont(font)
        self.lblNextDesc.setObjectName("lblNextDesc")
        self.horizontalLayout_3.addWidget(self.lblNextDesc)
        self.lblNextVal = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lblNextVal.setFont(font)
        self.lblNextVal.setText("")
        self.lblNextVal.setObjectName("lblNextVal")
        self.horizontalLayout_3.addWidget(self.lblNextVal)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        WaterIntakeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(WaterIntakeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        WaterIntakeWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(WaterIntakeWindow)
        self.statusbar.setObjectName("statusbar")
        WaterIntakeWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(WaterIntakeWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtGui.QAction(WaterIntakeWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(WaterIntakeWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), WaterIntakeWindow.close)
        QtCore.QMetaObject.connectSlotsByName(WaterIntakeWindow)

    def retranslateUi(self, WaterIntakeWindow):
        WaterIntakeWindow.setWindowTitle(QtGui.QApplication.translate("WaterIntakeWindow", "WaterIntake", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGoalDesc.setText(QtGui.QApplication.translate("WaterIntakeWindow", "Goal", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAcheivedDesc.setText(QtGui.QApplication.translate("WaterIntakeWindow", "Total Today", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConsumedGlass.setText(QtGui.QApplication.translate("WaterIntakeWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNextDesc.setText(QtGui.QApplication.translate("WaterIntakeWindow", "Next Glass at", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("WaterIntakeWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("WaterIntakeWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("WaterIntakeWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

