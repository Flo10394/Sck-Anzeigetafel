# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/control.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ControlWindow(object):
    def setupUi(self, ControlWindow):
        ControlWindow.setObjectName("ControlWindow")
        ControlWindow.setEnabled(True)
        ControlWindow.resize(739, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(ControlWindow.sizePolicy().hasHeightForWidth())
        ControlWindow.setSizePolicy(sizePolicy)
        ControlWindow.setMaximumSize(QtCore.QSize(1400, 1050))
        self.centralwidget = QtWidgets.QWidget(ControlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_edit_time_manual_seconds = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_time_manual_seconds.setGeometry(QtCore.QRect(270, 430, 31, 20))
        self.line_edit_time_manual_seconds.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_time_manual_seconds.setObjectName("line_edit_time_manual_seconds")
        self.label_time_manual_double_point = QtWidgets.QLabel(self.centralwidget)
        self.label_time_manual_double_point.setGeometry(QtCore.QRect(240, 430, 31, 21))
        self.label_time_manual_double_point.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_manual_double_point.setObjectName("label_time_manual_double_point")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(190, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.button_time_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_time_start.setGeometry(QtCore.QRect(210, 290, 91, 23))
        self.button_time_start.setObjectName("button_time_start")
        self.line_edit_time_manual_minutes = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_time_manual_minutes.setGeometry(QtCore.QRect(210, 430, 31, 20))
        self.line_edit_time_manual_minutes.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_time_manual_minutes.setObjectName("line_edit_time_manual_minutes")
        self.button_time_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_time_reset.setGeometry(QtCore.QRect(210, 350, 91, 23))
        self.button_time_reset.setObjectName("button_time_reset")
        self.button_time_manual = QtWidgets.QPushButton(self.centralwidget)
        self.button_time_manual.setGeometry(QtCore.QRect(210, 400, 91, 23))
        self.button_time_manual.setObjectName("button_time_manual")
        self.button_time_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_time_pause.setGeometry(QtCore.QRect(210, 320, 91, 23))
        self.button_time_pause.setObjectName("button_time_pause")
        self.label_score_double_point = QtWidgets.QLabel(self.centralwidget)
        self.label_score_double_point.setGeometry(QtCore.QRect(60, 320, 31, 21))
        self.label_score_double_point.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score_double_point.setObjectName("label_score_double_point")
        self.button_score_home_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_score_home_minus.setGeometry(QtCore.QRect(20, 350, 41, 23))
        self.button_score_home_minus.setObjectName("button_score_home_minus")
        self.label_spielstand = QtWidgets.QLabel(self.centralwidget)
        self.label_spielstand.setEnabled(True)
        self.label_spielstand.setGeometry(QtCore.QRect(10, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_spielstand.setFont(font)
        self.label_spielstand.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spielstand.setObjectName("label_spielstand")
        self.line_edit_score_guest = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_score_guest.setGeometry(QtCore.QRect(90, 320, 41, 20))
        self.line_edit_score_guest.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_score_guest.setObjectName("line_edit_score_guest")
        self.button_score_guest_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_score_guest_minus.setGeometry(QtCore.QRect(90, 350, 41, 23))
        self.button_score_guest_minus.setObjectName("button_score_guest_minus")
        self.button_score_home_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_score_home_plus.setGeometry(QtCore.QRect(20, 290, 41, 23))
        self.button_score_home_plus.setObjectName("button_score_home_plus")
        self.line_edit_score_home = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_score_home.setGeometry(QtCore.QRect(20, 320, 41, 20))
        self.line_edit_score_home.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_score_home.setObjectName("line_edit_score_home")
        self.button_score_guest_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_score_guest_plus.setGeometry(QtCore.QRect(90, 290, 41, 23))
        self.button_score_guest_plus.setObjectName("button_score_guest_plus")
        self.label_display_pos_x = QtWidgets.QLabel(self.centralwidget)
        self.label_display_pos_x.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label_display_pos_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display_pos_x.setObjectName("label_display_pos_x")
        self.line_edit_display_pos_x = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_display_pos_x.setGeometry(QtCore.QRect(90, 70, 51, 20))
        self.line_edit_display_pos_x.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_display_pos_x.setObjectName("line_edit_display_pos_x")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setEnabled(True)
        self.label_display.setGeometry(QtCore.QRect(10, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_display.setFont(font)
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")
        self.label_width = QtWidgets.QLabel(self.centralwidget)
        self.label_width.setEnabled(False)
        self.label_width.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.label_width.setAlignment(QtCore.Qt.AlignCenter)
        self.label_width.setObjectName("label_width")
        self.line_edit_display_height = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_display_height.setEnabled(False)
        self.line_edit_display_height.setGeometry(QtCore.QRect(90, 160, 51, 20))
        self.line_edit_display_height.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_display_height.setObjectName("line_edit_display_height")
        self.label_height = QtWidgets.QLabel(self.centralwidget)
        self.label_height.setEnabled(False)
        self.label_height.setGeometry(QtCore.QRect(10, 160, 61, 21))
        self.label_height.setAlignment(QtCore.Qt.AlignCenter)
        self.label_height.setObjectName("label_height")
        self.line_edit_display_width = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_display_width.setEnabled(False)
        self.line_edit_display_width.setGeometry(QtCore.QRect(90, 130, 51, 20))
        self.line_edit_display_width.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_display_width.setObjectName("line_edit_display_width")
        self.line_edit_display_pos_y = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_display_pos_y.setGeometry(QtCore.QRect(90, 100, 51, 20))
        self.line_edit_display_pos_y.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_display_pos_y.setObjectName("line_edit_display_pos_y")
        self.label_display_pos_y = QtWidgets.QLabel(self.centralwidget)
        self.label_display_pos_y.setGeometry(QtCore.QRect(10, 97, 61, 20))
        self.label_display_pos_y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display_pos_y.setObjectName("label_display_pos_y")
        self.button_select_emblem_guest = QtWidgets.QPushButton(self.centralwidget)
        self.button_select_emblem_guest.setGeometry(QtCore.QRect(200, 100, 111, 23))
        self.button_select_emblem_guest.setObjectName("button_select_emblem_guest")
        self.button_select_emblem_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_select_emblem_home.setGeometry(QtCore.QRect(200, 70, 111, 23))
        self.button_select_emblem_home.setObjectName("button_select_emblem_home")
        self.label_emblem = QtWidgets.QLabel(self.centralwidget)
        self.label_emblem.setEnabled(True)
        self.label_emblem.setGeometry(QtCore.QRect(200, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_emblem.setFont(font)
        self.label_emblem.setAlignment(QtCore.Qt.AlignCenter)
        self.label_emblem.setObjectName("label_emblem")
        self.button_select_background = QtWidgets.QPushButton(self.centralwidget)
        self.button_select_background.setGeometry(QtCore.QRect(200, 130, 111, 23))
        self.button_select_background.setObjectName("button_select_background")
        self.label_display_pos_x_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_display_pos_x_2.setGeometry(QtCore.QRect(210, 470, 31, 21))
        self.label_display_pos_x_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display_pos_x_2.setObjectName("label_display_pos_x_2")
        self.line_edit_display_time_pos_y = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_display_time_pos_y.setGeometry(QtCore.QRect(260, 500, 41, 20))
        self.line_edit_display_time_pos_y.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_display_time_pos_y.setObjectName("line_edit_display_time_pos_y")
        self.label_display_pos_y_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_display_pos_y_2.setGeometry(QtCore.QRect(210, 500, 31, 20))
        self.label_display_pos_y_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display_pos_y_2.setObjectName("label_display_pos_y_2")
        self.line_edit_display_time_pos_x = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_display_time_pos_x.setGeometry(QtCore.QRect(260, 470, 41, 20))
        self.line_edit_display_time_pos_x.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_display_time_pos_x.setObjectName("line_edit_display_time_pos_x")
        self.label_text = QtWidgets.QLabel(self.centralwidget)
        self.label_text.setEnabled(True)
        self.label_text.setGeometry(QtCore.QRect(370, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_text.setFont(font)
        self.label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text.setObjectName("label_text")
        self.button_select_text_color = QtWidgets.QPushButton(self.centralwidget)
        self.button_select_text_color.setGeometry(QtCore.QRect(370, 70, 111, 23))
        self.button_select_text_color.setObjectName("button_select_text_color")
        ControlWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlWindow)
        QtCore.QMetaObject.connectSlotsByName(ControlWindow)

    def retranslateUi(self, ControlWindow):
        _translate = QtCore.QCoreApplication.translate
        ControlWindow.setWindowTitle(_translate("ControlWindow", "SCK Anzeigetafel"))
        self.line_edit_time_manual_seconds.setText(_translate("ControlWindow", "00"))
        self.label_time_manual_double_point.setText(_translate("ControlWindow", ":"))
        self.label_time.setText(_translate("ControlWindow", "Zeit"))
        self.button_time_start.setText(_translate("ControlWindow", "Start"))
        self.line_edit_time_manual_minutes.setText(_translate("ControlWindow", "00"))
        self.button_time_reset.setText(_translate("ControlWindow", "Reset"))
        self.button_time_manual.setText(_translate("ControlWindow", "Manuell"))
        self.button_time_pause.setText(_translate("ControlWindow", "Pause"))
        self.label_score_double_point.setText(_translate("ControlWindow", ":"))
        self.button_score_home_minus.setText(_translate("ControlWindow", "-"))
        self.label_spielstand.setText(_translate("ControlWindow", "Spielstand"))
        self.line_edit_score_guest.setText(_translate("ControlWindow", "0"))
        self.button_score_guest_minus.setText(_translate("ControlWindow", "-"))
        self.button_score_home_plus.setText(_translate("ControlWindow", "+"))
        self.line_edit_score_home.setText(_translate("ControlWindow", "0"))
        self.button_score_guest_plus.setText(_translate("ControlWindow", "+"))
        self.label_display_pos_x.setText(_translate("ControlWindow", "X"))
        self.line_edit_display_pos_x.setText(_translate("ControlWindow", "0"))
        self.label_display.setText(_translate("ControlWindow", "Anzeige"))
        self.label_width.setText(_translate("ControlWindow", "Breite (%)"))
        self.line_edit_display_height.setText(_translate("ControlWindow", "0"))
        self.label_height.setText(_translate("ControlWindow", "Höhe  (%)"))
        self.line_edit_display_width.setText(_translate("ControlWindow", "0"))
        self.line_edit_display_pos_y.setText(_translate("ControlWindow", "0"))
        self.label_display_pos_y.setText(_translate("ControlWindow", "Y"))
        self.button_select_emblem_guest.setText(_translate("ControlWindow", "Wappen Gast"))
        self.button_select_emblem_home.setText(_translate("ControlWindow", "Wappen Heim"))
        self.label_emblem.setText(_translate("ControlWindow", "Bilder"))
        self.button_select_background.setText(_translate("ControlWindow", "Hintergrund"))
        self.label_display_pos_x_2.setText(_translate("ControlWindow", "X"))
        self.line_edit_display_time_pos_y.setText(_translate("ControlWindow", "0"))
        self.label_display_pos_y_2.setText(_translate("ControlWindow", "Y"))
        self.line_edit_display_time_pos_x.setText(_translate("ControlWindow", "0"))
        self.label_text.setText(_translate("ControlWindow", "Text"))
        self.button_select_text_color.setText(_translate("ControlWindow", "Farbe Einstellen"))
