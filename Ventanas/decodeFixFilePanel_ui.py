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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
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

        self.retranslateUi(decodeFixFile)

        QMetaObject.connectSlotsByName(decodeFixFile)
    # setupUi

    def retranslateUi(self, decodeFixFile):
        decodeFixFile.setWindowTitle(QCoreApplication.translate("decodeFixFile", u"Form", None))
        self.tituloLabel.setText(QCoreApplication.translate("decodeFixFile", u"Desproteger y corregir Archivo", None))
        self.back_btn.setText(QCoreApplication.translate("decodeFixFile", u"Volver", None))
    # retranslateUi

