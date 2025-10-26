# ============================================================================
# 2. re.match() - Busca coincidencia SOLO AL INICIO del texto
# ============================================================================
# Cuándo usar: Para validar que un texto COMIENCE con un patrón específico
# Devuelve: Un objeto Match o None

import re

def ej1():  
    re.match(r"Hola", "Hola mundo") #Coincide
    re.match(r"mundo", "Hola mundo") #No coincide

    if re.match(r"Hola", "Hola mundo"):
        print("Coincide")
        print(re.match(r"Hola", "Hola mundo").group())

    if re.match(r"mundo", "Hola mundo")==None:
        print("No coincide")


def ej2():
    texto1="Python es genial"
    texto2="Me gusta python"
    print(re.match(r"Python",texto1)) #devuelve un objeto
    print(re.match(r"Python", texto2)) #devuelve None
    print(re.match(r"Python",texto1).group()) # devuelve lo encontrado

def main():
    ej1()

if __name__=="__main__":
    main()