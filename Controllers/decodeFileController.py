from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt6 import uic
import os

class DecodeFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/decodeFilePanel.ui", self)
        self.mainWindow = main_window


        # Obtenemos la ruta donde estan los archivos
        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            # Directorio Actual
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  # Carpeta donde se guardan los archivos


        # ---------- SETEOS INICIALES ---------------------------------------------------------------------------------------------------------
        self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # Para que se selecciones la fila completa
        self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    # Para que permita seleccionar una fila a la vez
        self.tableFile.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)      # Para que no permita editar las celdas
        self.tableFile.horizontalHeader().resizeSection(0, 360)
        self.tableFile.horizontalHeader().resizeSection(1, 100)
        self.tableFile.setRowCount(0)  # Limpiar la tabla antes de cargar los datos
        self.textFileP.setReadOnly(True)  # Hacer el QTextEdit de solo lectura
        self.textFileD.setReadOnly(True)  # Hacer el QTextEdit de solo lectura
        self.cargarTabla()  # Cargar los datos en la tabla


        # --------- ACCIONES DE BOTONES Y EVENTOS ----------------------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        #self.desproteger_btn.clicked.connected()
        self.tableFile.itemSelectionChanged.connect(self.mostrarArchivoP)



    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)
    
    def refrescarPanel(self):
        self.tableFile.setRowCount(0)
        self.cargarTabla()
        self.textFileP.clear()
        self.textFileD.clear()

    def showEvent(self, event):
        super().showEvent(event)
        self.refrescarPanel()

    def cargarTabla(self):
        if os.path.exists(self.carpetaArchivos):
            files = os.listdir(self.carpetaArchivos)
            for f in files:
                tipo = os.path.splitext(f)[1]
                file_path = os.path.join(self.carpetaArchivos, f)   # Ruta completa del archivo f
                if tipo == ".HA1" or tipo == ".HA2" or tipo == ".HA3" or tipo == ".HE1" or tipo == ".HE2" or tipo == ".HE3": # 
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
    
    def mostrarArchivoP (self):
        self.textFileP.clear()  
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombreFile = self.tableFile.item(fila,0).text()
        rutaFile = os.path.join(self.carpetaArchivos, nombreFile)
        try: 
            if os.path.exists(rutaFile):
                with open(rutaFile, "r") as f:
                    contenido = f.read()
                bloques = contenido.split()
                for bloque in bloques:
                    if 32<=int(bloque,2)<=126:
                         caracter = chr(int(bloque,2))
                    else:
                        caracter = "$"
                    caracter = chr(int(bloque,2))
                    self.textFileP.insertPlainText(caracter)
            else:
                QMessageBox.critical(self, "Error", "El archivo seleccionado no existe.")
        except Exception as e:
            QMessageBox.critical(self, "Error", "No se ha podido leer el archivo seleccionado.")

    def sacarbitsSinErrores(self):
        with open("Archivos/BTrad1024.txt","r") as f:
            l2 = f.read()
            l1 = ""
            l=""
            i = 0
            c=0
            while i<len(l2):
                if l2[i] == " ":
                    break
                i+=1
            l = l2.replace(" ","")
            s_final = ""
            while(c <= len(l)):
                bloque = l[c:c+i+1]
                if(len(bloque)<i):
                    break
                l1 += self.fromHtoHH(bloque)
                c+=i
            for k in range(0, len(l1), 8):
                btd = l1[k : k + 8]
                if len(btd) == 8:
                    if btd != "00000000":
                        s_final += chr(int(btd, 2))
        with open("Archivos/Trad.txt","w") as f:
            f.write(s_final)


    def fromHtoHH(self, l):
        j=0
        l1 = []
        x=""
        for s in range(len(l)):
            if (2**j == s+1):
                j+=1
            else:
                x += l[s]
        return x
