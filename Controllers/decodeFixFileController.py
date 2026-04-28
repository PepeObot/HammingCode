from PyQt6.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QWidget
from PyQt6 import uic
import os

class DecodeFixFileController(QWidget):
    def __init__(self, main_window):
        # ... [Todo tu __init__ original queda igual] ...
        super().__init__()
        uic.loadUi("Ventanas/decodeFixFilePanel.ui", self)
        self.mainWindow = main_window

        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  

        self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  
        self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    
        self.tableFile.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)      
        self.tableFile.horizontalHeader().resizeSection(0, 360)
        self.tableFile.horizontalHeader().resizeSection(1, 100)
        self.tableFile.setRowCount(0)  
        self.textFileP.setReadOnly(True)  
        self.textFileD.setReadOnly(True)  
        self.cargarTabla()  

        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     
        self.desproteger_btn.clicked.connect(self.mostrarArchivoD)
        self.tableFile.itemSelectionChanged.connect(self.mostrarArchivoD)



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
    
    def mostrarArchivoD(self):
        self.textFileP.clear()  
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombreFile = self.tableFile.item(fila,0).text()
        rutaFile = os.path.join(self.carpetaArchivos, nombreFile)
        
        try: 
            if os.path.exists(rutaFile):
                texto_decodificado = self.sacarbits(rutaFile)
                
                self.textFileD.setPlainText(texto_decodificado)
            else:
                QMessageBox.critical(self, "Error", "El archivo seleccionado no existe.")
        except Exception as e:
            print(f"Error: {e}") 
            QMessageBox.critical(self, "Error", "No se ha podido leer el archivo seleccionado.")
        
        except ValueError as ve:
            QMessageBox.critical(self, "Error de Datos", f"El archivo contiene caracteres no binarios o está corrupto.\nDetalle: {ve}")
        except Exception as e:
            print(f"Error al leer archivo: {e}")
            QMessageBox.critical(self, "Error", "No se ha podido leer el archivo seleccionado.")
    
    def sacarbits(self, rutaFile):
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
            i+=1
            print(i)
            l = l2.replace(" ","")
            s_final = ""
            while(c <= len(l)):
                bloque = l[c:c+i]
                if(len(bloque)<i):
                    break
                l1 += self.fromHtoHH(self.unhamming_not8(bloque)) 
                c+=i
            for k in range(0, len(l1), 8):
                btd = l1[k : k + 8]
                if len(btd) == 8:
                    if btd != "00000000":
                        s_final += chr(int(btd, 2))
        
        ruta_trad = os.path.join(self.carpetaArchivos, "Trad.txt")
        with open(ruta_trad, "w") as f:
            f.write(s_final)
        return s_final
    
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
    
    def unhamming_not8(self,n1):
        j = 0
        x = ""
        for i in range (len(n1)):
            if (2**j == i+1):
                j+=1
            else:
                x += n1[i]
        l = self.hamminization_not8(x)
        i=0
        if (l != n1):
            i = 1
            y = ""
            z = ""
            j = 0
            while i <= len(n1):
                if i-1 < len(l):
                    y += n1[i-1]
                    z += l[i-1]
                j += 1
                i = 2**j
            xy = ""
            for i in range(0,len(y)):
                xy += str(int(y[i]) ^ int(z[i]))
            xy_r = xy[::-1]
            #print(xy_r)
            if xy_r == 0 or (int(xy_r) & (int(xy_r) - 1)) == 0:
                return l
            xy_r = int(xy_r,2)
            #print (xy_r)
            listapp = list(n1)
            if xy_r <= len(listapp):
                if listapp[xy_r-1] == '0':
                    listapp[xy_r-1] = '1'
                else:
                    listapp[xy_r-1] = '0'
            sol = "".join(listapp)
            return sol
        else:
            return n1
        
    def hamminization_not8(self,n1):
        long = len(n1)
        p = 0
        while (2**p < len(n1)+p+1):
            p+=1

        trama = ['0'] * (long+p)
        j = 0
        for i in range (long+p):
            if ((i & (i-1))!= 0):
                trama[i-1] = n1[j]
                j+=1
        for l in range(p):
            i = (2**l)
            sum = 0
            for cont1 in range(long+p):
                preal = cont1 + 1
                if(preal & i) != 0:
                    if preal != i:
                        sum = sum ^ int(trama[cont1])
            trama[i-1] = str(sum)
        sum=0
        l = 0
        while l < len(trama):
            sum += int(trama[l])
            l+=1
        if sum%2 == 0:
            trama[len(trama)-1] = "1"
        else:
            trama[len(trama)-1] = "0"

        sol = "".join(trama)
        return sol