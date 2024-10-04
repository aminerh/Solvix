from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 745)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QDialog{\n"
"background-color: #808080;\n"
"color: #FFA500;\n"
"border: 1px solid #333333;}\n"

"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid RGB(243, 158, 78);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/SolvixIcon.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(243,158,78); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: RGB(243, 158, 78);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(229, 119, 16);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(243,158,78);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"       background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: white;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(229, 119, 16)     ;\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(243, 158, 78);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(243,158,78)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(229, 119, 16); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(243, 158, 78); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(229, 119, 16);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(229, 119, 16);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(243, 158, 78);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(229, 119, 16); border-st"
                        "yle: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: RGB(229, 119, 16); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(243,158,78); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(229, 119, 16); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(229, 119, 16);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(243, 158, 78);\n"
"	color: rg"
                        "b(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(243,158,78);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-c"
                        "olor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: RGB(243, 158, 78);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid RGB(243, 158, 78);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-"
                        "color: RGB(243, 158, 78);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(243,158,78);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(243,158,78);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid RGB(243, 158, 78);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(229, 119, 16);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(243,158,78);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: RGB(243, 158, 78);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color:rgb(243, 158, 78);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(243,158,78);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(243,158,78);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(243,158,78);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: RGB(243, 158, 78);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(229, 119, 16);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(243,158,78);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(229, 119, 16);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(243, 158, 78);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 900))
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_login = QPushButton(self.topMenu)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(0, 45))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_login.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")

        self.verticalLayout_8.addWidget(self.btn_login)

        self.pushButton_2 = QPushButton(self.topMenu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 45))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-truck.png)")

        self.verticalLayout_8.addWidget(self.pushButton_2)

        self.btn_surplus = QPushButton(self.topMenu)
        self.btn_surplus.setObjectName(u"btn_surplus")
        sizePolicy.setHeightForWidth(self.btn_surplus.sizePolicy().hasHeightForWidth())
        self.btn_surplus.setSizePolicy(sizePolicy)
        self.btn_surplus.setMinimumSize(QSize(0, 45))
        self.btn_surplus.setFont(font)
        self.btn_surplus.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_surplus.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_surplus.setStyleSheet("""
    QPushButton {
        background-image: url(:/icons/images/icons/cil-library-add.png);
    }
    QPushButton:pressed {
        background-image: url(:/icons/images/icons/cil-library-add.png);
    }
""")

        self.verticalLayout_8.addWidget(self.btn_surplus)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.UserInfo = QLabel(self.leftBox)
        self.UserInfo.setObjectName(u"UserInfo")
        self.UserInfo.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.UserInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.horizontalLayout_7 = QHBoxLayout(self.login)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.login)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.logo_login = QLabel(self.frame)
        self.logo_login.setObjectName(u"logo_login")
        self.logo_login.setMinimumSize(QSize(300, 330))
        self.logo_login.setMaximumSize(QSize(500, 900))
        self.logo_login.setStyleSheet(u"background :url(:/images/images/images/Solvix.png) no-repeat center;\n"
"background-size: cover;")

        self.gridLayout_3.addWidget(self.logo_login, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.username = QLineEdit(self.frame)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(350, 30))
        self.username.setMaximumSize(QSize(120, 16777215))
        self.username.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.username, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(350, 30))
        self.password.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.password, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.login_button = QPushButton(self.frame)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(150, 40))
        self.login_button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-lock-unlocked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.login_button.setIcon(icon4)

        self.gridLayout_3.addWidget(self.login_button, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.frame)

        self.stackedWidget.addWidget(self.login)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        self.home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.home.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.home)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.home_header = QFrame(self.home)
        self.home_header.setObjectName(u"home_header")
        self.home_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.home_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.home_header)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.refresh = QPushButton(self.home_header)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setMinimumSize(QSize(150, 30))
        self.refresh.setFont(font)
        self.refresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refresh.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh.setIcon(icon5)

        self.horizontalLayout_6.addWidget(self.refresh, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_21.addWidget(self.home_header)

        self.PickAnomalies = QTableWidget(self.home)
        self.PickAnomalies.setObjectName(u"PickAnomalies")

        self.verticalLayout_21.addWidget(self.PickAnomalies)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon6)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 352, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon7)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.surplus = QWidget()
        self.surplus.setObjectName(u"surplus")
        self.surplus.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_20 = QVBoxLayout(self.surplus)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_3 = QFrame(self.surplus)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 40px; /* Adjust as needed */\n"
