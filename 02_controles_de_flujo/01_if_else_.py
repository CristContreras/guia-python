def main():
    pass  #borrar y poner una funcion a ejecutar

# -------------------------
# Forma 1: básica
# -------------------------
def if_basico():
    edad = 18
    if edad>=18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

# -------------------------
# Forma 2: if-elif-else
# -------------------------
def if_elif():
    nota = 7
    if nota >= 9:
        print("Excelente")
    elif nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


# -------------------------
# Forma 3: operador ternario
# -------------------------
def if_ternario():
    edad = 20
    mensaje = "Mayor" if edad >= 18 else "Menor"
    print(mensaje)


# -------------------------
# Forma 4: if en una línea
# -------------------------
def if_en_linea():
    x = 10
    if x > 5: print("x es mayor que 5")


# -------------------------
# Pruebas
# -------------------------
if __name__ == "__main__":
    if_basico()
    if_elif()
    if_ternario()
    if_en_linea()