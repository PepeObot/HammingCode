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
        self.textFileE.setReadOnly(True)  
        self.textFileC.setReadOnly(True)  
        self.cargarTabla()  

        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     
        self.desproteger_btn.clicked.connect(self.mostrarArchivoC)
        self.tableFile.itemSelectionChanged.connect(self.mostrarArchivoE)



    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)
    
    def refrescarPanel(self):
        self.tableFile.setRowCount(0)
        self.cargarTabla()
        self.textFileE.clear()
        self.textFileC.clear()

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
    
    def mostrarArchivoE(self):
        self.textFileE.clear()
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
                self.textFileE.insertPlainText(texto_decodificado)
            else:
                QMessageBox.critical(self, "Error", "El archivo seleccionado no existe.")
        except Exception as e:
            print(f"Error al leer archivo: {e}") 
            QMessageBox.critical(self, "Error", "No se ha podido leer el archivo seleccionado.")

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
            while(c <= len(l)):
                bloque = l[c:c+i+1]
                if(len(bloque)<i):
                    break
                l1 += self.sacarParidad(bloque)
                c+=i
            for k in range(0, len(l1), 8):
                btd = l1[k : k + 8]
                if len(btd) == 8:
                    if btd != "00000000":
                        s_final += chr(int(btd, 2))
        # match os.path.splitext(rutaFile)[1]:
        #     case ".HA2" | ".HE2":
        #         archivoFinal = os.path.splitext(rutaFile)[0] + ".DE2"
        #     case ".HA3" | ".HE3":
        #         archivoFinal = os.path.splitext(rutaFile)[0] + ".DE3"
        # with open(archivoFinal,"w") as f:
        #     f.write(s_final)
        return s_final
    
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
                l1+=self.sacarParidad8(bloque)
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

    def mostrarArchivoC(self):
        self.textFileC.clear()  
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombreFile = self.tableFile.item(fila,0).text()
        rutaFile = os.path.join(self.carpetaArchivos, nombreFile)
        try: 
            if os.path.exists(rutaFile):
                if os.path.splitext(rutaFile)[1] == ".HA1" or os.path.splitext(rutaFile)[1] == ".HE1":
                    texto_decodificado = self.sacarbitsCorregir8(rutaFile)
                else: 
                    texto_decodificado = self.sacarbitsCorregido(rutaFile)
                self.textFileC.insertPlainText(texto_decodificado)
            else:
                QMessageBox.critical(self, "Error", "El archivo seleccionado no existe.")
        
        except Exception as e:
            print(f"Error al leer archivo: {e}") 
            QMessageBox.critical(self, "Error", "No se ha podido leer el archivo seleccionado.")
        except ValueError as ve:
            QMessageBox.critical(self, "Error de Datos", f"El archivo contiene caracteres no binarios o está corrupto.\nDetalle: {ve}")
    
    def sacarbitsCorregir8(self, rutaFile):
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
                l1+=self.sacarParidad8(self.hamming_ver8(bloque))
                c+=i
            for k in range(0, len(l1), 8):
                btd = l1[k : k + 8]
                if len(btd) == 8:
                    if btd != "00000000":
                        s_final += chr(int(btd, 2))
        archivoFinal = os.path.splitext(rutaFile)[0] + ".DC1"
        with open(archivoFinal,"w") as f:
            f.write(s_final)
        return s_final
        
    
    def sacarbitsCorregido(self, rutaFile):
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
            #i+=1
            l = l2.replace(" ","")
            s_final = ""
            while(c <= len(l)):
                bloque = l[c:c+i]
                if(len(bloque)<i):
                    break
                l1 += self.sacarParidad(self.unhamming_not8(bloque)) 
                c+=i
            for k in range(0, len(l1), 8):
                btd = l1[k : k + 8]
                if len(btd) == 8:
                    if btd != "00000000":
                        s_final += chr(int(btd, 2))
        #ruta_trad = os.path.join(self.carpetaArchivos, "Trad.txt")
        match os.path.splitext(rutaFile)[1]:
            case ".HA2" | ".HE2":
                archivoFinal = os.path.splitext(rutaFile)[0] + ".DC2"
            case ".HA3" | ".HE3":
                archivoFinal = os.path.splitext(rutaFile)[0] + ".DC3"
        with open(archivoFinal, "w") as f:
            f.write(s_final)        # Aca se traba al deshamminizar con mod 8
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
    
    def sacarParidad8(self, l):
        j = 0	
        x=""
        x1=""
        y = l[0:8]
        y1= l[8:16]
        for i in range(0,8): 
            if (2**j == i+1):
                j+=1
            else:
                x += y[i]
                x1 += y1[i]
        x+=x1
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
        for i in range(long + p):
            if (((i + 1) & i) != 0):
                trama[i] = n1[j]
                j += 1
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
    
    def hamming_ver8(self, n1): 
        j = 0   
        x=""
        x1=""
        y_bloque = n1[0:8]   
        y1_bloque = n1[8:16] 
        
        for i in range(0,8): 
            if (2**j == i+1):
                j+=1
            else:
                x += y_bloque[i]
                x1 += y1_bloque[i]

        x+=x1
        l = self.hamminization(x) 
        
        if (l != n1):
            listapp = list(n1)
            
            if l[0:8] != y_bloque:
                i = 1
                y_sin = ""
                z_sin = ""
                j = 0
                while i <= 8:
                    y_sin += y_bloque[i-1]
                    z_sin += l[0:8][i-1]
                    j += 1
                    i = 2**j
                xy = ""
                for k in range(0,len(y_sin)):
                    xy += str(int(y_sin[k]) ^ int(z_sin[k]))
                
                xy_r = int(xy[::-1], 2)
                
                if xy_r <= 8 and xy_r > 0:
                    if listapp[xy_r-1] == '0':
                        listapp[xy_r-1] = '1'
                    else:
                        listapp[xy_r-1] = '0'
            if l[8:16] != y1_bloque:
                i = 1
                y_sin = ""
                z_sin = ""
                j = 0
                while i <= 8:
                    y_sin += y1_bloque[i-1]
                    z_sin += l[8:16][i-1]
                    j += 1
                    i = 2**j
                xy = ""
                for k in range(0,len(y_sin)):
                    xy += str(int(y_sin[k]) ^ int(z_sin[k]))
                
                xy_r = int(xy[::-1], 2)
                
                if xy_r <= 8 and xy_r > 0:
                    # Le sumamos 8 a la posición porque estamos en la segunda mitad
                    if listapp[8 + xy_r - 1] == '0':
                        listapp[8 + xy_r - 1] = '1'
                    else:
                        listapp[8 + xy_r - 1] = '0'

            sol = "".join(listapp)
            return sol
        else:
            return n1
    
    def hamminization(self,n1):
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