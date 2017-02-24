# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\h2ointake_settings.ui'
#
# Created: Wed Feb 22 12:42:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(345, 95)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 102))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblTargetDesc = QtGui.QLabel(self.layoutWidget)
        self.lblTargetDesc.setObjectName("lblTargetDesc")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblTargetDesc)
        self.sbGlassCount = QtGui.QSpinBox(self.layoutWidget)
        self.sbGlassCount.setObjectName("sbGlassCount")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.sbGlassCount)
        self.lblWorkDayStartDesc = QtGui.QLabel(self.layoutWidget)
        self.lblWorkDayStartDesc.setObjectName("lblWorkDayStartDesc")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblWorkDayStartDesc)
        self.teStartTime = QtGui.QTimeEdit(self.layoutWidget)
        self.teStartTime.setTime(QtCore.QTime(7, 0, 0))
        self.teStartTime.setObjectName("teStartTime")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.teStartTime)
        self.lblWorkDayEndDesc = QtGui.QLabel(self.layoutWidget)
        self.lblWorkDayEndDesc.setObjectName("lblWorkDayEndDesc")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblWorkDayEndDesc)
        self.teEndTime = QtGui.QTimeEdit(self.layoutWidget)
        self.teEndTime.setTime(QtCore.QTime(18, 0, 0))
        self.teEndTime.setObjectName("teEndTime")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.teEndTime)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.LabelRole, self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTargetDesc.setText(QtGui.QApplication.translate("Dialog", "Water Intake Target (glasses)", None, QtGui.QApplication.UnicodeUTF8))
        self.lblWorkDayStartDesc.setText(QtGui.QApplication.translate("Dialog", "Workday Start Time", None, QtGui.QApplication.UnicodeUTF8))
        self.lblWorkDayEndDesc.setText(QtGui.QApplication.translate("Dialog", "Workday End Time", None, QtGui.QApplication.UnicodeUTF8))

