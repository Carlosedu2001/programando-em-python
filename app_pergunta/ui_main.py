# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainSgjFFD.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 438)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(3, 213, 255, 255), stop:1 rgba(226, 250, 255, 255));\n"
"}\n"
"\n"
"QLabel#pergunta {\n"
"	font-size: 40px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLabel#resposta {\n"
"	font-size: 40px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 2px solid black;\n"
"	font-size: 20px;\n"
"	min-height: 45px;\n"
"	border-radius: 5;\n"
"	background-color: white;\n"
"	font-weight: bold;\n"
"}")
        self.pergunta = QLabel(self.centralwidget)
        self.pergunta.setObjectName(u"pergunta")
        self.pergunta.setGeometry(QRect(10, 20, 431, 91))
        self.pergunta.setAlignment(Qt.AlignCenter)
        self.frame_yes = QFrame(self.centralwidget)
        self.frame_yes.setObjectName(u"frame_yes")
        self.frame_yes.setGeometry(QRect(50, 200, 160, 90))
        self.frame_yes.setFrameShape(QFrame.NoFrame)
        self.frame_yes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_yes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.botton_yes = QPushButton(self.frame_yes)
        self.botton_yes.setObjectName(u"botton_yes")

        self.horizontalLayout.addWidget(self.botton_yes)

        self.frame_no = QFrame(self.centralwidget)
        self.frame_no.setObjectName(u"frame_no")
        self.frame_no.setGeometry(QRect(230, 200, 160, 90))
        self.frame_no.setFrameShape(QFrame.NoFrame)
        self.frame_no.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_no)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_no = QPushButton(self.frame_no)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout_2.addWidget(self.button_no)

        self.resposta = QLabel(self.centralwidget)
        self.resposta.setObjectName(u"resposta")
        self.resposta.setGeometry(QRect(10, 30, 431, 60))
        self.resposta.setAlignment(Qt.AlignCenter)
        self.risada = QLabel(self.centralwidget)
        self.risada.setObjectName(u"risada")
        self.risada.setGeometry(QRect(40, 110, 370, 300))
        self.risada.setPixmap(QPixmap(u":/images/tom_cruise_smiling.png"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pergunta.setText(QCoreApplication.translate("MainWindow", u"Voc\u00ea \u00e9 idiota?", None))
        self.botton_yes.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.button_no.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.resposta.setText(QCoreApplication.translate("MainWindow", u"HAHAHA EU SABIA", None))
        self.risada.setText("")
    # retranslateUi

