# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'decodeFixFilePanel.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_decodeFixFile(object):
    def setupUi(self, decodeFixFile):
        if not decodeFixFile.objectName():
            decodeFixFile.setObjectName(u"decodeFixFile")
        decodeFixFile.resize(1280, 720)
        self.tituloLabel = QLabel(decodeFixFile)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setGeometry(QRect(310, 30, 651, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_btn = QPushButton(decodeFixFile)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 81, 26))
        self.label = QLabel(decodeFixFile)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 120, 171, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label.setFont(font1)
        self.tableFile = QTableWidget(decodeFixFile)
        if (self.tableFile.columnCount() < 2):
            self.tableFile.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableFile.setObjectName(u"tableFile")
        self.tableFile.setGeometry(QRect(30, 140, 461, 481))
        self.desproteger_btn = QPushButton(decodeFixFile)
        self.desproteger_btn.setObjectName(u"desproteger_btn")
        self.desproteger_btn.setGeometry(QRect(120, 640, 281, 51))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.desproteger_btn.setFont(font2)
        self.textFileC = QTextEdit(decodeFixFile)
        self.textFileC.setObjectName(u"textFileC")
        self.textFileC.setGeometry(QRect(550, 400, 691, 221))
        self.textFileE = QTextEdit(decodeFixFile)
        self.textFileE.setObjectName(u"textFileE")
        self.textFileE.setGeometry(QRect(550, 140, 691, 221))
        self.label_2 = QLabel(decodeFixFile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(560, 120, 251, 21))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(decodeFixFile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(560, 380, 251, 21))
        self.label_3.setFont(font1)

        self.retranslateUi(decodeFixFile)

        QMetaObject.connectSlotsByName(decodeFixFile)
    # setupUi

    def retranslateUi(self, decodeFixFile):
        decodeFixFile.setWindowTitle(QCoreApplication.translate("decodeFixFile", u"Form", None))
        self.tituloLabel.setText(QCoreApplication.translate("decodeFixFile", u"Desproteger y corregir Archivo", None))
        self.back_btn.setText(QCoreApplication.translate("decodeFixFile", u"Volver", None))
        self.label.setText(QCoreApplication.translate("decodeFixFile", u"Seleccionar Archivo: ", None))
        ___qtablewidgetitem = self.tableFile.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("decodeFixFile", u"Archivo", None))
        ___qtablewidgetitem1 = self.tableFile.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("decodeFixFile", u"Tama\u00f1o", None))
        self.desproteger_btn.setText(QCoreApplication.translate("decodeFixFile", u"Desproteger y Corregir Archivo", None))
        self.label_2.setText(QCoreApplication.translate("decodeFixFile", u"Archivo desprotegido sin corregir:", None))
        self.label_3.setText(QCoreApplication.translate("decodeFixFile", u"Archivo desprotegido y corregido:", None))
    # retranslateUi

