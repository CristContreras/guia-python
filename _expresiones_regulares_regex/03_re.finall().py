#Encuentra todas las coincidencias y las devuelve en una lista
import re

def ej1():

    texto = "Tengo 2 perros y 3 gatos"
    numeros = re.findall(r"\d+", texto)
    print(numeros)


def ej2():
    #Encuentra letras mayusculuas seguidas de numeros y muestralas

    texto = "Mi placa es ABC123 y mi código es XYZ789"
    placas: list[str] = re.findall(r"[A-Z]{3}", texto) #encuentra letras [A-Z] de 3 posiciones 
    codigos: list[str]=re.findall(r"\d{3}", texto) #encuentra numeros [0-9] de 3 posiciones

    #print(conver_unalinea(placas))
    #print(*placas, sep="-")
    desemp= "-".join(placas)
    
def conver_unalinea(lista:list):
    return "-".join(linea for linea in lista)

def main():
    ej2()

if __name__=="__main__":
    main()