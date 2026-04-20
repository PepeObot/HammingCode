# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'encodeFilePanel.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_encodeFile(object):
    def setupUi(self, encodeFile):
        if not encodeFile.objectName():
            encodeFile.setObjectName(u"encodeFile")
        encodeFile.resize(1280, 720)
        self.back_btn = QPushButton(encodeFile)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 81, 26))
        self.tituloLabel = QLabel(encodeFile)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setGeometry(QRect(450, 30, 371, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tableFile = QTableWidget(encodeFile)
        if (self.tableFile.columnCount() < 3):
            self.tableFile.setColumnCount(3)
        font1 = QFont()
        font1.setBold(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1)
        self.tableFile.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableFile.setObjectName(u"tableFile")
        self.tableFile.setGeometry(QRect(40, 140, 1201, 471))
        self.tableFile.horizontalHeader().setCascadingSectionResizes(False)
        self.tableFile.horizontalHeader().setDefaultSectionSize(400)
        self.tableFile.horizontalHeader().setHighlightSections(True)
        self.tableFile.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableFile.horizontalHeader().setStretchLastSection(True)
        self.tableFile.verticalHeader().setVisible(True)
        self.tableFile.verticalHeader().setCascadingSectionResizes(False)
        self.tableFile.verticalHeader().setHighlightSections(True)
        self.tableFile.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableFile.verticalHeader().setStretchLastSection(False)
        self.selectLabel = QLabel(encodeFile)
        self.selectLabel.setObjectName(u"selectLabel")
        self.selectLabel.setGeometry(QRect(60, 100, 301, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.selectLabel.setFont(font2)
        self.protegerFile_btn = QPushButton(encodeFile)
        self.protegerFile_btn.setObjectName(u"protegerFile_btn")
        self.protegerFile_btn.setGeometry(QRect(500, 630, 271, 51))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.protegerFile_btn.setFont(font3)

        self.retranslateUi(encodeFile)

        QMetaObject.connectSlotsByName(encodeFile)
    # setupUi

    def retranslateUi(self, encodeFile):
        encodeFile.setWindowTitle(QCoreApplication.translate("encodeFile", u"Form", None))
        self.back_btn.setText(QCoreApplication.translate("encodeFile", u"Volver", None))
        self.tituloLabel.setText(QCoreApplication.translate("encodeFile", u"Proteger Archivo", None))
        ___qtablewidgetitem = self.tableFile.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("encodeFile", u"Archivo", None))
        ___qtablewidgetitem1 = self.tableFile.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("encodeFile", u"Tipo", None))
        ___qtablewidgetitem2 = self.tableFile.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("encodeFile", u"Tama\u00f1o", None))
        self.selectLabel.setText(QCoreApplication.translate("encodeFile", u"Selecciona el archivo a proteger: ", None))
        self.protegerFile_btn.setText(QCoreApplication.translate("encodeFile", u"Proteger Archivo Seleccionado", None))
    # retranslateUi

