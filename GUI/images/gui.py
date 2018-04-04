# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sandarbh/Desktop/Sourcerer/GUI/mainwindow.ui'
#
# Created: Tue Apr  3 15:49:11 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1090, 871)
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
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #44cf6c, stop: 1 #ffa02f);\n"
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
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #44cf6c, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #44cf6c);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #44cf6c, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
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
"    /*border: 1px solid #b1b1b1;*/\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #44cf6c;\n"
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
"}"))
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
        self.pwd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pwd.setInputMask(_fromUtf8(""))
        self.pwd.setText(_fromUtf8(""))
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pwd.setPlaceholderText(_fromUtf8(""))
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
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.Login)
        self.goToSignup = QtGui.QLabel(self.login)
        self.goToSignup.setMouseTracking(True)
        self.goToSignup.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.goToSignup.setToolTipDuration(0)
        self.goToSignup.setObjectName(_fromUtf8("goToSignup"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.goToSignup)
        self.label_9 = QtGui.QLabel(self.login)
        self.label_9.setToolTipDuration(0)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_5.setWidget(7, QtGui.QFormLayout.FieldRole, self.label_9)
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
        self.sign_pwd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sign_pwd.setInputMask(_fromUtf8(""))
        self.sign_pwd.setText(_fromUtf8(""))
        self.sign_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.sign_pwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sign_pwd.setPlaceholderText(_fromUtf8(""))
        self.sign_pwd.setObjectName(_fromUtf8("sign_pwd"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.FieldRole, self.sign_pwd)
        self.conf_pwd = QtGui.QLineEdit(self.signup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.conf_pwd.setFont(font)
        self.conf_pwd.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.conf_pwd.setInputMethodHints(QtCore.Qt.ImhNone)
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
        self.formLayout_6.setWidget(7, QtGui.QFormLayout.FieldRole, self.Signup)
        self.goToLogin = QtGui.QLabel(self.signup)
        self.goToLogin.setMouseTracking(True)
        self.goToLogin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.goToLogin.setToolTipDuration(0)
        self.goToLogin.setObjectName(_fromUtf8("goToLogin"))
        self.formLayout_6.setWidget(8, QtGui.QFormLayout.FieldRole, self.goToLogin)
        self.label_12 = QtGui.QLabel(self.signup)
        self.label_12.setToolTipDuration(0)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_6.setWidget(10, QtGui.QFormLayout.FieldRole, self.label_12)
        self.name = QtGui.QLineEdit(self.signup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.name.setObjectName(_fromUtf8("name"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.name)
        self.horizontalLayout_2.addLayout(self.formLayout_6)
        self.stackedWidget.addWidget(self.signup)
        self.Main = QtGui.QWidget()
        self.Main.setStyleSheet(_fromUtf8("background-color:#f6f8ff"))
        self.Main.setObjectName(_fromUtf8("Main"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.Main)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tabWidget = QtGui.QTabWidget(self.Main)
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
        self.gridLayout = QtGui.QGridLayout(self.Sourcerer)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        self.verticalLayout.addWidget(self.const_volt)
        self.sine_volt = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        self.sine_volt.setFont(font)
        self.sine_volt.setStyleSheet(_fromUtf8("focus{\n"
"    border: 0px;\n"
"}"))
        self.sine_volt.setObjectName(_fromUtf8("sine_volt"))
        self.verticalLayout.addWidget(self.sine_volt)
        self.var_volt = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        self.var_volt.setFont(font)
        self.var_volt.setObjectName(_fromUtf8("var_volt"))
        self.verticalLayout.addWidget(self.var_volt)
        self.voltage_input = QtGui.QStackedWidget(self.groupBox)
        self.voltage_input.setObjectName(_fromUtf8("voltage_input"))
        self.cont_voltage = QtGui.QWidget()
        self.cont_voltage.setObjectName(_fromUtf8("cont_voltage"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.cont_voltage)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
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
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_18)
        self.duration_2 = QtGui.QLineEdit(self.cont_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.duration_2.setFont(font)
        self.duration_2.setStyleSheet(_fromUtf8("border-radius:15;padding-left:10px;"))
        self.duration_2.setObjectName(_fromUtf8("duration_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.duration_2)
        self.Start_2 = QtGui.QPushButton(self.cont_voltage)
        self.Start_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Start_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Start_2.setStyleSheet(_fromUtf8("padding:5px;\n"
"color: #f6f8ff;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.Start_2.setObjectName(_fromUtf8("Start_2"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.Start_2)
        self.checkBox = QtGui.QCheckBox(self.cont_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBox)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.voltage_input.addWidget(self.cont_voltage)
        self.variable_voltage = QtGui.QWidget()
        self.variable_voltage.setObjectName(_fromUtf8("variable_voltage"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.variable_voltage)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_3 = QtGui.QFormLayout()
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
        self.Start_3 = QtGui.QPushButton(self.variable_voltage)
        self.Start_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Start_3.setFont(font)
        self.Start_3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Start_3.setStyleSheet(_fromUtf8("padding:5px;\n"
"color: #f6f8ff;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.Start_3.setObjectName(_fromUtf8("Start_3"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.Start_3)
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
        self.checkBox_2 = QtGui.QCheckBox(self.variable_voltage)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox_2)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.voltage_input.addWidget(self.variable_voltage)
        self.verticalLayout.addWidget(self.voltage_input)
        self.gridLayout.addWidget(self.groupBox, 0, 2, 1, 3)
        self.pushButton_2 = QtGui.QPushButton(self.Sourcerer)
        self.pushButton_2.setStyleSheet(_fromUtf8("padding:5px;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.Sourcerer)
        self.pushButton_3.setStyleSheet(_fromUtf8("padding:5px;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 2, 4, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.Sourcerer)
        self.pushButton_4.setStyleSheet(_fromUtf8("padding:5px;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 2, 3, 1, 1)
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
        self.gridLayout.addWidget(self.image_main_1, 0, 0, 3, 2)
        self.valuesTable = QtGui.QTableWidget(self.Sourcerer)
        self.valuesTable.setStyleSheet(_fromUtf8("/*selection-background-color: #4988af;\n"
"alternate-background-color: #000000;*/\n"
"\n"
""))
        self.valuesTable.setRowCount(0)
        self.valuesTable.setObjectName(_fromUtf8("valuesTable"))
        self.valuesTable.setColumnCount(4)
        item = QtGui.QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.valuesTable.setHorizontalHeaderItem(3, item)
        self.valuesTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.valuesTable, 1, 2, 1, 3)
        self.tabWidget.addTab(self.Sourcerer, _fromUtf8(""))
        self.Graph = QtGui.QWidget()
        self.Graph.setObjectName(_fromUtf8("Graph"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Graph)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background-color: #4988af"))
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 4)
        self.label_5 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
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
        self.gridLayout_2.addWidget(self.xAxis, 0, 1, 1, 1)
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
        self.gridLayout_2.addWidget(self.yAxis, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineColor = QtGui.QPushButton(self.Graph)
        self.lineColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineColor.setFont(font)
        self.lineColor.setStyleSheet(_fromUtf8("border-radius: 5px;"))
        self.lineColor.setText(_fromUtf8(""))
        self.lineColor.setObjectName(_fromUtf8("lineColor"))
        self.gridLayout_2.addWidget(self.lineColor, 1, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.Graph)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.bgColor = QtGui.QPushButton(self.Graph)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.bgColor.setFont(font)
        self.bgColor.setStyleSheet(_fromUtf8("border-radius: 5px;"))
        self.bgColor.setText(_fromUtf8(""))
        self.bgColor.setObjectName(_fromUtf8("bgColor"))
        self.gridLayout_2.addWidget(self.bgColor, 1, 3, 1, 1)
        self.tabWidget.addTab(self.Graph, _fromUtf8(""))
        self.Arduino = QtGui.QWidget()
        self.Arduino.setObjectName(_fromUtf8("Arduino"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Arduino)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(428, 188, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 2, 3)
        spacerItem1 = QtGui.QSpacerItem(278, 628, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 5, 1)
        spacerItem2 = QtGui.QSpacerItem(358, 374, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 3, 4, 1)
        self.label_15 = QtGui.QLabel(self.Arduino)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("color: #292f36;"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 2, 1, 1, 1)
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
        self.lineEdit_2 = QtGui.QLineEdit(self.Arduino)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(_fromUtf8("margin: 10px;"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.Arduino)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setStyleSheet(_fromUtf8("margin: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 4, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(428, 252, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 5, 1, 1, 3)
        self.tabWidget.addTab(self.Arduino, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.Main)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1090, 20))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.voltage_input.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#4988af;\">LOGIN</span></p></body></html>", None))
        self.Login.setText(_translate("MainWindow", "LOGIN", None))
        self.goToSignup.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Create a new account!</span></a></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Forgot Password?</span></a></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#4988af;\">SIGN UP</span></p></body></html>", None))
        self.Signup.setText(_translate("MainWindow", "SIGN UP", None))
        self.goToLogin.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Already a user? Sign in!</span></a></p></body></html>", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4988af;\">SOMETHING TO FILL IN!!!</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Voltage Specification", None))
        self.const_volt.setText(_translate("MainWindow", "Constant Value", None))
        self.sine_volt.setText(_translate("MainWindow", "Sine Wave", None))
        self.var_volt.setText(_translate("MainWindow", "Variable Voltage", None))
        self.label_17.setText(_translate("MainWindow", "Value : ", None))
        self.label_18.setText(_translate("MainWindow", "Duration of Experiment : ", None))
        self.Start_2.setText(_translate("MainWindow", "START", None))
        self.checkBox.setText(_translate("MainWindow", "Use LED", None))
        self.label_19.setText(_translate("MainWindow", "Start Value : ", None))
        self.label_20.setText(_translate("MainWindow", "End Value : ", None))
        self.Start_3.setText(_translate("MainWindow", "START", None))
        self.label_21.setText(_translate("MainWindow", "Number of Steps : ", None))
        self.checkBox_2.setText(_translate("MainWindow", "Use LED", None))
        self.pushButton_2.setText(_translate("MainWindow", "Export Readings", None))
        self.pushButton_3.setText(_translate("MainWindow", "Plot Graph", None))
        self.pushButton_4.setText(_translate("MainWindow", "Generate CSV", None))
        item = self.valuesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.valuesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Voltage", None))
        item = self.valuesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Current", None))
        item = self.valuesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Resistance", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sourcerer), _translate("MainWindow", "Sourcerer", None))
        self.label_6.setText(_translate("MainWindow", "GRAPH WILL BE HERE", None))
        self.label_5.setText(_translate("MainWindow", "X-Axis : ", None))
        self.xAxis.setItemText(0, _translate("MainWindow", "Time", None))
        self.yAxis.setItemText(0, _translate("MainWindow", "Current", None))
        self.yAxis.setItemText(1, _translate("MainWindow", "Voltage", None))
        self.yAxis.setItemText(2, _translate("MainWindow", "Resistance", None))
        self.label_8.setText(_translate("MainWindow", "Line Color :", None))
        self.label_11.setText(_translate("MainWindow", "Background Color :", None))
        self.label_4.setText(_translate("MainWindow", "Y-Axis :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Graph), _translate("MainWindow", "Graph", None))
        self.label_15.setText(_translate("MainWindow", "Start Voltage : ", None))
        self.label_16.setText(_translate("MainWindow", "End Voltage : ", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Arduino), _translate("MainWindow", "Arduino", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

