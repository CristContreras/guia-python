import datetime

def main():
    ej5()

def ej1():
    #Obtiene y muestra la fecha actual
    hoy = datetime.date.today()
    print(hoy)

def ej2():  
    #Crea una fecha y la muestra
    fecha1 = datetime.date(2025,1,20)
    print(fecha1)

def ej3():
    #obtiene y muestra la fecha con hora actual y modificada
    ahora = datetime.datetime.now() # devuelve con microsegundos
    print(ahora)
    ahora_modificado = datetime.datetime.now().replace(microsecond=0)
    print(ahora_modificado)

def ej4():
    #Calcula los dias pasados entre dos fechas
    fecha_creada = datetime.date(2025,1,10)
    fecha_actual = datetime.date.today()
    diferencia = fecha_actual-fecha_creada
    print("Pasaron: ", diferencia.days , "días")

    meses = fecha_actual.month-fecha_creada.month
    if fecha_actual.day < fecha_creada.day:
        meses -= 1
    if meses < 0:
        meses += 12
    print("Pasaron" , meses, "meses")

    anios = fecha_actual.year - fecha_creada.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_creada.month, fecha_creada.day):
        anios -= 1
    print("Pasaron", anios, "años")

def ej5():
    #Muestra la hora unicamente
    ahora = datetime.datetime.now()
    hora_actual = ahora.time().replace(microsecond=0)
    print("Hora actual", hora_actual)

if __name__=="__main__":
    main()