"font-weight: bold;\n"
"letter-spacing: 2px; /* Spacing between letters */\n"
"text-transform: uppercase; /* All caps */\n"
"font-family: 'Arial', sans-serif;\n"
"color: #ff6600;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_20.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.surplus)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Asin = QLineEdit(self.frame_2)
        self.Asin.setObjectName(u"Asin")
        self.Asin.setMinimumSize(QSize(350, 30))
        self.Asin.setMaximumSize(QSize(120, 16777215))
        self.Asin.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.Asin, 0, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Mission = QLineEdit(self.frame_2)
        self.Mission.setObjectName(u"Mission")
        self.Mission.setMinimumSize(QSize(350, 30))
        self.Mission.setMaximumSize(QSize(120, 16777215))
        self.Mission.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.Mission, 2, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.hospital_emp = QComboBox(self.frame_2)
        self.hospital_emp.setEditable(True)

        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("") 
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")
        self.hospital_emp.addItem("")

# /*********************************
        self.hospital_emp.setObjectName(u"hospital_emp")
        self.hospital_emp.setMinimumSize(QSize(350, 30))
        self.hospital_emp.setMaximumSize(QSize(120, 16777215))
        self.hospital_emp.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.hospital_emp, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Emp_initial = QLineEdit(self.frame_2)
        self.Emp_initial.setObjectName(u"Emp_initial")
        self.Emp_initial.setMinimumSize(QSize(350, 30))
        self.Emp_initial.setMaximumSize(QSize(120, 16777215))
        self.Emp_initial.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.Emp_initial, 3, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.picking_user = QLineEdit(self.frame_2)
        self.picking_user.setObjectName(u"picking_user")
        self.picking_user.setMinimumSize(QSize(350, 30))
        self.picking_user.setMaximumSize(QSize(120, 16777215))
        self.picking_user.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.picking_user, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.quantite = QLineEdit(self.frame_2)
        self.quantite.setObjectName(u"quantite")
        self.quantite.setMinimumSize(QSize(350, 30))
        self.quantite.setMaximumSize(QSize(120, 16777215))
        self.quantite.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.quantite, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_20.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.surplus)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.new_surplus = QPushButton(self.frame_4)
        self.new_surplus.setObjectName(u"new_surplus")
        self.new_surplus.setMinimumSize(QSize(150, 40))
        self.new_surplus.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_surplus.setIcon(icon8)

        self.verticalLayout_9.addWidget(self.new_surplus, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_20.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.surplus)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"SOLVIX", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"By Solvix Team", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Hopital", None))
        self.btn_surplus.setText(QCoreApplication.translate("MainWindow", u"Surplus", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Solvix", None))
        self.UserInfo.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.logo_login.setText("")
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R520", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mot de passe", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.refresh.setText(QCoreApplication.translate("MainWindow", u"Rafra\u00eechir", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Ajouter un nouveau Surplus", None))
        self.Asin.setText("")
        self.Asin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ASIN", None))
        self.Mission.setText("")
        self.Mission.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mission", None))

        self.hospital_emp.setItemText(0, QCoreApplication.translate("MainWindow", u"HOPI.001 00 A", None))
        self.hospital_emp.setItemText(1, QCoreApplication.translate("MainWindow", u"HOPI.001 00 B", None))
        self.hospital_emp.setItemText(2, QCoreApplication.translate("MainWindow", u"HOPI.001 00 C", None))
        self.hospital_emp.setItemText(3, QCoreApplication.translate("MainWindow", u"HOPI.001 00 D", None))
        self.hospital_emp.setItemText(4, QCoreApplication.translate("MainWindow", u"HOPI.001 05 A", None))
        self.hospital_emp.setItemText(5, QCoreApplication.translate("MainWindow", u"HOPI.001 05 B", None))
        self.hospital_emp.setItemText(6, QCoreApplication.translate("MainWindow", u"HOPI.001 05 C", None))
        self.hospital_emp.setItemText(7, QCoreApplication.translate("MainWindow", u"HOPI.001 05 D", None))
        self.hospital_emp.setItemText(8, QCoreApplication.translate("MainWindow", u"HOPI.001 10 A", None))
        self.hospital_emp.setItemText(9, QCoreApplication.translate("MainWindow", u"HOPI.001 10 B", None))
        self.hospital_emp.setItemText(10, QCoreApplication.translate("MainWindow", u"HOPI.001 10 C", None))
        self.hospital_emp.setItemText(11, QCoreApplication.translate("MainWindow", u"HOPI.001 10 D", None))
        self.hospital_emp.setItemText(12, QCoreApplication.translate("MainWindow", u"HOPI.001 15 A", None))
        self.hospital_emp.setItemText(13, QCoreApplication.translate("MainWindow", u"HOPI.001 15 B", None))
        self.hospital_emp.setItemText(14, QCoreApplication.translate("MainWindow", u"HOPI.001 15 C", None))
        self.hospital_emp.setItemText(15, QCoreApplication.translate("MainWindow", u"HOPI.001 15 D", None))
        self.hospital_emp.setItemText(16, QCoreApplication.translate("MainWindow", u"HOPI.001 20 A", None))
        self.hospital_emp.setItemText(17, QCoreApplication.translate("MainWindow", u"HOPI.001 20 B", None))
        self.hospital_emp.setItemText(18, QCoreApplication.translate("MainWindow", u"HOPI.001 20 C", None))
        self.hospital_emp.setItemText(19, QCoreApplication.translate("MainWindow", u"HOPI.001 20 D", None))
        self.hospital_emp.setItemText(20, QCoreApplication.translate("MainWindow", u"HOPI.001 25 A", None))
        self.hospital_emp.setItemText(21, QCoreApplication.translate("MainWindow", u"HOPI.001 25 B", None))
        self.hospital_emp.setItemText(22, QCoreApplication.translate("MainWindow", u"HOPI.001 25 C", None))
        self.hospital_emp.setItemText(23, QCoreApplication.translate("MainWindow", u"HOPI.001 25 D", None))
        self.hospital_emp.setItemText(24, QCoreApplication.translate("MainWindow", u"HOPI.001 30 A", None))
        self.hospital_emp.setItemText(25, QCoreApplication.translate("MainWindow", u"HOPI.001 30 B", None))
        self.hospital_emp.setItemText(26, QCoreApplication.translate("MainWindow", u"HOPI.001 30 C", None))
        self.hospital_emp.setItemText(27, QCoreApplication.translate("MainWindow", u"HOPI.001 30 D", None))
        self.hospital_emp.setItemText(28, QCoreApplication.translate("MainWindow", u"HOPI.001 35 A", None))
        self.hospital_emp.setItemText(29, QCoreApplication.translate("MainWindow", u"HOPI.001 35 B", None))
        self.hospital_emp.setItemText(30, QCoreApplication.translate("MainWindow", u"HOPI.001 35 C", None))
        self.hospital_emp.setItemText(31, QCoreApplication.translate("MainWindow", u"HOPI.001 35 D", None))
        self.hospital_emp.setItemText(32, QCoreApplication.translate("MainWindow", u"HOPI.002 30 A", None))
        self.hospital_emp.setItemText(33, QCoreApplication.translate("MainWindow", u"HOPI.002 30 B", None))
        self.hospital_emp.setItemText(34, QCoreApplication.translate("MainWindow", u"HOPI.002 30 C", None))
        self.hospital_emp.setItemText(35, QCoreApplication.translate("MainWindow", u"HOPI.002 30 D", None))
        self.hospital_emp.setItemText(36, QCoreApplication.translate("MainWindow", u"HOPI.002 35 A", None))
        self.hospital_emp.setItemText(37, QCoreApplication.translate("MainWindow", u"HOPI.002 35 B", None))
        self.hospital_emp.setItemText(38, QCoreApplication.translate("MainWindow", u"HOPI.002 35 C", None))
        self.hospital_emp.setItemText(39, QCoreApplication.translate("MainWindow", u"HOPI.002 35 D", None))
        self.hospital_emp.setItemText(40, QCoreApplication.translate("MainWindow", u"HOPI.003 30 A", None))
        self.hospital_emp.setItemText(41, QCoreApplication.translate("MainWindow", u"HOPI.003 30 B", None))
        self.hospital_emp.setItemText(42, QCoreApplication.translate("MainWindow", u"HOPI.003 30 C", None))
        self.hospital_emp.setItemText(43, QCoreApplication.translate("MainWindow", u"HOPI.003 30 D", None))
        self.hospital_emp.setItemText(44, QCoreApplication.translate("MainWindow", u"HOPI.003 35 A", None))
        self.hospital_emp.setItemText(45, QCoreApplication.translate("MainWindow", u"HOPI.003 35 B", None))
        self.hospital_emp.setItemText(46, QCoreApplication.translate("MainWindow", u"HOPI.003 35 C", None))
        self.hospital_emp.setItemText(47, QCoreApplication.translate("MainWindow", u"HOPI.003 35 D", None))
        self.hospital_emp.setItemText(48, QCoreApplication.translate("MainWindow", u"HOPI.001 40 A", None))
        self.hospital_emp.setItemText(49, QCoreApplication.translate("MainWindow", u"HOPI.001 40 B", None))
        self.hospital_emp.setItemText(50, QCoreApplication.translate("MainWindow", u"HOPI.001 40 C", None))
        self.hospital_emp.setItemText(51, QCoreApplication.translate("MainWindow", u"HOPI.001 40 D", None))
        self.hospital_emp.setItemText(52, QCoreApplication.translate("MainWindow", u"HOPI.001 45 A", None))
        self.hospital_emp.setItemText(53, QCoreApplication.translate("MainWindow", u"HOPI.001 45 B", None))
        self.hospital_emp.setItemText(54, QCoreApplication.translate("MainWindow", u"HOPI.001 45 C", None))
        self.hospital_emp.setItemText(55, QCoreApplication.translate("MainWindow", u"HOPI.001 45 D", None))
        self.hospital_emp.setItemText(56, QCoreApplication.translate("MainWindow", u"HOPI.002 00 A", None))
        self.hospital_emp.setItemText(57, QCoreApplication.translate("MainWindow", u"HOPI.002 00 B", None))
        self.hospital_emp.setItemText(58, QCoreApplication.translate("MainWindow", u"HOPI.002 00 C", None))
        self.hospital_emp.setItemText(59, QCoreApplication.translate("MainWindow", u"HOPI.002 00 D", None))
        self.hospital_emp.setItemText(60, QCoreApplication.translate("MainWindow", u"HOPI.002 05 A", None))
        self.hospital_emp.setItemText(61, QCoreApplication.translate("MainWindow", u"HOPI.002 05 B", None))
        self.hospital_emp.setItemText(62, QCoreApplication.translate("MainWindow", u"HOPI.002 05 C", None))
        self.hospital_emp.setItemText(63, QCoreApplication.translate("MainWindow", u"HOPI.002 05 D", None))
        self.hospital_emp.setItemText(64, QCoreApplication.translate("MainWindow", u"HOPI.002 10 A", None))
        self.hospital_emp.setItemText(65, QCoreApplication.translate("MainWindow", u"HOPI.002 10 B", None))
        self.hospital_emp.setItemText(66, QCoreApplication.translate("MainWindow", u"HOPI.002 10 C", None))
        self.hospital_emp.setItemText(67, QCoreApplication.translate("MainWindow", u"HOPI.002 10 D", None))
        self.hospital_emp.setItemText(68, QCoreApplication.translate("MainWindow", u"HOPI.002 15 A", None))
        self.hospital_emp.setItemText(69, QCoreApplication.translate("MainWindow", u"HOPI.002 15 B", None))
        self.hospital_emp.setItemText(70, QCoreApplication.translate("MainWindow", u"HOPI.002 15 C", None))
        self.hospital_emp.setItemText(71, QCoreApplication.translate("MainWindow", u"HOPI.002 15 D", None))
        self.hospital_emp.setItemText(72, QCoreApplication.translate("MainWindow", u"HOPI.002 20 A", None))
        self.hospital_emp.setItemText(73, QCoreApplication.translate("MainWindow", u"HOPI.002 20 B", None))
        self.hospital_emp.setItemText(74, QCoreApplication.translate("MainWindow", u"HOPI.002 20 C", None))
        self.hospital_emp.setItemText(75, QCoreApplication.translate("MainWindow", u"HOPI.002 20 D", None))
        self.hospital_emp.setItemText(76, QCoreApplication.translate("MainWindow", u"HOPI.002 25 A", None))
        self.hospital_emp.setItemText(77, QCoreApplication.translate("MainWindow", u"HOPI.002 25 B", None))
        self.hospital_emp.setItemText(78, QCoreApplication.translate("MainWindow", u"HOPI.002 25 C", None))
        self.hospital_emp.setItemText(79, QCoreApplication.translate("MainWindow", u"HOPI.002 25 D", None))
        self.hospital_emp.setItemText(80, QCoreApplication.translate("MainWindow", u"HOPI.002 40 A", None))
        self.hospital_emp.setItemText(81, QCoreApplication.translate("MainWindow", u"HOPI.002 40 B", None))
        self.hospital_emp.setItemText(82, QCoreApplication.translate("MainWindow", u"HOPI.002 40 C", None))
        self.hospital_emp.setItemText(83, QCoreApplication.translate("MainWindow", u"HOPI.002 40 D", None))
        self.hospital_emp.setItemText(84, QCoreApplication.translate("MainWindow", u"HOPI.002 45 A", None))
        self.hospital_emp.setItemText(85, QCoreApplication.translate("MainWindow", u"HOPI.002 45 B", None))
        self.hospital_emp.setItemText(86, QCoreApplication.translate("MainWindow", u"HOPI.002 45 C", None))
        self.hospital_emp.setItemText(87, QCoreApplication.translate("MainWindow", u"HOPI.002 45 D", None))
        self.hospital_emp.setItemText(88, QCoreApplication.translate("MainWindow", u"HOPI.003 00 A", None))
        self.hospital_emp.setItemText(89, QCoreApplication.translate("MainWindow", u"HOPI.003 00 B", None))
        self.hospital_emp.setItemText(90, QCoreApplication.translate("MainWindow", u"HOPI.003 00 C", None))
        self.hospital_emp.setItemText(91, QCoreApplication.translate("MainWindow", u"HOPI.003 00 D", None))
        self.hospital_emp.setItemText(92, QCoreApplication.translate("MainWindow", u"HOPI.003 05 A", None))
        self.hospital_emp.setItemText(93, QCoreApplication.translate("MainWindow", u"HOPI.003 05 B", None))
        self.hospital_emp.setItemText(94, QCoreApplication.translate("MainWindow", u"HOPI.003 05 C", None))
        self.hospital_emp.setItemText(95, QCoreApplication.translate("MainWindow", u"HOPI.003 05 D", None))
        self.hospital_emp.setItemText(96, QCoreApplication.translate("MainWindow", u"HOPI.003 10 A", None))
        self.hospital_emp.setItemText(97, QCoreApplication.translate("MainWindow", u"HOPI.003 10 B", None))
        self.hospital_emp.setItemText(98, QCoreApplication.translate("MainWindow", u"HOPI.003 10 C", None))
        self.hospital_emp.setItemText(99, QCoreApplication.translate("MainWindow", u"HOPI.003 10 D", None))
        self.hospital_emp.setItemText(100, QCoreApplication.translate("MainWindow", u"HOPI.003 15 A", None))
        self.hospital_emp.setItemText(101, QCoreApplication.translate("MainWindow", u"HOPI.003 15 B", None))
        self.hospital_emp.setItemText(102, QCoreApplication.translate("MainWindow", u"HOPI.003 15 C", None))
        self.hospital_emp.setItemText(103, QCoreApplication.translate("MainWindow", u"HOPI.003 15 D", None))
        self.hospital_emp.setItemText(104, QCoreApplication.translate("MainWindow", u"HOPI.003 20 A", None))
        self.hospital_emp.setItemText(105, QCoreApplication.translate("MainWindow", u"HOPI.003 20 B", None))
        self.hospital_emp.setItemText(106, QCoreApplication.translate("MainWindow", u"HOPI.003 20 C", None))
        self.hospital_emp.setItemText(107, QCoreApplication.translate("MainWindow", u"HOPI.003 20 D", None))
        self.hospital_emp.setItemText(108, QCoreApplication.translate("MainWindow", u"HOPI.003 25 A", None))
        self.hospital_emp.setItemText(109, QCoreApplication.translate("MainWindow", u"HOPI.003 25 B", None))
        self.hospital_emp.setItemText(110, QCoreApplication.translate("MainWindow", u"HOPI.003 25 C", None))
        self.hospital_emp.setItemText(111, QCoreApplication.translate("MainWindow", u"HOPI.003 25 D", None))
        self.hospital_emp.setItemText(112, QCoreApplication.translate("MainWindow", u"HOPI.003 40 A", None))
        self.hospital_emp.setItemText(113, QCoreApplication.translate("MainWindow", u"HOPI.003 40 B", None))
        self.hospital_emp.setItemText(114, QCoreApplication.translate("MainWindow", u"HOPI.003 40 C", None))
        self.hospital_emp.setItemText(115, QCoreApplication.translate("MainWindow", u"HOPI.003 40 D", None))
        self.hospital_emp.setItemText(116, QCoreApplication.translate("MainWindow", u"HOPI.003 45 A", None))
        self.hospital_emp.setItemText(117, QCoreApplication.translate("MainWindow", u"HOPI.003 45 B", None))
        self.hospital_emp.setItemText(118, QCoreApplication.translate("MainWindow", u"HOPI.003 45 C", None))
        self.hospital_emp.setItemText(119, QCoreApplication.translate("MainWindow", u"HOPI.003 45 D", None))
        self.hospital_emp.setItemText(120, QCoreApplication.translate("MainWindow", u"HOPI.004 00 A", None))
        self.hospital_emp.setItemText(121, QCoreApplication.translate("MainWindow", u"HOPI.004 00 B", None))
        self.hospital_emp.setItemText(122, QCoreApplication.translate("MainWindow", u"HOPI.004 00 C", None))
        self.hospital_emp.setItemText(123, QCoreApplication.translate("MainWindow", u"HOPI.004 00 D", None))
        self.hospital_emp.setItemText(124, QCoreApplication.translate("MainWindow", u"HOPI.004 05 A", None))
        self.hospital_emp.setItemText(125, QCoreApplication.translate("MainWindow", u"HOPI.004 05 B", None))
        self.hospital_emp.setItemText(126, QCoreApplication.translate("MainWindow", u"HOPI.004 05 C", None))
        self.hospital_emp.setItemText(127, QCoreApplication.translate("MainWindow", u"HOPI.004 05 D", None))
        self.hospital_emp.setItemText(128, QCoreApplication.translate("MainWindow", u"HOPI.004 10 A", None))
        self.hospital_emp.setItemText(129, QCoreApplication.translate("MainWindow", u"HOPI.004 10 B", None))
        self.hospital_emp.setItemText(130, QCoreApplication.translate("MainWindow", u"HOPI.004 10 C", None))
        self.hospital_emp.setItemText(131, QCoreApplication.translate("MainWindow", u"HOPI.004 10 D", None))
        self.hospital_emp.setItemText(132, QCoreApplication.translate("MainWindow", u"HOPI.004 15 A", None))
        self.hospital_emp.setItemText(133, QCoreApplication.translate("MainWindow", u"HOPI.004 15 B", None))
        self.hospital_emp.setItemText(134, QCoreApplication.translate("MainWindow", u"HOPI.004 15 C", None))
        self.hospital_emp.setItemText(135, QCoreApplication.translate("MainWindow", u"HOPI.004 15 D", None))
        self.hospital_emp.setItemText(136, QCoreApplication.translate("MainWindow", u"HOPI.004 20 A", None))
        self.hospital_emp.setItemText(137, QCoreApplication.translate("MainWindow", u"HOPI.004 20 B", None))
        self.hospital_emp.setItemText(138, QCoreApplication.translate("MainWindow", u"HOPI.004 20 C", None))
        self.hospital_emp.setItemText(139, QCoreApplication.translate("MainWindow", u"HOPI.004 20 D", None))
        self.hospital_emp.setItemText(140, QCoreApplication.translate("MainWindow", u"HOPI.004 25 A", None))
        self.hospital_emp.setItemText(141, QCoreApplication.translate("MainWindow", u"HOPI.004 25 B", None))
        self.hospital_emp.setItemText(142, QCoreApplication.translate("MainWindow", u"HOPI.004 25 C", None))
        self.hospital_emp.setItemText(143, QCoreApplication.translate("MainWindow", u"HOPI.004 25 D", None))
        self.hospital_emp.setItemText(144, QCoreApplication.translate("MainWindow", u"HOPI.004 40 A", None))
        self.hospital_emp.setItemText(145, QCoreApplication.translate("MainWindow", u"HOPI.004 40 B", None))
        self.hospital_emp.setItemText(146, QCoreApplication.translate("MainWindow", u"HOPI.004 40 C", None))
        self.hospital_emp.setItemText(147, QCoreApplication.translate("MainWindow", u"HOPI.004 40 D", None))
        self.hospital_emp.setItemText(148, QCoreApplication.translate("MainWindow", u"HOPI.004 45 A", None))
        self.hospital_emp.setItemText(149, QCoreApplication.translate("MainWindow", u"HOPI.004 45 B", None))
        self.hospital_emp.setItemText(150, QCoreApplication.translate("MainWindow", u"HOPI.004 45 C", None))
        self.hospital_emp.setItemText(151, QCoreApplication.translate("MainWindow", u"HOPI.004 45 D", None))

        self.hospital_emp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Emp Hospital", None))
        self.Emp_initial.setText("")
        self.Emp_initial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Emp inital ou Chemin picking", None))
        self.picking_user.setText("")
        self.picking_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Picking R520", None))
        self.quantite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9", None))
        self.new_surplus.setText(QCoreApplication.translate("MainWindow", u"Enregistrer ", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Solvix team", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

