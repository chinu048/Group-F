# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#

from PyQt4 import QtCore, QtGui
from time import time
import send_constant
import matplotlib.pyplot as plt

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
    # values,tim=[],[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(829, 638)
        MainWindow.setMinimumSize(QtCore.QSize(829, 638))
        MainWindow.setMaximumSize(QtCore.QSize(829, 638))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.sourcemeter = QtGui.QTabWidget(self.centralwidget)
        self.sourcemeter.setGeometry(QtCore.QRect(20, 10, 781, 571))
        self.sourcemeter.setObjectName(_fromUtf8("sourcemeter"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 30, 221, 171))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(397, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.constVolt = QtGui.QRadioButton(self.tab)
        self.constVolt.setGeometry(QtCore.QRect(410, 70, 151, 22))
        self.constVolt.setObjectName(_fromUtf8("constVolt"))
        self.constVolt.setChecked(True)


        self.sineVolt = QtGui.QRadioButton(self.tab)
        self.sineVolt.setGeometry(QtCore.QRect(410, 100, 117, 22))
        self.sineVolt.setObjectName(_fromUtf8("sineVolt"))
        self.voltage = QtGui.QLineEdit(self.tab)
        self.voltage.setGeometry(QtCore.QRect(450, 150, 91, 27))
        self.voltage.setText(_fromUtf8(""))
        self.voltage.setObjectName(_fromUtf8("voltage"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(380, 160, 51, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(550, 160, 68, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(410, 230, 181, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.totalTime = QtGui.QLineEdit(self.tab)
        self.totalTime.setGeometry(QtCore.QRect(430, 260, 91, 27))
        self.totalTime.setObjectName(_fromUtf8("totalTime"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(530, 270, 81, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.table = QtGui.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(290, 330, 401, 192))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.table.verticalHeader().setStretchLastSection(False)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.start = QtGui.QPushButton(self.tab)
        self.start.setGeometry(QtCore.QRect(650, 200, 99, 81))
        self.start.setObjectName(_fromUtf8("start"))
        # self.values,self.tim =
        self.start.clicked.connect(self.mainFun)

        self.plotGraph = QtGui.QPushButton(self.tab)
        self.plotGraph.setGeometry(QtCore.QRect(30, 390, 99, 27))
        self.plotGraph.setObjectName(_fromUtf8("plotGraph"))
        self.plotGraph.clicked.connect(self.graphPlot)

        self.yAxis = QtGui.QComboBox(self.tab)
        self.yAxis.setGeometry(QtCore.QRect(70, 300, 85, 27))
        self.yAxis.setObjectName(_fromUtf8("yAxis"))
        self.yAxis.addItem(_fromUtf8(""))
        self.yAxis.addItem(_fromUtf8(""))
        self.yAxis.addItem(_fromUtf8(""))
        self.xAxis = QtGui.QComboBox(self.tab)
        self.xAxis.setGeometry(QtCore.QRect(70, 350, 85, 27))
        self.xAxis.setObjectName(_fromUtf8("xAxis"))
        self.xAxis.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 51, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 350, 41, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))


        import download
        # import export
        self.exportReadings = QtGui.QPushButton(self.tab)
        self.exportReadings.setGeometry(QtCore.QRect(130, 480, 121, 27))
        self.exportReadings.setObjectName(_fromUtf8("exportReadings"))
        # self.exportReadings.clicked.connect(export.export)


        self.generate = QtGui.QPushButton(self.tab)
        self.generate.setGeometry(QtCore.QRect(130, 440, 111, 27))
        self.generate.setObjectName(_fromUtf8("generate"))
        self.generate.clicked.connect(download.save)


        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(37, 240, 141, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.sourcemeter.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.light = QtGui.QCheckBox(self.tab_2)
        self.light.setGeometry(QtCore.QRect(290, 20, 161, 22))
        self.light.setObjectName(_fromUtf8("light"))
        self.onTime = QtGui.QLineEdit(self.tab_2)
        self.onTime.setGeometry(QtCore.QRect(400, 90, 113, 27))
        self.onTime.setObjectName(_fromUtf8("onTime"))
        self.offTime = QtGui.QLineEdit(self.tab_2)
        self.offTime.setGeometry(QtCore.QRect(400, 140, 113, 27))
        self.offTime.setObjectName(_fromUtf8("offTime"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(310, 100, 68, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(310, 150, 68, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.apply = QtGui.QPushButton(self.tab_2)
        self.apply.setGeometry(QtCore.QRect(320, 240, 99, 27))
        self.apply.setObjectName(_fromUtf8("apply"))
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(290, 20, 161, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(400, 90, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 140, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(310, 100, 68, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(310, 150, 68, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.sourcemeter.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sourcemeter.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "SOURCERER", None))
        self.label_2.setText(_translate("MainWindow", "Voltage Specifications :", None))
        self.constVolt.setText(_translate("MainWindow", "Constant Voltage", None))
        self.sineVolt.setText(_translate("MainWindow", "Sine Wave", None))
        self.label_3.setText(_translate("MainWindow", "Value  :", None))
        self.label_4.setText(_translate("MainWindow", "( Volts )", None))
        self.label_5.setText(_translate("MainWindow", "Time Period of Experiment", None))
        self.label_6.setText(_translate("MainWindow", "( Seconds )", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Voltage", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Current", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Resistance", None))
        self.start.setText(_translate("MainWindow", "START", None))
        self.plotGraph.setText(_translate("MainWindow", "Plot Graph", None))
        self.yAxis.setItemText(0, _translate("MainWindow", "Current", None))
        self.yAxis.setItemText(1, _translate("MainWindow", "Voltage", None))
        self.yAxis.setItemText(2, _translate("MainWindow", "Resistance", None))
        self.xAxis.setItemText(0, _translate("MainWindow", "time", None))
        self.label_7.setText(_translate("MainWindow", "Y Axis", None))
        self.label_8.setText(_translate("MainWindow", "X Axis", None))
        self.exportReadings.setText(_translate("MainWindow", "Export Readings", None))
        self.generate.setText(_translate("MainWindow", "Generate CSV", None))
        self.sourcemeter.setTabText(self.sourcemeter.indexOf(self.tab), _translate("MainWindow", "Sourcemeter", None))
        self.checkBox.setText(_translate("MainWindow", "Use changing light ", None))
        self.label_9.setText(_translate("MainWindow", "OnTime", None))
        self.label_10.setText(_translate("MainWindow", "OffTime", None))
        self.apply.setText(_translate("MainWindow", "Apply", None))
        self.sourcemeter.setTabText(self.sourcemeter.indexOf(self.tab_2), _translate("MainWindow", "Arduino", None))



    def mainFun(self):
        volt = self.voltage.text()
        tm = self.totalTime.text()
        # values,tim = [],[]
        if volt == "" or tm == "":
            self.showMessageBox(MainWindow,"Please fill in all required fields","Error!")
        else:
            if self.constVolt.isChecked() == True:
                values,tim = send_constant.main(float(volt),float(tm))
                # values,tim = send_constant.main(volt,float(tm))
                for i in range(len(tim)):
                    self.table.insertRow(self.table.rowCount())
                    self.table.setItem(i, 0, QtGui.QTableWidgetItem(str(tim[i])))
                    for j in range(3):
                        self.table.setItem(i,j+1,QtGui.QTableWidgetItem(str(values[i][j])))


                y = str(self.yAxis.currentText())
                x = str(self.xAxis.currentText())
                b = tim
                volt, current,resistance=[],[],[]
                a=[]
                for tup in values:
                    volt.append(tup[0])
                    current.append(tup[1])
                    resistance.append(tup[2])


                if y == "Voltage":
                    a = volt
                elif y == "Current":
                    a = current
                else:
                    a = resistance
                import numpy as np
                plt.plot(b, a)
                plt.yticks(np.arange(0, max(a)+0.1*max(a), max(a)/10))
                plt.show()

        print(values)
        print(tim)
        # return values,tim

    def graphPlot(self):
        print("LOL")
        # y = str(self.yAxis.currentText())
        # x = str(self.xAxis.currentText())
        # b = tim
        # volt=[]
        # for tup in values:
        #     volt.append(tup[0])
        #     # current = tup[1] for tup in values
        # # resistance = tup[2] for tup in values
        # if y == "Voltage":
        #     a = volt
        # # elif y == "Current":
        #     # a = current
        # # else:
        #     # a = resistance
        #
        # plt.plot(b, a)
        # plt.show()


    def showMessageBox(self,win,message,title):
        msg = QtGui.QMessageBox(win)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
