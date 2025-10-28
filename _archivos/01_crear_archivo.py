try:

    #X lo crea si no existe, si existe sale error
    with open("ejemplo.txt", "x") as archivo:
        pass #dejando pass ya lo crea
except Exception as e:
    print(f"Error inesperado {type(e)}")




# W lo crea si no existe  y si existe lo sobrescribre
with open("ejemplo.txt","w") as archivo:
    pass


