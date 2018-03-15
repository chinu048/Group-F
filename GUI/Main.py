import visa
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys
import os
import math
import time
from PyQt4 import QtCore, QtGui

# import pyexcel as pe
# print(sys.path,len(sys.path))

import visa
rm = visa.ResourceManager()
###keithley = rm.open_resource("GPIB0::20::INSTR")

sys.path.append(os.path.dirname(os.getcwd()) + "/Generating-Functions" )
import send_sin
import send_cos
import send_constant

amplitude=10
freq=10
time_duration=10
phase=0

###send_sin.sin(keithley,amplitude ,freq ,time_duration , phase)
###send_cos.cos(keithley,amplitude ,freq ,time_duration , phase)
###send_constant.constant(keithley,amplitude,time_duration)

sys.path.append(os.path.dirname(os.getcwd()) + "/Set-UP" )
#import set_connection

# check = set_connection.setup()
# set_connection.reset()
# set_connection.output()

sys.path.append(os.path.dirname(os.getcwd()) + "/csv_download" )
import generate
###data=[1,2],[2,3]
###save_path = '/home/akash/Desktop'
###generate.save(data,save_path)
###

sys.path.append(os.path.dirname(os.getcwd()) + "/Arduino" )
import arduino


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def ardf_apply(self):
        ontime = int( self.lineEdit_2.text() )
        offtime = int( self.lineEdit_4.text() )
        totaltime = int( self.lineEdit_3.text() )
        arduino.ard(ontime,offtime,totaltime)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(805, 616)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.main_window = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_window.sizePolicy().hasHeightForWidth())
        self.main_window.setSizePolicy(sizePolicy)
        self.main_window.setObjectName(_fromUtf8("main_window"))
        self.sourcemeter_tab = QtGui.QWidget()
        self.sourcemeter_tab.setObjectName(_fromUtf8("sourcemeter_tab"))
        self.apply = QtGui.QPushButton(self.sourcemeter_tab)
        self.apply.setGeometry(QtCore.QRect(510, 120, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply.sizePolicy().hasHeightForWidth())
        self.apply.setSizePolicy(sizePolicy)
        self.apply.setObjectName(_fromUtf8("apply"))

###
###        self.apply.clicked.connect(self.f_apply)
###
        self.start = QtGui.QPushButton(self.sourcemeter_tab)
        self.start.setGeometry(QtCore.QRect(290, 340, 81, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setObjectName(_fromUtf8("start"))
###
###        self.start.clicked.connect(self.f_start)
###
        self.stop = QtGui.QPushButton(self.sourcemeter_tab)
        self.stop.setGeometry(QtCore.QRect(460, 340, 99, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy)
        self.stop.setObjectName(_fromUtf8("stop"))
###
###        self.stop.clicked.connect(self.f_stop)
###
        self.lineEdit = QtGui.QLineEdit(self.sourcemeter_tab)
        self.lineEdit.setGeometry(QtCore.QRect(320, 240, 51, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.export_reading = QtGui.QPushButton(self.sourcemeter_tab)
        self.export_reading.setGeometry(QtCore.QRect(20, 340, 111, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_reading.sizePolicy().hasHeightForWidth())
        self.export_reading.setSizePolicy(sizePolicy)
        self.export_reading.setObjectName(_fromUtf8("export_reading"))
        self.image = QtGui.QLabel(self.sourcemeter_tab)
        self.image.setGeometry(QtCore.QRect(10, 100, 271, 181))
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("Sourcerer.png")))
        self.image.setScaledContents(True)
        self.image.setObjectName(_fromUtf8("image"))
        self.horizontalScrollBar = QtGui.QScrollBar(self.sourcemeter_tab)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(430, 50, 231, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setMaximum(15)
        self.horizontalScrollBar.setPageStep(1)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName(_fromUtf8("horizontalScrollBar"))
        self.label_2 = QtGui.QLabel(self.sourcemeter_tab)
        self.label_2.setGeometry(QtCore.QRect(390, 50, 16, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.amplitude = QtGui.QLabel(self.sourcemeter_tab)
        self.amplitude.setGeometry(QtCore.QRect(300, 50, 81, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amplitude.sizePolicy().hasHeightForWidth())
        self.amplitude.setSizePolicy(sizePolicy)
        self.amplitude.setObjectName(_fromUtf8("amplitude"))
        self.label_9 = QtGui.QLabel(self.sourcemeter_tab)
        self.label_9.setGeometry(QtCore.QRect(200, 380, 68, 17))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.time_duration = QtGui.QLabel(self.sourcemeter_tab)
        self.time_duration.setGeometry(QtCore.QRect(400, 250, 131, 17))
        self.time_duration.setObjectName(_fromUtf8("time_duration"))
        self.sine_wave = QtGui.QRadioButton(self.sourcemeter_tab)
        self.sine_wave.setGeometry(QtCore.QRect(300, 100, 117, 22))
        self.sine_wave.setObjectName(_fromUtf8("sine_wave"))
        self.cos_wave = QtGui.QRadioButton(self.sourcemeter_tab)
        self.cos_wave.setGeometry(QtCore.QRect(300, 130, 117, 22))
        self.cos_wave.setObjectName(_fromUtf8("cos_wave"))
        self.constant_voltage = QtGui.QRadioButton(self.sourcemeter_tab)
        self.constant_voltage.setGeometry(QtCore.QRect(300, 160, 161, 22))
        self.constant_voltage.setObjectName(_fromUtf8("constant_voltage"))
        self.apply.raise_()
        self.horizontalScrollBar.raise_()
        self.start.raise_()
        self.stop.raise_()
        self.lineEdit.raise_()
        self.export_reading.raise_()
        self.image.raise_()
        self.label_2.raise_()
        self.amplitude.raise_()
        self.label_9.raise_()
        self.time_duration.raise_()
        self.sine_wave.raise_()
        self.cos_wave.raise_()
        self.constant_voltage.raise_()
        self.main_window.addTab(self.sourcemeter_tab, _fromUtf8(""))
        self.arduino_tab = QtGui.QWidget()
        self.arduino_tab.setObjectName(_fromUtf8("arduino_tab"))
        self.ard_apply = QtGui.QPushButton(self.arduino_tab)
        self.ard_apply.setGeometry(QtCore.QRect(380, 290, 99, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ard_apply.sizePolicy().hasHeightForWidth())
        self.ard_apply.setSizePolicy(sizePolicy)
        self.ard_apply.setObjectName(_fromUtf8("ard_apply"))

        self.lineEdit_3 = QtGui.QLineEdit(self.arduino_tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 220, 61, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.ard_time_interval = QtGui.QLabel(self.arduino_tab)
        self.ard_time_interval.setGeometry(QtCore.QRect(460, 220, 101, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ard_time_interval.sizePolicy().hasHeightForWidth())
        self.ard_time_interval.setSizePolicy(sizePolicy)
        self.ard_time_interval.setObjectName(_fromUtf8("ard_time_interval"))
        self.lineEdit_2 = QtGui.QLineEdit(self.arduino_tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 110, 61, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_4 = QtGui.QLineEdit(self.arduino_tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 160, 61, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label = QtGui.QLabel(self.arduino_tab)
        self.label.setGeometry(QtCore.QRect(470, 110, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.arduino_tab)
        self.label_3.setGeometry(QtCore.QRect(470, 160, 68, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.arduino_tab)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 221, 371))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("arduino.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.main_window.addTab(self.arduino_tab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit_9 = QtGui.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 210, 113, 27))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(220, 210, 68, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(220, 90, 91, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_10 = QtGui.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 150, 113, 27))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_12 = QtGui.QLineEdit(self.tab)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 90, 113, 27))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(220, 150, 81, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 290, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.main_window.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.main_window, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
###
        self.ard_apply.clicked.connect(self.ardf_apply)
###
        self.retranslateUi(MainWindow)
        self.main_window.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QObject.connect(self.horizontalScrollBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_2.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.main_window.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Plot</p></body></html>", None))
        self.apply.setText(_translate("MainWindow", "Apply", None))
        self.start.setText(_translate("MainWindow", "Start", None))
        self.stop.setText(_translate("MainWindow", "Stop", None))
        self.export_reading.setText(_translate("MainWindow", "Export reading", None))
        self.label_2.setText(_translate("MainWindow", "0", None))
        self.amplitude.setText(_translate("MainWindow", "Amplitude", None))
        self.time_duration.setText(_translate("MainWindow", "Time interval ", None))
        self.sine_wave.setText(_translate("MainWindow", "Sine Wave", None))
        self.cos_wave.setText(_translate("MainWindow", "Cos Wave", None))
        self.constant_voltage.setText(_translate("MainWindow", "Constant Voltage", None))
        self.main_window.setTabText(self.main_window.indexOf(self.sourcemeter_tab), _translate("MainWindow", "Sourcemeter", None))
        self.ard_apply.setText(_translate("MainWindow", "Apply", None))
        self.ard_time_interval.setText(_translate("MainWindow", "  Total  Time ", None))
        self.label.setText(_translate("MainWindow", "On Time", None))
        self.label_3.setText(_translate("MainWindow", "Off Time", None))
        self.main_window.setTabText(self.main_window.indexOf(self.arduino_tab), _translate("MainWindow", "Arduino", None))
        self.label_7.setText(_translate("MainWindow", "Interval", None))
        self.label_8.setText(_translate("MainWindow", "start Time", None))
        self.label_10.setText(_translate("MainWindow", "End Time", None))
        self.pushButton_2.setText(_translate("MainWindow", "Plot", None))
        self.main_window.setTabText(self.main_window.indexOf(self.tab), _translate("MainWindow", "Page", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
