import prueba as p

def mostrar_menu():
    print("=== Menú principal ===")
    print("1. Mostrar el contenido del archivo")
    print("2. Pasar el archivo a binario según ASCII")
    print("3. Salir")

def mostrar_menu_trad():
    print("=== Hamminization Machine ===")
    print("1. Hamminization para 8")
    print("2. Hamminization para 1024")
    print("3. Hamminization para 16384")
    print("4. No' vemo'")

def mostrarArchivo():
    try:
        with open("Archivos/textoA.txt", "r", encoding="utf-8") as archivo: #ESTO HAY QUE CAMBIARLO CADA VEX QUE QUIERAS ENTRAR AL ARCHIVO. YO LO PUSE PARA MI RUTA ESPECIFICA.
            texto = archivo.read()
            print(f"Contenido del archivo es: {texto}")
    except FileNotFoundError:
        print("El archivo no se encontró.")
    archivo.close()

def enBinario():
    l = []
    l1 = []
    s_final = ""
    while True:
        mostrar_menu_trad()
        eleccion = input("Elija tamaño para la Hamminization Machine ")
        match eleccion :
            case "1": #ESTO ES PARA 8 BITS.
                print("HOLA?")
                try:
                    with open("Archivos/textoD.txt", "rb") as archivo:                #Con "rb" se abre el archivo en modo lectura binaria, lo que permite leer los bytes directamente.
                        contenido = archivo.read()
                    for byte in contenido:
                        if 32<=byte<=126:
                            caracter = chr(byte)
                        else:
                            caracter = "-"
                        l.append(f"{format(byte,'08b')}")
                        print(f"{byte:3} - {format(byte, '08b')} - {caracter}") #format(byte, '08b') convierte el byte a su representación binaria de 8 bits completando con ceros a la izquierda si es necesario.
                    archivo.close()
                except FileNotFoundError:
                    print("El archivo no se encontró.")
                with open("Archivos/BTrad.txt", "w") as arch:
                    for b in l:
                        arch.write(p.hamminization(b))
                        arch.write(" ")
                arch.close()
            case "2": #ESTO ES PARA 1024 BITS.
                try:
                    i=0
                    with open("Archivos/textoD.txt", "rb") as archivo:                #Con "rb" se abre el archivo en modo lectura binaria, lo que permite leer los bytes directamente.
                        contenido = archivo.read()
                    for byte in contenido:
                        if 32<=byte<=126:
                            caracter = chr(byte)
                        else:
                            caracter = "-"
                        l.append(f"{format(byte,'08b')}")
                        s_final += l[i]
                        i+=1
                        print(i)
                        print(f"{byte:3} - {format(byte, '08b')} - {caracter}") #format(byte, '08b') convierte el byte a su representación binaria de 8 bits completando con ceros a la izquierda si es necesario.
                    x = len(s_final)
                    n=0
                    while n <= len(s_final):
                        if x-n < 0:
                            l1.append(f"{s_final[n-1024:x]}")
                            print("ENENETRAAR")
                            break
                        l1.append(f"{s_final[n:n+1024]}")
                        n+=1024
                    archivo.close()
                except FileNotFoundError:
                    print("El archivo no se encontró.")
                #print(l1[0])    
            case "3": # PARA 16384 BITS.
                try:
                    i=0
                    with open("Archivos/textoC.txt", "rb") as archivo:                #Con "rb" se abre el archivo en modo lectura binaria, lo que permite leer los bytes directamente.
                        contenido = archivo.read()
                    for byte in contenido:
                        if 32<=byte<=126:
                            caracter = chr(byte)
                        else:
                            caracter = "-"
                        l.append(f"{format(byte,'08b')}")
                        s_final += l[i]
                        i+=1
                        print(i)
                        print(f"{byte:3} - {format(byte, '08b')} - {caracter}") #format(byte, '08b') convierte el byte a su representación binaria de 8 bits completando con ceros a la izquierda si es necesario.
                    x = len(s_final)
                    n=0
                    while n <= len(s_final):
                        if x-n < 0:
                            l1.append(f"{s_final[n-16384:x]}")
                            print("ENENETRAAR")
                            break
                        l1.append(f"{s_final[n:n+16384]}")
                        n+=16384
                    archivo.close()
                except FileNotFoundError:
                    print("El archivo no se encontró.")
        with open("Archivos/BTrad16384.txt", "w") as arch:
            for b in l1:
                arch.write(p.hamminization(b))
                arch.write(" ")
        arch.close()


def main():
    while True:
        mostrar_menu()
        eleccion = input("Selecciona una opción: ")

        if eleccion == "1":
            mostrarArchivo()
        elif eleccion == "2":
            enBinario()
        elif eleccion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
        print()

if __name__ == "__main__":
    main()