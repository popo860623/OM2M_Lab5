# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 429)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 291, 120))
        self.groupBox.setObjectName("groupBox")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 20, 261, 71))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 150, 291, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.fan_minus = QtWidgets.QPushButton(self.groupBox_2)
        self.fan_minus.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.fan_minus.setObjectName("fan_minus")
        self.fan_plus = QtWidgets.QPushButton(self.groupBox_2)
        self.fan_plus.setGeometry(QtCore.QRect(140, 140, 75, 23))
        self.fan_plus.setObjectName("fan_plus")
        self.movie_screen = QtWidgets.QLabel(self.groupBox_2)
        self.movie_screen.setGeometry(QtCore.QRect(60, 20, 151, 111))
        self.movie_screen.setFrameShape(QtWidgets.QFrame.Box)
        self.movie_screen.setObjectName("movie_screen")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 330, 291, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tmp_minus = QtWidgets.QPushButton(self.groupBox_3)
        self.tmp_minus.setGeometry(QtCore.QRect(60, 30, 75, 23))
        self.tmp_minus.setObjectName("tmp_minus")
        self.tmp_plus = QtWidgets.QPushButton(self.groupBox_3)
        self.tmp_plus.setGeometry(QtCore.QRect(140, 30, 75, 23))
        self.tmp_plus.setObjectName("tmp_plus")
        self.get_status = QtWidgets.QPushButton(self.groupBox)
        self.get_status.setGeometry(QtCore.QRect(120, 95, 75, 23))
        self.get_status.setObjectName("get_status")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "1. 溫度"))
        self.groupBox_2.setTitle(_translate("Dialog", "2. 風量"))
        self.fan_minus.setText(_translate("Dialog", "◄"))
        self.fan_plus.setText(_translate("Dialog", "►"))
        self.movie_screen.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_3.setTitle(_translate("Dialog", "3. 溫度控制"))
        self.tmp_minus.setText(_translate("Dialog", "◄"))
        self.tmp_plus.setText(_translate("Dialog", "►"))
        self.get_status.setText(_translate("Dialog","Get_Status"))
