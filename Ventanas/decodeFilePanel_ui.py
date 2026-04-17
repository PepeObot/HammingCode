# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'decodeFilePanel.ui'
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

class Ui_decodeFile(object):
    def setupUi(self, decodeFile):
        if not decodeFile.objectName():
            decodeFile.setObjectName(u"decodeFile")
        decodeFile.resize(1280, 720)
        self.tituloLabel = QLabel(decodeFile)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setGeometry(QRect(310, 40, 651, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_btn = QPushButton(decodeFile)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(20, 20, 81, 26))

        self.retranslateUi(decodeFile)

        QMetaObject.connectSlotsByName(decodeFile)
    # setupUi

    def retranslateUi(self, decodeFile):
        decodeFile.setWindowTitle(QCoreApplication.translate("decodeFile", u"Form", None))
        self.tituloLabel.setText(QCoreApplication.translate("decodeFile", u"Desproteger Archivo", None))
        self.back_btn.setText(QCoreApplication.translate("decodeFile", u"Volver", None))
    # retranslateUi

