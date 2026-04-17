# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addErrorPanel.ui'
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

class Ui_addError(object):
    def setupUi(self, addError):
        if not addError.objectName():
            addError.setObjectName(u"addError")
        addError.resize(1280, 720)
        self.back_btn = QPushButton(addError)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 81, 26))
        self.tituloLabel = QLabel(addError)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setGeometry(QRect(390, 30, 491, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(addError)

        QMetaObject.connectSlotsByName(addError)
    # setupUi

    def retranslateUi(self, addError):
        addError.setWindowTitle(QCoreApplication.translate("addError", u"Form", None))
        self.back_btn.setText(QCoreApplication.translate("addError", u"Volver", None))
        self.tituloLabel.setText(QCoreApplication.translate("addError", u"Insertar Error al Archivo", None))
    # retranslateUi

