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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
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
        self.textFile = QTextEdit(addError)
        self.textFile.setObjectName(u"textFile")
        self.textFile.setGeometry(QRect(660, 230, 571, 381))
        self.selectLabel_2 = QLabel(addError)
        self.selectLabel_2.setObjectName(u"selectLabel_2")
        self.selectLabel_2.setGeometry(QRect(680, 190, 301, 41))
        font1 = QFont()
        font1.setPointSize(15)
        self.selectLabel_2.setFont(font1)
        self.selectLabel = QLabel(addError)
        self.selectLabel.setObjectName(u"selectLabel")
        self.selectLabel.setGeometry(QRect(60, 190, 301, 41))
        self.selectLabel.setFont(font1)
        self.tableFile = QTableWidget(addError)
        if (self.tableFile.columnCount() < 2):
            self.tableFile.setColumnCount(2)
        font2 = QFont()
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2)
        self.tableFile.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableFile.setObjectName(u"tableFile")
        self.tableFile.setGeometry(QRect(40, 230, 570, 381))
        self.tableFile.horizontalHeader().setCascadingSectionResizes(False)
        self.tableFile.horizontalHeader().setDefaultSectionSize(300)
        self.tableFile.horizontalHeader().setHighlightSections(True)
        self.tableFile.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableFile.horizontalHeader().setStretchLastSection(False)
        self.tableFile.verticalHeader().setVisible(True)
        self.tableFile.verticalHeader().setCascadingSectionResizes(False)
        self.tableFile.verticalHeader().setHighlightSections(True)
        self.tableFile.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableFile.verticalHeader().setStretchLastSection(False)
        self.addError_btn = QPushButton(addError)
        self.addError_btn.setObjectName(u"addError_btn")
        self.addError_btn.setGeometry(QRect(230, 640, 191, 41))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.addError_btn.setFont(font3)
        self.loadHA1_btn = QPushButton(addError)
        self.loadHA1_btn.setObjectName(u"loadHA1_btn")
        self.loadHA1_btn.setGeometry(QRect(150, 110, 231, 51))
        self.loadHA1_btn.setFont(font3)
        self.loadHA2_btn = QPushButton(addError)
        self.loadHA2_btn.setObjectName(u"loadHA2_btn")
        self.loadHA2_btn.setGeometry(QRect(520, 110, 231, 51))
        self.loadHA2_btn.setFont(font3)
        self.loadHA3_btn = QPushButton(addError)
        self.loadHA3_btn.setObjectName(u"loadHA3_btn")
        self.loadHA3_btn.setGeometry(QRect(890, 110, 231, 51))
        self.loadHA3_btn.setFont(font3)

        self.retranslateUi(addError)

        QMetaObject.connectSlotsByName(addError)
    # setupUi

    def retranslateUi(self, addError):
        addError.setWindowTitle(QCoreApplication.translate("addError", u"Form", None))
        self.back_btn.setText(QCoreApplication.translate("addError", u"Volver", None))
        self.tituloLabel.setText(QCoreApplication.translate("addError", u"Insertar Error al Archivo", None))
        self.selectLabel_2.setText(QCoreApplication.translate("addError", u"Archivo Seleccionado:", None))
        self.selectLabel.setText(QCoreApplication.translate("addError", u"Seleccionar Archivo: ", None))
        ___qtablewidgetitem = self.tableFile.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("addError", u"Archivo", None))
        ___qtablewidgetitem1 = self.tableFile.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("addError", u"Tama\u00f1o", None))
        self.addError_btn.setText(QCoreApplication.translate("addError", u"Insertar Error", None))
        self.loadHA1_btn.setText(QCoreApplication.translate("addError", u"Cargar Archivos \".HA1\"", None))
        self.loadHA2_btn.setText(QCoreApplication.translate("addError", u"Cargar Archivos \".HA2\"", None))
        self.loadHA3_btn.setText(QCoreApplication.translate("addError", u"Cargar Archivos \".HA3\"", None))
    # retranslateUi

