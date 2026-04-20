from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QFileDialog, QTableWidget
from PyQt6 import uic
import os
import shutil

class EncodeFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/encodeFilePanel.ui", self)
        self.mainWindow = main_window

        # Obtenemos la ruta donde estan los archivos
        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            # Directorio Actual
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  # Carpeta donde se guardan los archivos

        self.fileSelect = None              # Variable para guardar el nombre del archivo que se selecciona de la tabla

        # Cargamos la tabla
        try:
            self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # Seleccionar fila completa
            self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    # Selección única
            self.tableFile.setRowCount(0)  # Limpiar la tabla antes de cargar los datos
            self.cargarTabla()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla: {str(e)}")

        # Acciones de los botones, los eventos
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.protegerFile_btn.clicked.connect(lambda: self.obtenerArchivoSeleccionado())

    def cargarTabla(self):
        if os.path.exists(self.carpetaArchivos):
            files = os.listdir(self.carpetaArchivos)
            for f in files:
                file_path = os.path.join(self.carpetaArchivos, f)   # Ruta completa del archivo f
                if os.path.isfile(file_path):  # Pregunta si f es un archivo (y no una carpeta)
                    # Obtenemos el tipo y el tamaño de f
                    tipo = os.path.splitext(f)[1] if os.path.splitext(f)[1] else "Sin extensión"
                    tamaño = os.path.getsize(file_path)

                    # Convertir tamaño a formato B, KB o MB
                    if tamaño < 1024:
                        tamaño_str = f"{tamaño} B"
                    elif tamaño < 1024 * 1024:
                        tamaño_str = f"{tamaño / 1024:.2f} KB"
                    else:
                        tamaño_str = f"{tamaño / (1024 * 1024):.2f} MB"
                    
                    rowPosition = self.tableFile.rowCount()
                    self.tableFile.insertRow(rowPosition)
                    self.tableFile.setItem(rowPosition, 0, QTableWidgetItem(f))             # Nombre
                    self.tableFile.setItem(rowPosition, 1, QTableWidgetItem(tipo))          # Tipo
                    self.tableFile.setItem(rowPosition, 2, QTableWidgetItem(tamaño_str))    # Tamaño
    
    def obtenerArchivoSeleccionado(self):
        selected_rows = self.tableFile.selectionModel().selectedRows()
        if selected_rows:
            row = selected_rows[0].row()
            nombre_archivo = self.tableFile.item(row, 0).text()
            self.fileSelect = nombre_archivo
        else:
            self.fileSelect = None

    
    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)