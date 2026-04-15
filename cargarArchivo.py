import os


# Abrir y leer el archivo elegido
def abrirArchivo():
    ruta_archivo = os.path.join(directorio, archivo_elegido)
    print(f"\nAbriendo archivo: {archivo_elegido}\n")
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido)

#------------------------------------------------------------------------------------------------------

# Obtener el directorio actual
directorio = os.getcwd()
# Obtener el directorio de una carpeta X dentra del proyecto actual: directorio = os.path.join(os.getcwd(), "X")
# Obtener el directorio de una carpeta X en otra ruta: directorio = "D:/ruta/a/la/carpeta/X"


# Obtener lista de archivos (sin carpetas)
#archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
# Obtener lista de archivos con extensión específica (ejemplo: .txt)
archivos = [f for f in os.listdir(directorio) if f.endswith('.txt')]

# Mostrar opciones al usuario
print("Archivos disponibles:")
for i, archivo in enumerate(archivos, 1):
    print(f"{i}. {archivo}")
print("0. Salir")

# Pedir al usuario que elija uno
while True:
    try:
        opcion = int(input("\nElige el número del archivo: "))
        if 1 <= opcion <= len(archivos):
            archivo_elegido = archivos[opcion - 1]
            abrirArchivo()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print(f"Por favor, elige un número entre 1 y {len(archivos)}")
            
    except ValueError:
        print("Debes ingresar un número válido")

