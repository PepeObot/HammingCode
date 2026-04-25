from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt6 import uic
import os

class AddErrorController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/addErrorPanel.ui", self)
        self.mainWindow = main_window

        # Obtenemos la ruta donde estan los archivos
        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            # Directorio Actual
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  # Carpeta donde se guardan los archivos


        # ---------- SETEOS INICIALES ---------------------------------------------------------------------------------------------------------
        self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # Para que se selecciones la fila completa
        self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    # Para que permita seleccionar una fila a la vez
        self.tableFile.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)      # Para que no permita editar las celdas
        self.tableFile.horizontalHeader().resizeSection(0, 400)
        self.tableFile.horizontalHeader().resizeSection(1, 150)
        self.tableFile.setRowCount(0)  # Limpiar la tabla antes de cargar los datos
        self.textFile.setReadOnly(True)  # Hacer el QTextEdit de solo lectura


        # --------- ACCIONES DE BOTONES Y EVENTOS ----------------------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.loadHA1_btn.clicked.connect(self.cargarArchivosHA1)  # Carga los archivos tipo HA1 en la tabla
        self.loadHA2_btn.clicked.connect(self.cargarArchivosHA2)  # Carga los archivos tipo HA2 en la tabla
        self.loadHA3_btn.clicked.connect(self.cargarArchivosHA3)  # Carga los archivos tipo HA3 en la tabla
        self.tableFile.itemSelectionChanged.connect(self.mostrarArchivo)    # Muestra el contenido del archivo seleccionado en el QTextEdit



    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)

    def refrescarPanel(self, mod):
        self.tableFile.setRowCount(0)
        self.cargarTabla(mod)
        self.textFile.clear()

    def showEvent(self, event):
        super().showEvent(event)
        self.refrescarPanel(0)

    def cargarTabla(self, mod):
        if os.path.exists(self.carpetaArchivos):
            files = os.listdir(self.carpetaArchivos)
            for f in files:
                tipo = os.path.splitext(f)[1]
                file_path = os.path.join(self.carpetaArchivos, f)   # Ruta completa del archivo f
                match mod:
                    case 0:
                        try: 
                            if os.path.isfile(file_path):  # Pregunta si f es un archivo (y no una carpeta)
                                # Obtenemos el tamaño de f
                                tamaño = os.path.getsize(file_path)

                                # Convertir tamaño a formato B, KB o MB
                                if tamaño < 1024:
                                    tamaño_str = f"{tamaño} B"
                                elif tamaño < 1024 * 1024:
                                    tamaño_str = f"{tamaño / 1024:.2f} KB"
                                else:
                                    tamaño_str = f"{tamaño / (1024 * 1024):.2f} MB"
                                
                                # Agregamos el archivo a la tabla
                                rowPosition = self.tableFile.rowCount()
                                self.tableFile.insertRow(rowPosition)
                                self.tableFile.setItem(rowPosition, 0, QTableWidgetItem(f))             # Nombre
                                self.tableFile.setItem(rowPosition, 1, QTableWidgetItem(tamaño_str))    # Tamaño
                        except FileNotFoundError:
                            QMessageBox.critical(self, "Error", "No se han encontrado archivos en la carpeta 'Archivos'.")
                    case 1:
                        try: 
                            if tipo == ".HA1":  # Busca que el archivo sea tipo HA1
                                # Obtenemos el tamaño de f
                                tamaño = os.path.getsize(file_path)

                                # Convertir tamaño a formato B, KB o MB
                                if tamaño < 1024:
                                    tamaño_str = f"{tamaño} B"
                                elif tamaño < 1024 * 1024:
                                    tamaño_str = f"{tamaño / 1024:.2f} KB"
                                else:
                                    tamaño_str = f"{tamaño / (1024 * 1024):.2f} MB"
                                
                                # Agregamos el archivo a la tabla
                                rowPosition = self.tableFile.rowCount()
                                self.tableFile.insertRow(rowPosition)
                                self.tableFile.setItem(rowPosition, 0, QTableWidgetItem(f))             # Nombre
                                self.tableFile.setItem(rowPosition, 1, QTableWidgetItem(tamaño_str))    # Tamaño
                        except FileNotFoundError:
                            QMessageBox.critical(self, "Error", "No se han encontrado archivos tipo '.HA1'.")
                    case 2:
                        try:
                            if tipo == ".HA2":  # Busca que el archivo sea tipo HA2
                                # Obtenemos el tamaño de f
                                tamaño = os.path.getsize(file_path)

                                # Convertir tamaño a formato B, KB o MB
                                if tamaño < 1024:
                                    tamaño_str = f"{tamaño} B"
                                elif tamaño < 1024 * 1024:
                                    tamaño_str = f"{tamaño / 1024:.2f} KB"
                                else:
                                    tamaño_str = f"{tamaño / (1024 * 1024):.2f} MB"
                                
                                # Agregamos el archivo a la tabla
                                rowPosition = self.tableFile.rowCount()
                                self.tableFile.insertRow(rowPosition)
                                self.tableFile.setItem(rowPosition, 0, QTableWidgetItem(f))             # Nombre
                                self.tableFile.setItem(rowPosition, 1, QTableWidgetItem(tamaño_str))    # Tamaño
                        except FileNotFoundError:
                            QMessageBox.critical(self, "Error", "No se han encontrado archivos tipo '.HA2'.") 
                    case 3:
                        try:
                            if tipo == ".HA3":  # Busca que el archivo sea tipo HA3
                                # Obtenemos el tamaño de f
                                tamaño = os.path.getsize(file_path)

                                # Convertir tamaño a formato B, KB o MB
                                if tamaño < 1024:
                                    tamaño_str = f"{tamaño} B"
                                elif tamaño < 1024 * 1024:
                                    tamaño_str = f"{tamaño / 1024:.2f} KB"
                                else:
                                    tamaño_str = f"{tamaño / (1024 * 1024):.2f} MB"
                                
                                # Agregamos el archivo a la tabla
                                rowPosition = self.tableFile.rowCount()
                                self.tableFile.insertRow(rowPosition)
                                self.tableFile.setItem(rowPosition, 0, QTableWidgetItem(f))             # Nombre
                                self.tableFile.setItem(rowPosition, 1, QTableWidgetItem(tamaño_str))    # Tamaño
                        except FileNotFoundError:
                            QMessageBox.critical(self, "Error", "No se han encontrado archivos tipo '.HA3'.") 

    def cargarArchivosHA1(self):
        self.refrescarPanel(1)
    
    def cargarArchivosHA2(self):
        self.refrescarPanel(2)

    def cargarArchivosHA3(self):
        self.refrescarPanel(3)

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
    
    #def insertarError(self):
