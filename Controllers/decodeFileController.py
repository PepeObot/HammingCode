from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class DecodeFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/decodeFilePanel.ui", self)
        self.mainWindow = main_window

        # Acciones de los botones, los eventos
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio

    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)