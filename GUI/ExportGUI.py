# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
#
# Created: Wed Apr  4 18:39:16 2018
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

class Ui_Mail(object):
    def setupUi(self, Mail):
        Mail.setObjectName(_fromUtf8("Mail"))
        Mail.resize(706, 508)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Mail.sizePolicy().hasHeightForWidth())
        Mail.setSizePolicy(sizePolicy)
        Mail.setStyleSheet(_fromUtf8("ToolTip\n"
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
"      border-radius: 10;\n"
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
"    width: 14px;\n"
"    height: 14px;\n"
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
"}"
"QLabel:focus{\n"
"    border: 0px;\n"
"}\n"
))
        self.centralwidget = QtGui.QWidget(Mail)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setFocus()
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/email.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(50, -1, 50, -1)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
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
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.password = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setWhatsThis(_fromUtf8(""))
        self.password.setAccessibleName(_fromUtf8(""))
        self.password.setStyleSheet(_fromUtf8("border-radius:5;padding-left:10px;\n"
"background-color: #f6f8ff;"))
        self.password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.password.setInputMask(_fromUtf8(""))
        self.password.setText(_fromUtf8(""))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password.setPlaceholderText(_fromUtf8("Password"))
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 4, 0, 1, 1)
        self.export_mail = QtGui.QPushButton(self.centralwidget)
        self.export_mail.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.export_mail.setFont(font)
        self.export_mail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_mail.setToolTip(_fromUtf8(""))
        self.export_mail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.export_mail.setStyleSheet(_fromUtf8("padding:5px;\n"
"border-radius:5;margin-top:10px;\n"
"background-color: #4988af;margin-bottom: 100px;"))
        self.export_mail.setFlat(False)
        self.export_mail.setObjectName(_fromUtf8("export_mail"))
        self.gridLayout.addWidget(self.export_mail, 5, 0, 1, 1)
        self.email = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstTitleL"))
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setStyleSheet(_fromUtf8("border-radius:5;padding-left:10px;\n"
"background-color: #f6f8ff;"))
        self.email.setText(_fromUtf8(""))
        self.email.setPlaceholderText("e-Mail")
        self.email.setObjectName(_fromUtf8("email"))
        self.gridLayout.addWidget(self.email, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        Mail.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Mail)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Mail.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Mail)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Mail.setStatusBar(self.statusbar)

        self.retranslateUi(Mail)
        QtCore.QMetaObject.connectSlotsByName(Mail)

    def retranslateUi(self, Mail):
        Mail.setWindowTitle(_translate("Mail", "MainWindow", None))
        self.label_7.setText(_translate("Mail", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#4988af;\">EXPORT</span></p></body></html>", None))
        self.export_mail.setText(_translate("Mail", "EMAIL", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Mail = QtGui.QMainWindow()
    ui = Ui_Mail()
    ui.setupUi(Mail)
    Mail.setWindowTitle("Export Readings")
    Mail.setFixedSize(Mail.width(),Mail.height())
    Mail.show()
    sys.exit(app.exec_())

