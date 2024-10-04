# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginV2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"*{\n"
"	font-family:Century gothic;\n"
"	font-size:10px;\n"
"	font-weight: bold; \n"
"}\n"
"QPushButton{\n"
"	border-radius:15px;\n"
"	background:blue;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius:15px;\n"
"	background:#49ebff;\n"
"	color:#333;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(-110, -70, 1920, 1080))
        self.groupBox.setStyleSheet(u"\n"
"*{\n"
"	font-family:Century gothic;\n"
"	font-size:24px;\n"
"}\n"
"QFrame{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius:50px;\n"
"	background:blue;\n"
"}\n"
"QToolButton{\n"
"	border-radius:50px;\n"
"	background:blue;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background:transparent;\n"
"	border:none;\n"
"	color:#717072;\n"
"	border-bottom:1px solid #717072;\n"
"}\n"
"#groupBox{\n"
"background:url(:/images/bg.jpg);\n"
"}")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(670, 170, 671, 851))
        self.widget.setStyleSheet(u"background:#D3D3D3;\n"
"border-radius:25px;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 400, 151, 51))
        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(220, 720, 221, 51))
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	border-radius:25px;\n"
"	background:blue;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius:25px;\n"
"	background:#49ebff;\n"
"	color:#333;\n"
"}\n"
"\n"
"")
        self.username_input = QLineEdit(self.widget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(170, 520, 321, 31))
        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(180, 630, 321, 31))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.logo = QGraphicsView(self.widget)
        self.logo.setObjectName(u"graphicsView")
        self.logo.setGeometry(QRect(210, 20, 256, 361))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"S'IDENTIFIER", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Se Connecter", None))
        self.username_input.setText("")
        self.username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R520", None))
        self.password_input.setText("")
        self.password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de Passe", None))
    # retranslateUi

