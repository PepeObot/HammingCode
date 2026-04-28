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
        self.textFileD.setReadOnly(True)  # Hacer el QTextEdit de solo lectura
        self.cargarTabla()  # Cargar los datos en la tabla


        # --------- ACCIONES DE BOTONES Y EVENTOS ----------------------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.desproteger_btn.clicked.connect(self.mostrarArchivoD)     # Muestra el contenido del archivo seleccionado en el QTextEdit de la derecha
        #self.tableFile.itemSelectionChanged.connect(self.mostrarArchivoD)



    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)
    
    def refrescarPanel(self):
        self.tableFile.setRowCount(0)
        self.cargarTabla()
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
    
    def mostrarArchivoD (self):
        self.textFileD.clear()  
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombreFile = self.tableFile.item(fila,0).text()
        rutaFile = os.path.join(self.carpetaArchivos, nombreFile)
        try: 
            if os.path.exists(rutaFile):
                if os.path.splitext(rutaFile)[1] == ".HA1" or os.path.splitext(rutaFile)[1] == ".HE1":
                    texto_decodificado = self.sacarbitsSinCorregir8(rutaFile)
                else: 
                    texto_decodificado = self.sacarbitsSinCorregir(rutaFile)
                self.textFileD.insertPlainText(texto_decodificado)
            else:
                QMessageBox.critical(self, "Error", "El archivo seleccionado no existe.")
        except Exception as e:
            QMessageBox.critical(self, "Error", "No se ha podido leer el archivo seleccionado.")

    #def mostrarArchivoD (self):

    def sacarbitsSinCorregir(self, rutaFile):
        with open(rutaFile, "r") as f:
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
            while c < len(l):
                bloque = l[c:c+i]
                if len(bloque) < i:
                    break
                l1 += self.sacarParidad(bloque)
                c += i
            for k in range(0, len(l1), 8):
                btd = l1[k : k + 8]
                if len(btd) == 8:
                    if btd != "00000000":
                        s_final += chr(int(btd, 2))
        match os.path.splitext(rutaFile)[1]:
            case ".HA2" | ".HE2":
                archivoFinal = os.path.splitext(rutaFile)[0] + ".DE2"
            case ".HA3" | ".HE3":
                archivoFinal = os.path.splitext(rutaFile)[0] + ".DE3"
        with open(archivoFinal,"w") as f:
            f.write(s_final)
        return s_final

    def sacarParidad(self, l):
        j=0
        l1 = []
        x=""
        for s in range(len(l)):
            if (2**j == s+1):
                j+=1
            else:
                x += l[s]
        return x
    
    def sacarbitsSinCorregir8(self, rutaFile):
        with open(rutaFile, "r") as f:
            l = ""
            s_final= ""
            l1 = ""
            l2 = f.read().replace(" ","")
            c = 0
            i = 16
            l = l2
            while c<=len(l):
                bloque = l[c:c+i]
                if(len(bloque)<i):
                    break
                l1+= self.sacarParidad8(bloque)
                c+=i
            for k in range(0, len(l1), 8):
                btd = l1[k : k + 8]
                if len(btd) == 8:
                    if btd != "00000000":
                        s_final += chr(int(btd, 2))
        archivoFinal = os.path.splitext(rutaFile)[0] + ".DE1"
        with open(archivoFinal,"w") as f:
            f.write(s_final)
        return s_final

    def sacarParidad8(self, l):
        j = 0	
        x=""
        x1=""
        y = l[0:8]
        y1= l[8:16]
        print(y)
        for i in range(0,8): 
            if (2**j == i+1):
                j+=1
            else:
                x += y[i]
                x1 += y1[i]
        x+=x1
        print(x)
        return x