#validar si se ingresa solo numeros

def forma_1():#es para negativos , positivos y decimales
    repetir = True
    while repetir:
        entrada = input("Ingrese un numero: ")
        try:
            valor = int(entrada)
            repetir=False
        except Exception as e:
            print(f"Error debe ser solo numeros: {e}") 
    print("Es un numero")

def forma_2(): #no valida negativos
    def es_numero(dato :str)->bool:
        import re
        return True if re.match(r"^\d+$", dato) else False
        #return True if re.match(r"^-?\d+$|^-?\d+\.\d+$") else False    #forma para negativos, positivos y decimales
    repetir = True
    while repetir:
        entrada = input("Ingrese un numero: ")
        if es_numero(entrada):
            entrada=int(entrada)
            repetir=False
        else:
            print("Debe ingresar solo numeros")
    
def forma_3():
    repetir = True
    while repetir:
        entrada=input("Ingrese un numero: ")
        if entrada.isdigit():
            print("Es un numero")
            repetir=False
        else:
            print("No es un numero")


def main():
    pass
if __name__=="__main__":
    main()