# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/control.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ControlWidget(object):
    def setupUi(self, ControlWidget):
        ControlWidget.setObjectName("ControlWidget")
        ControlWidget.setEnabled(True)
        ControlWidget.resize(921, 526)
        ControlWidget.setMaximumSize(QtCore.QSize(1400, 1050))
        self.centralwidget = QtWidgets.QWidget(ControlWidget)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 101, 143))
        self.centralwidget.setObjectName("centralwidget")
        self.labe_time = QtWidgets.QLabel(self.centralwidget)
        self.labe_time.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labe_time.setFont(font)
        self.labe_time.setAlignment(QtCore.Qt.AlignCenter)
        self.labe_time.setObjectName("labe_time")
        self.button_time_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_time_start.setGeometry(QtCore.QRect(10, 50, 81, 23))
        self.button_time_start.setObjectName("button_time_start")
        self.button_time_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_time_pause.setGeometry(QtCore.QRect(10, 80, 81, 23))
        self.button_time_pause.setObjectName("button_time_pause")
        self.button_time_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_time_reset.setGeometry(QtCore.QRect(10, 110, 81, 23))
        self.button_time_reset.setObjectName("button_time_reset")

        self.retranslateUi(ControlWidget)
        QtCore.QMetaObject.connectSlotsByName(ControlWidget)

    def retranslateUi(self, ControlWidget):
        _translate = QtCore.QCoreApplication.translate
        ControlWidget.setWindowTitle(_translate("ControlWidget", "SCK Anzeigetafel"))
        self.labe_time.setText(_translate("ControlWidget", "Zeit"))
        self.button_time_start.setText(_translate("ControlWidget", "Start"))
        self.button_time_pause.setText(_translate("ControlWidget", "Pause"))
        self.button_time_reset.setText(_translate("ControlWidget", "Reset"))
