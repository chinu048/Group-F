# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sandarbh/Desktop/Sourcerer/GUI/mainwindow.ui'
#
# Created: Sun Mar 25 06:11:07 2018
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
        MainWindow.resize(708, 750)
        MainWindow.setStyleSheet(_fromUtf8("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color:#f6f8ff;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
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
"    border: 1px solid #ffaa00;\n"
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
"        stop:0.1 #ffaa00*/\n"
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
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    color:#323232;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #4988af;\n"
"    border-radius:15;\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #f6f8ff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #4988af;\n"
"    border-style: solid;\n"
"    border-radius: 10;\n"
"    padding: 3px;\n"
"    font-size: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    width: 100px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
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
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
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
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
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
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
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
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
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
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
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
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"QMainWindow{\n"
"\n"
"    color:#f6f8ff;\n"
"    margin: 0px;\n"
"}"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setStyleSheet(_fromUtf8("background-color:#f6f8ff"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralWidget)
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
        self.image.setStyleSheet(_fromUtf8("background-color:#4988af"))
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
        self.pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
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
        self.goToSignup.setToolTipDuration(-1)
        self.goToSignup.setObjectName(_fromUtf8("goToSignup"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.goToSignup)
        self.label_9 = QtGui.QLabel(self.login)
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
        self.image_signup.setStyleSheet(_fromUtf8("background-color:#4988af"))
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
        self.sign_pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
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
        self.goToLogin.setToolTipDuration(-1)
        self.goToLogin.setObjectName(_fromUtf8("goToLogin"))
        self.formLayout_6.setWidget(8, QtGui.QFormLayout.FieldRole, self.goToLogin)
        self.label_12 = QtGui.QLabel(self.signup)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_6.setWidget(10, QtGui.QFormLayout.FieldRole, self.label_12)
        self.horizontalLayout_2.addLayout(self.formLayout_6)
        self.stackedWidget.addWidget(self.signup)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 708, 20))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.image.setText(_translate("MainWindow", "TextLabel", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#4988af;\">LOGIN</span></p></body></html>", None))
        self.Login.setText(_translate("MainWindow", "LOGIN", None))
        self.goToSignup.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Create a new account!</span></a></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Forgot Password?</span></a></p></body></html>", None))
        self.image_signup.setText(_translate("MainWindow", "TextLabel", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#4988af;\">SIGN UP</span></p></body></html>", None))
        self.Signup.setText(_translate("MainWindow", "SIGN UP", None))
        self.goToLogin.setText(_translate("MainWindow", "<html><head/><body><p><a href=\\\"whatever\\\">\n"
"<span style=\" font-size:12pt; color:#4988af;text-decoration: none;\">Already a user? Sign in!</span></a></p></body></html>", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4988af;\">SOMETHING TO FILL IN!!!</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

