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
        
        # ---------- SETEOS INICIALES ----------
        # Cargamos la tabla
        try:
            self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # Seleccionar fila completa
            self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    # Selección única
            self.tableFile.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
            self.tableFile.horizontalHeader().resizeSection(0, 400)
            self.tableFile.horizontalHeader().resizeSection(1, 150)
            self.tableFile.setRowCount(0)  # Limpiar la tabla antes de cargar los datos
            self.cargarTabla()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla: {str(e)}")
        self.textFile.setReadOnly(True)  # Hacer el QTextEdit de solo lectura

        # --------- ACCIONES DE BOTONES Y EVENTOS ---------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.protegerFile_btn.clicked.connect(lambda: self.obtenerArchivoSeleccionado())
        self.tableFile.itemSelectionChanged.connect(self.mostrarArchivo)
        #self.protegerFile8_btn.clicked.connect("funcion")
        #self.protegerFile1024_btn.clicked.connect("funcion")
        #self.protegerFile16384_btn.clicked.connect("funcion")




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
                    self.tableFile.setItem(rowPosition, 1, QTableWidgetItem(tamaño_str))    # Tamaño
    
    def mostrarArchivo(self):
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombre_archivo = self.tableFile.item(fila, 0).text()
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        rutaFile = os.path.join(directorio_actual, "..", "Archivos", nombre_archivo)
        try:
            if os.path.exists(rutaFile):
                with open(rutaFile, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.textFile.setPlainText(contenido)
            else:
                self.textFile.setPlainText("Error: El archivo no existe en la ruta especificada.")
        except Exception as e:
            self.textFile.setPlainText(f"No se pudo leer el archivo: {str(e)}")
            

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