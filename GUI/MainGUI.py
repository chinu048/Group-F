# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sandarbh/Desktop/Sourcerer/GUI/mainwindow.ui'
#
# Created: Fri Apr  6 02:43:54 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import send_constant
import step_voltage
import plot
import mailing

from PyQt4 import QtCore, QtGui
import sqlite3
import matplotlib.pyplot as plt
import ExportGUI
import export
import forgotPassword
import arduino

db = sqlite3.connect("SoftwareProject.db")
cur = db.cursor()
cur.execute("create table if not exists User (userid varchar(30),name varchar(30),password varchar(20),email varchar(40));")

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

    def __init__(self):

        self.values = []
        self.tim = []
        self.lcolor = "black"
        self.bcolor = "white"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1189, 861)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitle"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("ToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"/*Primary (Blue) : #4988af\n"
"Ghost White : #f6f8ff\n"
"Secondary(Green) : #44cf6c*/\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color:#f6f8ff;\n"
"  border-radius: 10;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #44cf6c;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #44cf6c;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #44cf6c;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #44cf6c*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    border: 2px solid #44cf6c;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"  color:#323232;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #4988af;\n"
"  border-radius:15;\n"
"  padding-left:10px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #f6f8ff;\n"
"  background-color: #4988af;\n"
"    border-width: 1px;\n"
"    border-color: #4988af;\n"
"    border-style: solid;\n"
"    border-radius: 15;\n"
"    padding: 5px;\n"
"    font-size: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"  width: 100px;\n"
"  margin-top:10px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #44cf6c;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #44cf6c, stop: 1 #44cf6c);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #44cf6c;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #44cf6c);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #44cf6c, stop: 1 #44cf6c);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #44cf6c, stop: 1 #44cf6c);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: #437ca0;\n"
"     height: 10px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: #e1e8e1;\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #44cf6c);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #44cf6c);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: #fff;\n"
"      width: 10px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #4988af;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    /*437ca0*/\n"
"      background: #e1e8e1;\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #34617c;\n"
"      border-radius: 2px;\n"
"      background: #34617c;\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #34617c;\n"
"      border-radius: 2px;\n"
"      background: #34617c;\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid #44cf6c;\n"
"      width: 2px;\n"
"      height: 2px;\n"
"      background: #44cf6c;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"/*QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}*/\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #44cf6c, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #44cf6c;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #4988af;\n"
"    border: 0px solid #444;\n"
"    /*border-bottom-style: none;*/\n"
"    background-color: #f6f8ff;\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    padding-top: 10px;\n"
"    padding-bottom: 5px;\n"
"    margin-right: 1px;\n"
"  margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar:focus{\n"
"    border: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 0px solid #444;\n"
"    top: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #f6f8ff;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: #4988af;\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"  background-color: #e1e8e1;\n"
"  color: #4988af;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #44cf6c;\n"
"    padding-bottom: 3px;\n"
"  #edff7a\n"
"  #ffd23f\n"
"  #f46036*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: #44cf6c;\n"
"  color: #274690;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #44cf6c;\n"
"    background-color: #f6f8ff;\n"
"    border: 2px solid #4988af;\n"
"    border-radius: 6px;\n"
"  padding : 15px;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"    border: 0px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: #44cf6c;\n"
"  border-radius: 6px;\n"
"  padding : 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 1px solid #4988af;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover{\n"
"  border: 1px solid #44cf6c;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #000;\n"
"    background-color: #f6f8ff;\n"
"    border: 2px solid #4988af;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #44cf6c;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"QCheckBox:focus{\n"
"    border: 0px;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"QMainWindow{\n"
"\n"
"  background-color:#f6f8ff;\n"
"  margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: #f6f8ff;\n"
"    background-color: #4988af;\n"
"      border: 1px solid #fffff8;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    padding: 4px;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    padding: 2px;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"QLabel:focus{\n"
"    border: 0px;\n"
"}\n"
""))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setStyleSheet(_fromUtf8("background-color:#f6f8ff"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralWidget)
        self.stackedWidget.setStyleSheet(_fromUtf8(""))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.login = QtGui.QWidget()
        self.login.setMinimumSize(QtCore.QSize(335, 0))
        self.login.setObjectName(_fromUtf8("login"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.login)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.image = QtGui.QLabel(self.login)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.image.setFont(font)
        self.image.setStyleSheet(_fromUtf8("background-color:#f6f8ff"))
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/sourcemeter.png")))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setMargin(0)
        self.image.setObjectName(_fromUtf8("image"))
        self.image.setFocusPolicy(QtCore.Qt.TabFocus)
        self.image.setFocus()
        self.horizontalLayout_3.addWidget(self.image)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_5.setContentsMargins(50, -1, 50, -1)
        self.formLayout_5.setVerticalSpacing(25)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_7 = QtGui.QLabel(self.login)
        self.label_7.setMaximumSize(QtCore.QSize(16666015, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8(""))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setMargin(20)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_7)
        self.usrname = QtGui.QLineEdit(self.login)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.usrname.setFont(font)
        self.usrname.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.usrname.setText(_fromUtf8(""))
        self.usrname.setObjectName(_fromUtf8("usrname"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.usrname)
        self.pwd = QtGui.QLineEdit(self.login)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.pwd.setFont(font)
        self.pwd.setWhatsThis(_fromUtf8(""))
        self.pwd.setAccessibleName(_fromUtf8(""))
        self.pwd.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.pwd.setInputMask(_fromUtf8(""))
        self.pwd.setText(_fromUtf8(""))
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pwd.setObjectName(_fromUtf8("pwd"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.pwd)
        self.Login = QtGui.QPushButton(self.login)
        self.Login.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Login.setFont(font)
        self.Login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Login.setStyleSheet(_fromUtf8("padding:5px;\n"
"border-radius:15;margin-top:10px;\n"
"background-color: #4988af;"))
        self.Login.setFlat(False)
        self.Login.setObjectName(_fromUtf8("Login"))
        self.Login.clicked.connect(self.loginClicked)

        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.Login)
        self.goToSignup = QtGui.QLabel(self.login)
        self.goToSignup.setMouseTracking(True)
        self.goToSignup.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.goToSignup.setObjectName(_fromUtf8("goToSignup"))
        self.goToSignup.mouseReleaseEvent = self.setSignupWindow

        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.goToSignup)
        self.label_9 = QtGui.QLabel(self.login)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_5.setWidget(7, QtGui.QFormLayout.FieldRole, self.label_9)
        self.label_9.mouseReleaseEvent = self.forgetPassword

        self.horizontalLayout_3.addLayout(self.formLayout_5)
        self.stackedWidget.addWidget(self.login)
        self.signup = QtGui.QWidget()
        self.signup.setObjectName(_fromUtf8("signup"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.signup)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.image_signup = QtGui.QLabel(self.signup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_signup.sizePolicy().hasHeightForWidth())
        self.image_signup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.image_signup.setFont(font)
        self.image_signup.setStyleSheet(_fromUtf8(""))
        self.image_signup.setText(_fromUtf8(""))
        self.image_signup.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/sourcemeter.png")))
        self.image_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.image_signup.setMargin(0)
        self.image_signup.setObjectName(_fromUtf8("image_signup"))
        self.image_signup.setFocusPolicy(QtCore.Qt.TabFocus)
        self.image_signup.setFocus()
        self.horizontalLayout_2.addWidget(self.image_signup)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_6.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_6.setContentsMargins(50, -1, 50, -1)
        self.formLayout_6.setVerticalSpacing(25)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_10 = QtGui.QLabel(self.signup)
        self.label_10.setMaximumSize(QtCore.QSize(16666015, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8(""))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setMargin(20)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_10)
        self.name = QtGui.QLineEdit(self.signup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.name.setObjectName(_fromUtf8("name"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.name)
        self.sign_usrname = QtGui.QLineEdit(self.signup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.sign_usrname.setFont(font)
        self.sign_usrname.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.sign_usrname.setObjectName(_fromUtf8("sign_usrname"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.FieldRole, self.sign_usrname)
        self.sign_pwd = QtGui.QLineEdit(self.signup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.sign_pwd.setFont(font)
        self.sign_pwd.setWhatsThis(_fromUtf8(""))
        self.sign_pwd.setAccessibleName(_fromUtf8(""))
        self.sign_pwd.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.sign_pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.sign_pwd.setInputMask(_fromUtf8(""))
        self.sign_pwd.setText(_fromUtf8(""))
        self.sign_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.sign_pwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sign_pwd.setObjectName(_fromUtf8("sign_pwd"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.FieldRole, self.sign_pwd)
        self.conf_pwd = QtGui.QLineEdit(self.signup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.conf_pwd.setFont(font)
        self.conf_pwd.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.conf_pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.conf_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.conf_pwd.setObjectName(_fromUtf8("conf_pwd"))
        self.formLayout_6.setWidget(5, QtGui.QFormLayout.FieldRole, self.conf_pwd)
        self.noIdea = QtGui.QLineEdit(self.signup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.noIdea.setFont(font)
        self.noIdea.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.noIdea.setObjectName(_fromUtf8("noIdea"))
        self.formLayout_6.setWidget(6, QtGui.QFormLayout.FieldRole, self.noIdea)
        self.Signup = QtGui.QPushButton(self.signup)
        self.Signup.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Signup.setFont(font)
        self.Signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Signup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Signup.setStyleSheet(_fromUtf8("padding:5px;\n"
"border-radius:15;margin-top:10px;\n"
"background-color: #4988af;"))
        self.Signup.setFlat(False)
        self.Signup.setObjectName(_fromUtf8("Signup"))
        self.Signup.clicked.connect(self.submitClicked)

        self.formLayout_6.setWidget(7, QtGui.QFormLayout.FieldRole, self.Signup)
        self.goToLogin = QtGui.QLabel(self.signup)
        self.goToLogin.setMouseTracking(True)
        self.goToLogin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.goToLogin.setObjectName(_fromUtf8("goToLogin"))
        self.goToLogin.mouseReleaseEvent = self.setLoginWindow

        self.formLayout_6.setWidget(8, QtGui.QFormLayout.FieldRole, self.goToLogin)
        self.horizontalLayout_2.addLayout(self.formLayout_6)
        self.stackedWidget.addWidget(self.signup)
        self.Main = QtGui.QWidget()
        self.Main.setStyleSheet(_fromUtf8("background-color:#f6f8ff"))
        self.Main.setObjectName(_fromUtf8("Main"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.Main)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.Main)
        self.scrollArea.setStyleSheet(_fromUtf8("QScrollBar:vertical\n"
"{\n"
"      background: #fff;\n"
"      width: 10px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #4988af;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    /*437ca0*/\n"
"      background: #e1e8e1;\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #34617c;\n"
"      border-radius: 2px;\n"
"      background: #34617c;\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #34617c;\n"
"      border-radius: 2px;\n"
"      background: #34617c;\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid #44cf6c;\n"
"      width: 2px;\n"
"      height: 2px;\n"
"      background: #44cf6c;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #4988af;\n"
"     background: #ffffff;\n"
"     height: 10px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: #e1e8e1;\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #34617c;\n"
"      border-radius: 2px;\n"
"      background: #34617c;\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #34617c;\n"
"      border-radius: 2px;\n"
"      background: #34617c;\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid #44cf6c;\n"
"      width: 2px;\n"
"      height: 2px;\n"
"      background: #44cf6c;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1153, 783))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.tabWidget = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color : #eff7ef\n"
"/*#eaf2ea*/"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Sourcerer = QtGui.QWidget()
        self.Sourcerer.setObjectName(_fromUtf8("Sourcerer"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.Sourcerer)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.image_main_1 = QtGui.QLabel(self.Sourcerer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_main_1.sizePolicy().hasHeightForWidth())
        self.image_main_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.image_main_1.setFont(font)
        self.image_main_1.setStyleSheet(_fromUtf8("margin-right: 20px;"))
        self.image_main_1.setText(_fromUtf8(""))
        self.image_main_1.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/sourcemeter.png")))
        self.image_main_1.setAlignment(QtCore.Qt.AlignCenter)
        self.image_main_1.setMargin(0)
        self.image_main_1.setObjectName(_fromUtf8("image_main_1"))
        self.image_main_1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.image_main_1.setFocus()
        self.horizontalLayout_8.addWidget(self.image_main_1)
        self.groupBox = QtGui.QGroupBox(self.Sourcerer)
        self.groupBox.setStyleSheet(_fromUtf8("color:#3a3a3a;"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.const_volt = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        self.const_volt.setFont(font)
        self.const_volt.setObjectName(_fromUtf8("const_volt"))

        self.const_volt.setChecked(True)
        self.const_volt.toggled.connect(lambda :self.radioButtonFun(1))

        self.verticalLayout.addWidget(self.const_volt)
        self.sine_volt = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        self.sine_volt.setFont(font)
        self.sine_volt.setStyleSheet(_fromUtf8("focus{\n"
"    border: 0px;\n"
"}"))
        self.sine_volt.setObjectName(_fromUtf8("sine_volt"))
        self.sine_volt.toggled.connect(lambda :self.radioButtonFun(2))

        self.verticalLayout.addWidget(self.sine_volt)
        self.var_volt = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        self.var_volt.setFont(font)
        self.var_volt.setObjectName(_fromUtf8("var_volt"))
        self.var_volt.toggled.connect(lambda :self.radioButtonFun(3))

        self.verticalLayout.addWidget(self.var_volt)
        self.voltage_input = QtGui.QStackedWidget(self.groupBox)
        self.voltage_input.setStyleSheet(_fromUtf8(""))
        self.voltage_input.setObjectName(_fromUtf8("voltage_input"))
        self.cont_voltage = QtGui.QWidget()
        self.cont_voltage.setObjectName(_fromUtf8("cont_voltage"))
        self.formLayout_2 = QtGui.QFormLayout(self.cont_voltage)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_17 = QtGui.QLabel(self.cont_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(_fromUtf8("color:#3a3a3a;"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_17)
        self.voltageValue_2 = QtGui.QLineEdit(self.cont_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.voltageValue_2.setFont(font)
        self.voltageValue_2.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.voltageValue_2.setObjectName(_fromUtf8("voltageValue_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.voltageValue_2)
        self.label_18 = QtGui.QLabel(self.cont_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8("color:#3a3a3a;"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_18)
        self.duration_2 = QtGui.QLineEdit(self.cont_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.duration_2.setFont(font)
        self.duration_2.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.duration_2.setObjectName(_fromUtf8("duration_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.duration_2)
        self.toggle_led0 = QtGui.QCheckBox(self.cont_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.toggle_led0.setFont(font)
        self.toggle_led0.setStyleSheet(_fromUtf8("margin-top: 10px;"))
        self.toggle_led0.setObjectName(_fromUtf8("toggle_led0"))
        self.toggle_led0.toggled.connect(lambda: self.ledOptions(0))

        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.toggle_led0)
        self.options00 = QtGui.QGroupBox(self.cont_voltage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options00.sizePolicy().hasHeightForWidth())
        self.options00.setSizePolicy(sizePolicy)
        self.options00.setTitle(_fromUtf8(""))
        self.options00.setObjectName(_fromUtf8("options00"))
        self.options00.setVisible(False)

        self.formLayout_11 = QtGui.QFormLayout(self.options00)
        self.formLayout_11.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_11.setObjectName(_fromUtf8("formLayout_11"))
        self.label_42 = QtGui.QLabel(self.options00)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.formLayout_11.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_42)
        self.compliance0 = QtGui.QLineEdit(self.options00)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.compliance0.setFont(font)
        self.compliance0.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.compliance0.setObjectName(_fromUtf8("compliance0"))
        self.formLayout_11.setWidget(2, QtGui.QFormLayout.FieldRole, self.compliance0)
        self.label_43 = QtGui.QLabel(self.options00)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.formLayout_11.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_43)
        self.voltrange0 = QtGui.QLineEdit(self.options00)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.voltrange0.setFont(font)
        self.voltrange0.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.voltrange0.setObjectName(_fromUtf8("voltrange0"))
        self.formLayout_11.setWidget(4, QtGui.QFormLayout.FieldRole, self.voltrange0)
        self.label_44 = QtGui.QLabel(self.options00)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.formLayout_11.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_44)
        self.resrange0 = QtGui.QLineEdit(self.options00)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.resrange0.setFont(font)
        self.resrange0.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.resrange0.setObjectName(_fromUtf8("resrange0"))
        self.formLayout_11.setWidget(5, QtGui.QFormLayout.FieldRole, self.resrange0)
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.SpanningRole, self.options00)
        self.var_start_3 = QtGui.QPushButton(self.cont_voltage)
        self.var_start_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.var_start_3.setFont(font)
        self.var_start_3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.var_start_3.setStyleSheet(_fromUtf8("padding:5px;\n"
"color: #f6f8ff;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.var_start_3.setObjectName(_fromUtf8("var_start_3"))
        self.var_start_3.clicked.connect(self.startExperiment)


        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.var_start_3)
        self.addopt0 = QtGui.QCheckBox(self.cont_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.addopt0.setFont(font)
        self.addopt0.setStyleSheet(_fromUtf8("margin-top:5px;"))
        self.addopt0.setObjectName(_fromUtf8("addopt0"))
        self.addopt0.toggled.connect(lambda :self.additionalOptions(self.addopt0))

        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.addopt0)
        self.voltage_input.addWidget(self.cont_voltage)

        ##
        self.sine_voltage = QtGui.QWidget()
        self.sine_voltage.setObjectName(_fromUtf8("sine_voltage"))
        self.formLayout_8 = QtGui.QFormLayout(self.sine_voltage)
        self.formLayout_8.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.amplitude = QtGui.QLabel(self.sine_voltage)
        self.amplitude.setObjectName(_fromUtf8("amplitude"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.LabelRole, self.amplitude)
        self.sine_amp = QtGui.QLineEdit(self.sine_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.sine_amp.setFont(font)
        self.sine_amp.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.sine_amp.setObjectName(_fromUtf8("sine_amp"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.FieldRole, self.sine_amp)
        self.label_35 = QtGui.QLabel(self.sine_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(_fromUtf8("color:#3a3a3a;"))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_35)
        self.sine_phase = QtGui.QLineEdit(self.sine_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.sine_phase.setFont(font)
        self.sine_phase.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.sine_phase.setObjectName(_fromUtf8("sine_phase"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.FieldRole, self.sine_phase)
        self.label_39 = QtGui.QLabel(self.sine_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet(_fromUtf8("color:#3a3a3a;"))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.formLayout_8.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_39)
        self.sine_frequency = QtGui.QLineEdit(self.sine_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.sine_frequency.setFont(font)
        self.sine_frequency.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.sine_frequency.setObjectName(_fromUtf8("sine_frequency"))
        self.formLayout_8.setWidget(2, QtGui.QFormLayout.FieldRole, self.sine_frequency)
        self.toggle_led1 = QtGui.QCheckBox(self.sine_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.toggle_led1.setFont(font)
        self.toggle_led1.setStyleSheet(_fromUtf8("margin-top: 10px;"))
        self.toggle_led1.setObjectName(_fromUtf8("toggle_led1"))
        self.formLayout_8.setWidget(4, QtGui.QFormLayout.FieldRole, self.toggle_led1)
        self.addopt1 = QtGui.QCheckBox(self.sine_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.addopt1.setFont(font)
        self.addopt1.setStyleSheet(_fromUtf8("margin-top: 5px;"))
        self.addopt1.setObjectName(_fromUtf8("addopt1"))
        self.formLayout_8.setWidget(5, QtGui.QFormLayout.FieldRole, self.addopt1)
        self.options01 = QtGui.QGroupBox(self.sine_voltage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options01.sizePolicy().hasHeightForWidth())
        self.options01.setSizePolicy(sizePolicy)
        self.options01.setTitle(_fromUtf8(""))
        self.options01.setObjectName(_fromUtf8("options01"))
        self.formLayout_12 = QtGui.QFormLayout(self.options01)
        self.formLayout_12.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_12.setObjectName(_fromUtf8("formLayout_12"))
        self.label_45 = QtGui.QLabel(self.options01)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.formLayout_12.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_45)
        self.compliance1 = QtGui.QLineEdit(self.options01)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.compliance1.setFont(font)
        self.compliance1.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.compliance1.setObjectName(_fromUtf8("compliance1"))
        self.formLayout_12.setWidget(2, QtGui.QFormLayout.FieldRole, self.compliance1)
        self.label_46 = QtGui.QLabel(self.options01)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.formLayout_12.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_46)
        self.voltrange1 = QtGui.QLineEdit(self.options01)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.voltrange1.setFont(font)
        self.voltrange1.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.voltrange1.setObjectName(_fromUtf8("voltrange1"))
        self.formLayout_12.setWidget(4, QtGui.QFormLayout.FieldRole, self.voltrange1)
        self.label_47 = QtGui.QLabel(self.options01)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.formLayout_12.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_47)
        self.resrange1 = QtGui.QLineEdit(self.options01)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.resrange1.setFont(font)
        self.resrange1.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.resrange1.setObjectName(_fromUtf8("resrange1"))
        self.formLayout_12.setWidget(5, QtGui.QFormLayout.FieldRole, self.resrange1)
        self.formLayout_8.setWidget(6, QtGui.QFormLayout.SpanningRole, self.options01)
        self.var_start_4 = QtGui.QPushButton(self.sine_voltage)
        self.var_start_4.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.var_start_4.setFont(font)
        self.var_start_4.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.var_start_4.setStyleSheet(_fromUtf8("padding:5px;\n"
"color: #f6f8ff;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.var_start_4.setObjectName(_fromUtf8("var_start_4"))
        self.formLayout_8.setWidget(7, QtGui.QFormLayout.FieldRole, self.var_start_4)
        self.sine_duration = QtGui.QLineEdit(self.sine_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.sine_duration.setFont(font)
        self.sine_duration.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.sine_duration.setObjectName(_fromUtf8("sine_duration"))
        self.formLayout_8.setWidget(3, QtGui.QFormLayout.FieldRole, self.sine_duration)
        self.dur_exp = QtGui.QLabel(self.sine_voltage)
        self.dur_exp.setObjectName(_fromUtf8("dur_exp"))
        self.formLayout_8.setWidget(3, QtGui.QFormLayout.LabelRole, self.dur_exp)
        self.voltage_input.addWidget(self.sine_voltage)

        ##
        self.variable_voltage = QtGui.QWidget()
        self.variable_voltage.setObjectName(_fromUtf8("variable_voltage"))
        self.formLayout_3 = QtGui.QFormLayout(self.variable_voltage)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_19 = QtGui.QLabel(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(_fromUtf8("color:#3a3a3a;"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_19)
        self.voltageValue_3 = QtGui.QLineEdit(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.voltageValue_3.setFont(font)
        self.voltageValue_3.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.voltageValue_3.setObjectName(_fromUtf8("voltageValue_3"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.voltageValue_3)
        self.label_20 = QtGui.QLabel(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(_fromUtf8("color:#3a3a3a;"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_20)
        self.duration_3 = QtGui.QLineEdit(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.duration_3.setFont(font)
        self.duration_3.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.duration_3.setObjectName(_fromUtf8("duration_3"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.duration_3)
        self.label_21 = QtGui.QLabel(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_21)
        self.lineEdit_3 = QtGui.QLineEdit(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.toggle_led2 = QtGui.QCheckBox(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.toggle_led2.setFont(font)
        self.toggle_led2.setStyleSheet(_fromUtf8("margin-top: 10px;"))
        self.toggle_led2.setObjectName(_fromUtf8("toggle_led2"))
        self.toggle_led2.toggled.connect(lambda: self.ledOptions(2))

        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.toggle_led2)
        self.addopt2 = QtGui.QCheckBox(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.addopt2.setFont(font)
        self.addopt2.setStyleSheet(_fromUtf8("margin-top: 5px;"))
        self.addopt2.setObjectName(_fromUtf8("addopt2"))
        self.addopt2.toggled.connect(lambda :self.additionalOptions(self.addopt2))

        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.addopt2)
        self.options02 = QtGui.QGroupBox(self.variable_voltage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options02.sizePolicy().hasHeightForWidth())
        self.options02.setSizePolicy(sizePolicy)
        self.options02.setTitle(_fromUtf8(""))
        self.options02.setObjectName(_fromUtf8("options02"))
        self.options02.setVisible(False)

        self.formLayout_10 = QtGui.QFormLayout(self.options02)
        self.formLayout_10.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_10.setObjectName(_fromUtf8("formLayout_10"))
        self.label_36 = QtGui.QLabel(self.options02)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.formLayout_10.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_36)
        self.compliance2 = QtGui.QLineEdit(self.options02)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.compliance2.setFont(font)
        self.compliance2.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.compliance2.setObjectName(_fromUtf8("compliance2"))
        self.formLayout_10.setWidget(2, QtGui.QFormLayout.FieldRole, self.compliance2)
        self.label_37 = QtGui.QLabel(self.options02)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.formLayout_10.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_37)
        self.voltrange2 = QtGui.QLineEdit(self.options02)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.voltrange2.setFont(font)
        self.voltrange2.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.voltrange2.setObjectName(_fromUtf8("voltrange2"))
        self.formLayout_10.setWidget(4, QtGui.QFormLayout.FieldRole, self.voltrange2)
        self.label_38 = QtGui.QLabel(self.options02)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.formLayout_10.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_38)
        self.resrange2 = QtGui.QLineEdit(self.options02)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.resrange2.setFont(font)
        self.resrange2.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.resrange2.setObjectName(_fromUtf8("resrange2"))
        self.formLayout_10.setWidget(5, QtGui.QFormLayout.FieldRole, self.resrange2)
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.SpanningRole, self.options02)
        self.var_start = QtGui.QPushButton(self.variable_voltage)
        self.var_start.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.var_start.setFont(font)
        self.var_start.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.var_start.setStyleSheet(_fromUtf8("padding:5px;\n"
"color: #f6f8ff;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.var_start.setObjectName(_fromUtf8("var_start"))
        self.var_start.clicked.connect(self.stepVoltage)

        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.var_start)
        self.voltage_input.addWidget(self.variable_voltage)
        self.verticalLayout.addWidget(self.voltage_input)
        self.horizontalLayout_8.addWidget(self.groupBox)
        self.tabWidget.addTab(self.Sourcerer, _fromUtf8(""))
        self.Graph = QtGui.QWidget()
        self.Graph.setObjectName(_fromUtf8("Graph"))
        self.gridLayout_7 = QtGui.QGridLayout(self.Graph)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.valuesTable = QtGui.QTableWidget(self.Graph)
        self.valuesTable.setStyleSheet(_fromUtf8("/*selection-background-color: #4988af;\n"
"alternate-background-color: #000000;*/\n"
"\n"
""))
        self.valuesTable.setRowCount(0)
        self.valuesTable.setObjectName(_fromUtf8("valuesTable"))
        self.valuesTable.setColumnCount(4)
        self.valuesTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        item = QtGui.QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(3, item)
        self.valuesTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout_7.addWidget(self.valuesTable, 0, 0, 3, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.export_2 = QtGui.QPushButton(self.Graph)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_2.sizePolicy().hasHeightForWidth())
        self.export_2.setSizePolicy(sizePolicy)
        self.export_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.export_2.setStyleSheet(_fromUtf8("padding:5px;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.export_2.setObjectName(_fromUtf8("export_2"))
        self.export_2.clicked.connect(self.file_open)

        self.gridLayout_2.addWidget(self.export_2, 0, 1, 1, 1)
        self.plot_graph = QtGui.QPushButton(self.Graph)
        self.plot_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plot_graph.setStyleSheet(_fromUtf8("padding:5px;\n"
"color: #f6f8ff;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.plot_graph.setObjectName(_fromUtf8("plot_graph"))
        self.plot_graph.clicked.connect(self.plotGraph)

        self.gridLayout_2.addWidget(self.plot_graph, 0, 2, 1, 1)
        self.csv = QtGui.QPushButton(self.Graph)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.csv.sizePolicy().hasHeightForWidth())
        self.csv.setSizePolicy(sizePolicy)
        self.csv.setMaximumSize(QtCore.QSize(180, 16777215))
        self.csv.setStyleSheet(_fromUtf8("padding:5px;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.csv.setObjectName(_fromUtf8("csv"))
        self.gridLayout_2.addWidget(self.csv, 0, 0, 1, 1)

        self.csv.clicked.connect(self.file_save)

        self.gridLayout_7.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setContentsMargins(-1, -1, -1, 10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.xAxis = QtGui.QComboBox(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garuda"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.xAxis.setFont(font)
        self.xAxis.setStyleSheet(_fromUtf8("padding : 5px;color: #4988af;\n"
"border: 1px solid #4988af;\n"
"/*44cf6c*/"))
        self.xAxis.setObjectName(_fromUtf8("xAxis"))
        self.xAxis.addItem(_fromUtf8(""))
        self.xAxis.addItem(_fromUtf8(""))
        self.xAxis.addItem(_fromUtf8(""))
        self.xAxis.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.xAxis, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.bgColor = QtGui.QPushButton(self.Graph)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.bgColor.setFont(font)
        self.bgColor.setStyleSheet(_fromUtf8("border-radius: 5px;"))
        self.bgColor.setText(_fromUtf8(""))
        self.bgColor.setObjectName(_fromUtf8("bgColor"))
        self.bgColor.clicked.connect(lambda : self.color_picker(1))

        self.gridLayout.addWidget(self.bgColor, 1, 3, 1, 1)
        self.lineEdit_18 = QtGui.QLineEdit(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet(_fromUtf8("border-radius: 5;"))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.gridLayout.addWidget(self.lineEdit_18, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_32 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout.addWidget(self.label_32, 3, 0, 1, 1)
        self.lineColor = QtGui.QPushButton(self.Graph)
        self.lineColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineColor.setFont(font)
        self.lineColor.setStyleSheet(_fromUtf8("border-radius: 5px;"))
        self.lineColor.setText(_fromUtf8(""))
        self.lineColor.setObjectName(_fromUtf8("lineColor"))
        self.lineColor.clicked.connect(lambda :self.color_picker(0))

        self.gridLayout.addWidget(self.lineColor, 1, 1, 1, 1)
        self.yAxis = QtGui.QComboBox(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garuda"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yAxis.setFont(font)
        self.yAxis.setStyleSheet(_fromUtf8("padding : 5px; color: #4988af;\n"
"border: 1px solid #4988af;"))
        self.yAxis.setObjectName(_fromUtf8("yAxis"))
        self.yAxis.addItem(_fromUtf8(""))
        self.yAxis.addItem(_fromUtf8(""))
        self.yAxis.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.yAxis, 0, 3, 1, 1)
        self.label_40 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout.addWidget(self.label_40, 2, 0, 1, 1)
        self.lineEdit_19 = QtGui.QLineEdit(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setStyleSheet(_fromUtf8("border-radius: 5;"))
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.gridLayout.addWidget(self.lineEdit_19, 2, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_41 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout.addWidget(self.label_41, 2, 2, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet(_fromUtf8("border-radius: 5;"))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout.addWidget(self.lineEdit_9, 3, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout.addWidget(self.label_33, 3, 2, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet(_fromUtf8("border-radius: 5;"))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout.addWidget(self.lineEdit_10, 3, 3, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet(_fromUtf8("border-radius: 5;"))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout.addWidget(self.lineEdit_11, 4, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout.addWidget(self.radioButton, 4, 0, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout.addWidget(self.radioButton_2, 4, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.Graph, _fromUtf8(""))
        self.Arduino = QtGui.QWidget()
        self.Arduino.setObjectName(_fromUtf8("Arduino"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Arduino)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.Arduino)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 4, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.Arduino)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(_fromUtf8("margin: 10px;"))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_3.addWidget(self.lineEdit_4, 4, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(358, 374, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 3, 5, 1)
        spacerItem2 = QtGui.QSpacerItem(428, 188, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 2, 3)
        self.lineEdit_2 = QtGui.QLineEdit(self.Arduino)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(_fromUtf8("margin: 10px;"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.Arduino)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("margin: 10px;"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_3.addWidget(self.lineEdit, 2, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.Arduino)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 3, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.Arduino)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 2, 1, 1, 1)
        self.arduino_start = QtGui.QPushButton(self.Arduino)
        self.arduino_start.setMaximumSize(QtCore.QSize(150, 16777215))
        self.arduino_start.setStyleSheet(_fromUtf8("margin: 10px;\n"
"background-color: #4988af;\n"
"border-radius: 5;"))
        self.arduino_start.setObjectName(_fromUtf8("arduino_start"))
        self.gridLayout_3.addWidget(self.arduino_start, 5, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(278, 628, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 6, 1)
        spacerItem4 = QtGui.QSpacerItem(428, 252, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 6, 1, 1, 3)
        self.tabWidget.addTab(self.Arduino, _fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.Main)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1189, 20))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)

        self.voltage_input.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Login, self.pwd)
        MainWindow.setTabOrder(self.pwd, self.usrname)
        MainWindow.setTabOrder(self.usrname, self.sign_usrname)
        MainWindow.setTabOrder(self.sign_usrname, self.sign_pwd)
        MainWindow.setTabOrder(self.sign_pwd, self.conf_pwd)
        MainWindow.setTabOrder(self.conf_pwd, self.noIdea)
        MainWindow.setTabOrder(self.noIdea, self.Signup)
        MainWindow.setTabOrder(self.Signup, self.name)
        MainWindow.setTabOrder(self.name, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.sine_volt)
        MainWindow.setTabOrder(self.sine_volt, self.var_volt)
        MainWindow.setTabOrder(self.var_volt, self.voltageValue_2)
        MainWindow.setTabOrder(self.voltageValue_2, self.duration_2)
        MainWindow.setTabOrder(self.duration_2, self.voltageValue_3)
        MainWindow.setTabOrder(self.voltageValue_3, self.duration_3)
        MainWindow.setTabOrder(self.duration_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.arduino_start)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#4988af;\">LOGIN</span></p></body></html>", None))
        self.usrname.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.pwd.setPlaceholderText(_translate("MainWindow", "Password", "efeswf"))
        self.Login.setText(_translate("MainWindow", "LOGIN", None))
        self.goToSignup.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Create a new account!</span></a></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Forgot Password?</span></a></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#4988af;\">SIGN UP</span></p></body></html>", None))
        self.name.setPlaceholderText(_translate("MainWindow", "Name", None))
        self.sign_usrname.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.sign_pwd.setPlaceholderText(_translate("MainWindow", "Password", "efeswf"))
        self.conf_pwd.setPlaceholderText(_translate("MainWindow", "Confirm Password", None))
        self.noIdea.setPlaceholderText(_translate("MainWindow", "e-Mail", None))
        self.Signup.setText(_translate("MainWindow", "SIGN UP", None))
        self.goToLogin.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Already a user? Sign in!</span></a></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Voltage Specification", None))
        self.const_volt.setText(_translate("MainWindow", "Constant Value", None))
        self.sine_volt.setText(_translate("MainWindow", "Sine Wave", None))
        self.var_volt.setText(_translate("MainWindow", "Variable Voltage", None))
        self.label_17.setText(_translate("MainWindow", "Value : ", None))
        self.voltageValue_2.setPlaceholderText(_translate("MainWindow", "in Volts", None))
        self.label_18.setText(_translate("MainWindow", "Duration of Experiment : ", None))
        self.duration_2.setPlaceholderText(_translate("MainWindow", "in Seconds", None))
        self.toggle_led0.setText(_translate("MainWindow", "Use LED", None))
        self.label_42.setText(_translate("MainWindow", "Compliance : ", None))
        self.label_43.setText(_translate("MainWindow", "Voltage Range : ", None))
        self.label_44.setText(_translate("MainWindow", "Resistance Range : ", None))
        self.var_start_3.setText(_translate("MainWindow", "START", None))
        self.addopt0.setText(_translate("MainWindow", "Additional Options", None))
        self.label_35.setText(_translate("MainWindow", "Initial Phase : ", None))
        self.sine_amp.setPlaceholderText(_translate("MainWindow", "in Volts", None))
        self.sine_phase.setPlaceholderText(_translate("MainWindow", "in Degrees", None))
        self.sine_duration.setPlaceholderText(_translate("MainWindow", "in Seconds", None))
        self.label_39.setText(_translate("MainWindow", "Frequency : ", None))
        self.sine_frequency.setPlaceholderText(_translate("MainWindow", "in Hertz", None))
        self.toggle_led1.setText(_translate("MainWindow", "Use LED", None))
        self.addopt1.setText(_translate("MainWindow", "Additional Options", None))
        self.label_45.setText(_translate("MainWindow", "Compliance : ", None))
        self.label_46.setText(_translate("MainWindow", "Voltage Range : ", None))
        self.label_47.setText(_translate("MainWindow", "Resistance Range : ", None))
        self.var_start_4.setText(_translate("MainWindow", "START", None))
        self.label_19.setText(_translate("MainWindow", "Start Value : ", None))
        self.voltageValue_3.setPlaceholderText(_translate("MainWindow", "in Volts", None))
        self.label_20.setText(_translate("MainWindow", "End Value : ", None))
        self.duration_3.setPlaceholderText(_translate("MainWindow", "in Volts", None))
        self.label_21.setText(_translate("MainWindow", "Number of Steps : ", None))
        self.toggle_led2.setText(_translate("MainWindow", "Use LED", None))
        self.addopt2.setText(_translate("MainWindow", "Additional Options", None))
        self.label_36.setText(_translate("MainWindow", "Compliance : ", None))
        self.label_37.setText(_translate("MainWindow", "Voltage Range : ", None))
        self.label_38.setText(_translate("MainWindow", "Resistance Range : ", None))
        self.var_start.setText(_translate("MainWindow", "START", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sourcerer), _translate("MainWindow", "Sourcerer", None))
        item = self.valuesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.valuesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Voltage", None))
        item = self.valuesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Current", None))
        item = self.valuesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Resistance", None))
        self.export_2.setText(_translate("MainWindow", "Export Readings", None))
        self.plot_graph.setText(_translate("MainWindow", "Plot Graph", None))
        self.csv.setText(_translate("MainWindow", "Generate CSV", None))
        self.xAxis.setItemText(0, _translate("MainWindow", "Time", None))
        self.xAxis.setItemText(1, _translate("MainWindow", "Current", None))
        self.xAxis.setItemText(2, _translate("MainWindow", "Voltage", None))
        self.xAxis.setItemText(3, _translate("MainWindow", "Resistance", None))
        self.label_5.setText(_translate("MainWindow", "X-Axis : ", None))
        self.label_11.setText(_translate("MainWindow", "Background Color :", None))
        self.label_4.setText(_translate("MainWindow", "Y-Axis :", None))
        self.label_32.setText(_translate("MainWindow", "Y-Start : ", None))
        self.yAxis.setItemText(0, _translate("MainWindow", "Current", None))
        self.yAxis.setItemText(1, _translate("MainWindow", "Voltage", None))
        self.yAxis.setItemText(2, _translate("MainWindow", "Resistance", None))
        self.label_40.setText(_translate("MainWindow", "X-Start : ", None))
        self.label_8.setText(_translate("MainWindow", "Line Color :", None))
        self.label_41.setText(_translate("MainWindow", "X-End : ", None))
        self.label_33.setText(_translate("MainWindow", "Y-End : ", None))
        self.label_6.setText(_translate("MainWindow", "Title : ", None))
        self.dur_exp.setText(_translate("MainWindow", "Duration of Experiment : ", None))
        self.amplitude.setText(_translate("MainWindow", "Amplitude : ", None))

        self.radioButton.setText(_translate("MainWindow", "GRID", None))
        self.radioButton_2.setText(_translate("MainWindow", "NO GRID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Graph), _translate("MainWindow", "Graph", None))
        self.label_2.setText(_translate("MainWindow", "Duration : ", None))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "in Seconds", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "in Seconds", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "in Seconds", None))
        self.label_16.setText(_translate("MainWindow", "Off Time : ", None))
        self.label_15.setText(_translate("MainWindow", "On Time : ", None))
        self.arduino_start.setText(_translate("MainWindow", "START", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Arduino), _translate("MainWindow", "LED", None))
        self.arduino_start.clicked.connect(self.ard_start)

    def mailingpwd(self):
        cur = db.cursor()
        cur.execute("select userid,password,email from User where email = '" + str(self.ui.email.text()) + "'")
        row = cur.fetchone()
        try:
            mailing.send_mail("sourcererkeithley@gmail.com", str(self.ui.email.text()),row)
            self.showMessageBox(self.win, "Email send successfully", "Success")
            self.win.close()
        except:
            self.showMessageBox(self.win, "Email is not valid or \nthere is no internet connection", "Error")
            self.win.close()

    def forgetPassword(self,event):
        self.win = QtGui.QMainWindow()
        self.ui = forgotPassword.Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.win.show()
        self.ui.recover_pwd.clicked.connect(self.mailingpwd)

    def ard_start(self):
        ontime = int( self.lineEdit.text() )
        offtime = int( self.lineEdit_2.text() )
        duration = int( self.lineEdit_4.text() )*60
        arduino.ard(ontime,offtime,duration)

    def setSignupWindow(self,event):
        self.stackedWidget.setCurrentIndex(1)

    def setLoginWindow(self,event):
        self.stackedWidget.setCurrentIndex(0)

    def color_picker(self,b):
        if b==0:
            self.lcolor = QtGui.QColorDialog.getColor()
            self.lcolor = self.lcolor.name()
            self.lineColor.setStyleSheet("QWidget { background-color: %s}" % self.lcolor)
        else:
            self.bcolor = QtGui.QColorDialog.getColor()
            self.bcolor = self.bcolor.name()
            self.bgColor.setStyleSheet("QWidget { background-color: %s}" % self.bcolor)

    def loginClicked(self):
        userid = self.usrname.text()
        password = self.pwd.text()
        cursor = db.cursor()
        stri = "select * from User where userid = \'" + str(userid) + "\' and password = \'" + str(password) + "\'"
        cursor.execute(stri)
        if cursor.fetchone() is not None:
             self.showMessageBox(MainWindow, "Congrats \n You are Logged In", "Successful Login")
             self.stackedWidget.setCurrentIndex(2)
        else:
             self.showMessageBox(MainWindow, "Please check your userid and password", "Login Error!")


    def submitClicked(self):
        name = str(self.name.text()).strip()
        email = str(self.noIdea.text()).strip()
        userid = str(self.sign_usrname.text()).strip()
        password = str(self.sign_pwd.text()).strip()
        cpassword = str(self.conf_pwd.text()).strip()
        if name == "" or email == "" or userid == "" or password == "":
            self.showMessageBox(MainWindow,"Please fill all the fields","Register Error!")
        else:
            cursor = db.cursor()
            cursor.execute("select * from User where userid=\"" + userid + "\"")
            if cursor.fetchone() is not None:
                self.showMessageBox(MainWindow,"Choose another userid","Register Error!")
            else:
                if password != cpassword:
                    self.showMessageBox(MainWindow,"Passwords do not match","Register Error!")
                else:
                    cursor = db.cursor()
                    try:
                        value = "INSERT INTO User(userid,name,password,email) " \
                                "VALUES(?,?,?,?)"
                        args = (userid, name, password, email)
                        cursor.execute(value, args)
                        db.commit()
                        self.showMessageBox(MainWindow,"Congrats \n You are successfully registered","Registration Successful")
                        self.stackedWidget.setCurrentIndex(2)
                    except Exception as e:
                        print(e)
                        db.rollback()


    def startExperiment(self):
        volt = self.voltageValue_2.text()
        tm = self.duration_2.text()
        self.valuesTable.setRowCount(0)
        a,b,c = 0.5,20,1000
        try:
            a,b,c = float(self.compliance0.text()),float(self.voltrange0.text()),float(self.resrange0.text())
        except:
            a,b,c = 0.5,20,1000
        try:
            self.values,self.tim = send_constant.main(float(volt),float(tm),a,b,c)
            self.tabWidget.setCurrentIndex(1)
            for i in range(len(self.tim)):
                self.valuesTable.insertRow(self.valuesTable.rowCount())
                self.valuesTable.setItem(i, 0, QtGui.QTableWidgetItem(str(self.tim[i])))
                for j in range(3):
                    self.valuesTable.setItem(i,j+1,QtGui.QTableWidgetItem(str(self.values[i][j])))

        except:
            self.showMessageBox(MainWindow,"Values entered are in wrong format\nOr keithley is not working","Error!")

    def stepVoltage(self):
        start = self.voltageValue_3.text()
        end = self.duration_3.text()
        steps = self.lineEdit_3.text()
        self.valuesTable.setRowCount(0)
        a,b,c = 0.5,20,1000
        try:
            a,b,c = float(self.compliance0.text()),float(self.voltrange0.text()),float(self.resrange0.text())
        except:
            a,b,c = 0.5,20,1000
        try:
            self.values,self.tim = step_voltage.main(float(start),float(end),float(steps),a,b,c)
            self.tabWidget.setCurrentIndex(1)
            for i in range(len(self.tim)):
                self.valuesTable.insertRow(self.valuesTable.rowCount())
                self.valuesTable.setItem(i, 0, QtGui.QTableWidgetItem(str(self.tim[i])))
                for j in range(3):
                    self.valuesTable.setItem(i, j + 1, QtGui.QTableWidgetItem(str(self.values[i][j])))

        except:
            self.showMessageBox(MainWindow, "Values entered are in wrong format\nOr keithley is not working", "Error!")

    def exportReadings(self):

        self.win = QtGui.QMainWindow()
        self.ui = ExportGUI.Ui_Mail()
        self.ui.setupUi(self.win)
        self.win.show()
        self.ui.export_mail.clicked.connect(self.exporting)

    def exporting(self,path_to,filename_to):
        cur = db.cursor()
        r = self.usrname.text()
        if str(self.usrname.text()) == "":
            r = self.sign_usrname.text()
        cur.execute("select email from User where userid = '" + str(r) + "';")
        p = str(cur.fetchone()[0])
        print(p,str(self.ui.email.text()),path_to)
        try:
            export.export(p,str(self.ui.email.text()),str(self.ui.password.text()),path = path_to,filename = filename_to )

            self.showMessageBox(self.win,"Mail was successfully sent","Success")
            self.win.close()
        except:
            self.showMessageBox(self.win,"Please check your internet connection\n Enter correct values","Authentication Error!")

            self.win.close()


    def plotGraph(self):
        self.tabWidget.setCurrentIndex(1)

        y = str(self.yAxis.currentText())
        x = str(self.xAxis.currentText())
        b = self.tim
        label_x = "Time"
        volt, current, resistance = [], [], []
        a = []
        # if len(self.values) == 0 :
        for tup in self.values:
            volt.append(tup[0])
            current.append(tup[1])
            resistance.append(tup[2])

        if y == "Voltage":
            a = volt
            label_y = "Voltage"
        elif y == "Current":
            a = current
            label_y = "Current"
        else:
            a = resistance
            label_y = "Resistance"

        if x == "Voltage":
            b = volt
            label_x = "Voltage"
        elif x == "Current":
            b = current
            label_x = "Current"
        elif x == "Resistance":
            b = resistance
            label_x = "Resistance"
        grid = False
        if self.radioButton.isChecked() == True:
            grid = True
        plot.beauty_plot(b,a,label_x,label_y,self.bcolor,self.lcolor,grid)

    def radioButtonFun(self,b):

        if self.const_volt.isChecked() == True:
            self.voltage_input.setCurrentIndex(0)

        elif self.sine_volt.isChecked() == True:
            self.voltage_input.setCurrentIndex(1)

        elif self.var_volt.isChecked() == True:
            self.voltage_input.setCurrentIndex(2)

    def additionalOptions(self,b):
        if self.addopt0.isChecked() == True:
            self.options00.setVisible(True)
        else:
            self.options00.setVisible(False)
        if self.addopt1.isChecked() == True:
            self.options01.setVisible(True)
        else:
            self.options01.setVisible(False)
        if self.addopt2.isChecked() == True:
            self.options02.setVisible(True)
        else:
            self.options02.setVisible(False)

    def ledOptions(self,b):

        if b == 0:
            if self.toggle_led0.isChecked() == True:
                self.tabWidget.setTabEnabled(2,True)
                self.tabWidget.setCurrentIndex(2)
        elif b == 1:
            if self.toggle_led1.isChecked() == True:
                self.tabWidget.setTabEnabled(2, True)
                self.tabWidget.setCurrentIndex(2)

        else:
            if self.toggle_led2.isChecked() == True:
                self.tabWidget.setTabEnabled(2, True)
                self.tabWidget.setCurrentIndex(2)

    def file_save(self):
        import ntpath,os
        import download
        location = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save File')
        filename = ntpath.basename(location)
        parent = os.path.dirname(location)
        download.save(path = parent, file_name = filename,rows = self.values,time = self.tim)

    def file_open(self):
        import ntpath,os
        import download
        location = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Save File')
        filename = ntpath.basename(location)

        self.win = QtGui.QMainWindow()
        self.ui = ExportGUI.Ui_Mail()
        self.ui.setupUi(self.win)
        self.win.show()
        self.ui.export_mail.clicked.connect(lambda: self.exporting(location,filename))


    def showMessageBox(self,win,message,title):
        msg = QtGui.QMessageBox(win)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.exec_()



import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("SOURCERER")
    MainWindow.show()
    sys.exit(app.exec_())
