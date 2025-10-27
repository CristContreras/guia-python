

def leer_archivo(direccion):
    with open(direccion, "r") as archivo:
        contenido = archivo.read()
        print(contenido)

def crear_archivo(direccion):
    with open(direccion, "x") as archivo:
        pass

def verificar_archivo(path)->bool:
    import os
    return os.path.exists(path)

def escribir_archivo(direccion, texto):
    with open(direccion, "a") as archivo:
        archivo.write(f"{texto}\n")
    
def borrar_contenido_archivo(path):
    with open(path,"w") as archivo:
        archivo.write("")



texto = input("Ingrese algo: ")

ubicacion= "C:\\"
nombre_archivo="ejemplo.txt"
path=ubicacion+nombre_archivo



if verificar_archivo(path):
    respuesta = input("Desea eliminar el contenido del archivo?")
    if respuesta == "si":
        borrar_contenido_archivo(path)
    escribir_archivo(path, texto)
    leer_archivo(path)
else:
    print("El archivo ya existe")
    crear_archivo(path)
    escribir_archivo(path, texto)
    leer_archivo(path)
