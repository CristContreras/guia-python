# ============================================================================
# 1. re.search() - Busca la PRIMERA coincidencia en cualquier parte del texto
# ============================================================================
# Cuándo usar: Cuando necesitas verificar SI existe un patrón en el texto
# Devuelve: Un objeto Match o None

import re

def ejemplo1():
    
    texto = "Mi número es 12345"
    patron = r"\d+"  #si el texto tiene numeros 0-9 consecutivos indicados por el +
    #resultado = re.search(r"\d+", texto) # \d+ = uno o más dígitos
    resultado = re.search(patron, texto) #otra forma mas ordenada
    if resultado:
        print(resultado.group()) #devuelve string de lo encontrado
        
def ejemplo2():
    texto = "Mi email es juan@gmail.com y mi teléfono es 555-1234"
    resultado = re.search(r"\d{3}-\d{4}", texto)
    if resultado:
        print(f"Encontrado: {resultado.group()}")
        print(f"Posicion: {resultado.start()}-{resultado.end()}")
              
def main():
    ejemplo1()

if __name__=="__main__":
    main()