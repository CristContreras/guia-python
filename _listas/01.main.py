def ej1():
    nombres: list[str] = []

    #mostrar cada nombre
    for nombre in nombres:
        print(nombre)
    
    #unir elementos en una linea y mostrar
    texto = "-".join(nombres)
    print(texto)

    #agregar nombres a la lista
    nombre = "Juan"
    nombres.append(nombre)

    #borrar un nombre segun indice
    indice = None
    for i in range(len(nombres)):
        if "Juan" == nombres[i]:
            indice=i
    if indice != None:
        del nombres[indice]
    
    #Otra forma de borrar
    if "Juan" in nombres: 
        nombres.remove("Juan") #borra la primera aparicion
    
    #Insert: inserta un nombre en una posicion especifica
    nombres.insert(3, "Carlos")

    #Pop(): borra el ultimo elemento y lo devuelve
    nombres.pop()
    #POP por indice
    nombres.pop(3)

    #borrar todos los nombres
    nombres.clear()

    #index() busca y encuentra la posicion
    nombres.index("Juan") #ojo por si hay mas 1 juan

    #Count() cuenta los nombres iguales
    nombres.count("Juan")

    #Sort() ordena de menor a mayor
    nombres.sort()
    #Sort() de mayor a menor
    nombres.sort(reverse=True)

    #obtener el total de listas
    len(nombres)

    #Max() obtiene el mayor
    numeros: list[int]=[]
    max(numeros)

    #Min() obtieene el menor
    min(numeros)

    #Sum() suma todo los numeros de la lista
    sum(numeros)

    #Copia superficial
    numeros_copia: list[int]=[]
    numeros=numeros_copia.copy() #copia los elementos a la nueva lista
    
    