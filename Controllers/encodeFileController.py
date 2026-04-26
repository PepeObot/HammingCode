from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt6 import uic
import os

class EncodeFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/encodeFilePanel.ui", self)
        self.mainWindow = main_window

        # Obtenemos la ruta donde estan los archivos
        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            # Directorio Actual
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  # Carpeta donde se guardan los archivos

        self.fileSelect = None              # Variable para guardar el nombre del archivo que se selecciona de la tabla
        
        # ---------- SETEOS INICIALES ---------------------------------------------------------------------------------------------------------
        # Cargamos la tabla
        try:
            self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # Para que se selecciones la fila completa
            self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    # Para que permita seleccionar una fila a la vez
            self.tableFile.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)      # Para que no permita editar las celdas
            self.tableFile.horizontalHeader().resizeSection(0, 400)
            self.tableFile.horizontalHeader().resizeSection(1, 150)
            self.tableFile.setRowCount(0)  # Limpiar la tabla antes de cargar los datos
            self.cargarTabla()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla: {str(e)}")

        self.textFile.setReadOnly(True)  # Hacer el QTextEdit de solo lectura


        # --------- ACCIONES DE BOTONES Y EVENTOS ---------------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.tableFile.itemSelectionChanged.connect(self.mostrarArchivo)    # Muestra el contenido del archivo seleccionado en el QTextEdit
        self.protegerFile8_btn.clicked.connect(self.hamming_8)
        #self.protegerFile1024_btn.clicked.connect(self.hamming_1024)
        #self.protegerFile16384_btn.clicked.connect(self.hamming_16384)


    def refrescarPanel(self):
        self.tableFile.setRowCount(0)
        self.cargarTabla()
        self.textFile.clear()

    def showEvent(self, event):
        super().showEvent(event)
        self.refrescarPanel()

    def cargarTabla(self):
        if os.path.exists(self.carpetaArchivos):
            files = os.listdir(self.carpetaArchivos)
            for f in files:
                file_path = os.path.join(self.carpetaArchivos, f)   # Ruta completa del archivo f
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
            return nombre_archivo
        else:
            return None

    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)

    def hamming_8(self):
        l = []
        self.fileSelect = self.obtenerArchivoSeleccionado()
        baseFile = os.path.splitext(self.fileSelect)[0]  # Obtener el nombre del archivo, sin la extensión
        try:
            with open(os.path.join(self.carpetaArchivos,self.fileSelect),'rb')as archivo:
                # PASAR A BITS
                contenido = archivo.read()
                for byte in contenido:
                    if 32<=byte<=126:
                        caracter = chr(byte)
                    else:
                        caracter = "-"
                    l.append(f"{format(byte,'08b')}")
                    #print(f"{byte:3} - {format(byte, '08b')} - {caracter}") #format(byte, '08b') convierte el byte a su representación binaria de 8 bits completando con ceros a la izquierda si es necesario.
            # archivo.close()   Lo comento xq puede causar errores ya que with lo cierra automaticamente
            with open(os.path.join(self.carpetaArchivos, baseFile + ".HA1"),'w') as f:
                bloques = [self.hamminization8(b) for b in l]
                f.write(" ".join(bloques))
                # for b in l:
                #     x = self.hamminization8(b)
                #     f.write(x)
                #     f.write(" ")
            # f.close()    Lo comento xq puede causar errores ya que with lo cierra automaticamente
            QMessageBox.information(self, "Éxito", f"Archivo protegido con Hamming (mod 8) correctamente. \nGuardado en '{baseFile}.HA1'.")
            self.refrescarPanel()
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "No se pudo encontrar el archivo seleccionado.")

    def hamming_1024(self):
        l = []
        l1 = []
        i = 0
        s_final1 = None
        self.fileSelect = self.obtenerArchivoSeleccionado()
        try:
            with open(os.path.join(self.carpetaArchivos,self.fileSelect),'rb')as archivo:
                # PASAR A BITS
                contenido = archivo.read()
            for byte in contenido:
                if 32<=byte<=126:
                    caracter = chr(byte)
                else:
                    caracter = "-"
                l.append(f"{format(byte,'08b')}")
                s_final1 += l[i]
                i+=1
                #print(f"{byte:3} - {format(byte, '08b')} - {caracter}") #format(byte, '08b') convierte el byte a su representación binaria de 8 bits completando con ceros a la izquierda si es necesario.
            x = len(s_final1)
            n = 0
            while n <= len(s_final1):
                    if x-n < 0:
                        l1.append(f"{s_final1[n-1024:x]}")
                        break
                    l1.append(f"{s_final1[n:n+1024]}")
                    n+=1024 
            # archivo.close()   Lo comento xq puede causar errores ya que with lo cierra automaticamente
            with open(os.path.join(self.carpetaArchivos,"BTrad1024.txt"),'w') as f:
                for b in l1:
                    """

                    ACA VA EL HAMMING DE MOD 1024 NO PARA MOD 8
                    
                    """
                    x = self.hamminization(b)
                    f.write(x)
                    f.write(" ")
            # f.close()    Lo comento xq puede causar errores ya que with lo cierra automaticamente
            QMessageBox.information(self, "Éxito", "Archivo protegido con Hamming (mod 1024) correctamente. Guardado en 'BTrad1024.txt'.")
            self.refrescarPanel()

        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "No se pudo encontrar el archivo seleccionado.")

    def hamming_16384(self):
        l = []
        l1 = []
        i = 0
        s_final = ""
        self.fileSelect = self.obtenerArchivoSeleccionado()
        try:
            with open(os.path.join(self.carpetaArchivos,self.fileSelect),'rb')as archivo:
                # PASAR A BITS
                contenido = archivo.read()
            for byte in contenido:
                if 32<=byte<=126:
                        caracter = chr(byte)
                else:
                        caracter = "-"
                l.append(f"{format(byte,'08b')}")
                s_final += l[i]
                i+=1
                #print(f"{byte:3} - {format(byte, '08b')} - {caracter}") #format(byte, '08b') convierte el byte a su representación binaria de 8 bits completando con ceros a la izquierda si es necesario.
            x = len(s_final)
            n = 0
            while n <= len(s_final):
                    if x-n < 0:
                        l1.append(f"{s_final[n-16384:x]}")
                        break
                    l1.append(f"{s_final[n:n+16384]}")
                    n+=16384
            # archivo.close()   Lo comento xq puede causar errores ya que with lo cierra automaticamente
            with open(os.path.join(self.carpetaArchivos,"BTrad16384.txt"),'w') as f:
                for b in l1:
                    """

                    ACA VA EL HAMMING DE MOD 16384 NO PARA MOD 8
                    
                    """
                    #x = self.hamminization(b)
                    f.write(x)
                    f.write(" ")
            # f.close()    Lo comento xq puede causar errores ya que with lo cierra automaticamente
            QMessageBox.information(self, "Éxito", "Archivo protegido con Hamming (mod 16384) correctamente. Guardado en 'BTrad16384.txt'.")
            self.refrescarPanel()

        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "No se pudo encontrar el archivo seleccionado.")

    """
    FALTA ARMAR HAMMING PARA MOD 1024 y 16384. HACER!
    """


    def hamminization8(self, n1):
        long = len(n1)
        p = 0
        
        while (2**p < len(n1)+p+1):
            p+=1

        trama1 = ['0'] * (long)
        trama = ['0'] * (long)

        j=0

        for i in range(1, long):
            if((i & (i-1)) != 0 ):
                trama[i-1] = n1[j]
                j+=1


        for i in range(1,long):
            if ((i&(i-1))!=0):
                trama1[i-1] = n1[j]
                j+=1

        for l in range(p):
            i = (2**l)
            sum = 0
            sum1 = 0
            for cont1 in range (long):
                posicion_real = cont1 + 1
                if(posicion_real & i) != 0:
                    if posicion_real!=i:
                        sum = sum ^ int(trama[cont1])
                        sum1 = sum1 ^ int(trama1[cont1])	
            trama[i-1] = str(sum)
            trama1[i-1] = str(sum1)

        sum = 0
        sum1 = 0

        while l < len(trama):
            sum += int(trama[l]) 
            sum1 += int(trama1[l])
            l+=1

        if sum%2 == 0:
            trama[len(trama)-1] = "1"
        else:
            trama[len(trama)-1] = "0"

        if sum1%2 == 0:
            trama1[len(trama1)-1] = "1"
        else:
            trama1[len(trama1)-1] = "0"

        sol = "".join(trama)
        sol += "".join(trama1)

        return sol 