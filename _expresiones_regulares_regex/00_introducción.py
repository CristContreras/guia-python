"""
=============================================================================
                    INTRODUCCIÓN A EXPRESIONES REGULARES (REGEX)
=============================================================================

¿QUÉ SON LAS EXPRESIONES REGULARES?
------------------------------------
Las expresiones regulares (regex) son patrones que te permiten buscar, 
validar y manipular texto de forma inteligente. Es como un "buscador 
avanzado" para strings.

En lugar de buscar texto literal como "hola", puedes buscar PATRONES como:
- "cualquier número de teléfono"
- "todos los emails"
- "palabras que empiecen con mayúscula"
- "fechas en formato DD/MM/YYYY"

¿PARA QUÉ SIRVEN?
-----------------
✓ Validar datos (emails, teléfonos, contraseñas, DNI, etc.)
✓ Extraer información de textos (scraping, parsing)
✓ Reemplazar o modificar texto de forma inteligente
✓ Limpiar y normalizar datos
✓ Buscar patrones complejos en logs o archivos

EJEMPLOS DEL MUNDO REAL:
------------------------
• Google usa regex para buscar en millones de documentos
• Tu email filtra spam usando regex
• Los formularios web validan tu email/teléfono con regex
• Los editores de código hacen "buscar y reemplazar" con regex
• Los scrapers extraen datos de páginas web con regex

=============================================================================
                        CONCEPTOS BÁSICOS DE REGEX
=============================================================================
"""

import re

# ---------------------------------------------------------------------------
# 1. CARACTERES LITERALES - Buscar texto exacto
# ---------------------------------------------------------------------------
texto = "Me gusta Python y python es genial"

# Buscar la palabra "Python" (case sensitive)
print(re.search(r'Python', texto))  # Encuentra "Python"
print(re.search(r'python', texto))  # Encuentra "python" (minúsculas)

# La 'r' antes del string significa "raw string" (string crudo)
# Evita problemas con caracteres especiales como \n, \t, etc.


# ---------------------------------------------------------------------------
# 2. METACARACTERES - Caracteres con significado especial
# ---------------------------------------------------------------------------
"""
.   - Cualquier carácter (excepto salto de línea)
^   - Inicio de línea/texto
$   - Fin de línea/texto
*   - 0 o más repeticiones
+   - 1 o más repeticiones
?   - 0 o 1 repetición (opcional)
[]  - Conjunto de caracteres
{}  - Cantidad exacta de repeticiones
()  - Grupos de captura
|   - OR (o esto o aquello)
\   - Escapar caracteres especiales
"""

# Ejemplos:
print(re.search(r'h.la', 'hola'))     # Match: . es cualquier carácter
print(re.search(r'^Hola', 'Hola mundo'))  # Match: empieza con Hola
print(re.search(r'mundo$', 'Hola mundo')) # Match: termina con mundo


# ---------------------------------------------------------------------------
# 3. CLASES DE CARACTERES - Conjuntos predefinidos
# ---------------------------------------------------------------------------
"""
\d  - Cualquier dígito [0-9]
\D  - Cualquier NO dígito
\w  - Cualquier letra, número o guión bajo [a-zA-Z0-9_]
\W  - Cualquier NO letra/número/guión bajo
\s  - Cualquier espacio en blanco (espacio, tab, salto de línea)
\S  - Cualquier NO espacio en blanco
"""

texto = "Mi número es 555-1234 y mi edad es 30"

# Encontrar números
numeros = re.findall(r'\d+', texto)  # \d+ = uno o más dígitos
print(f"Números encontrados: {numeros}")  # ['555', '1234', '30']

# Encontrar palabras
palabras = re.findall(r'\w+', texto)
print(f"Palabras: {palabras}")


# ---------------------------------------------------------------------------
# 4. CUANTIFICADORES - Especificar cantidad de repeticiones
# ---------------------------------------------------------------------------
"""
*     - 0 o más veces
+     - 1 o más veces
?     - 0 o 1 vez (opcional)
{n}   - Exactamente n veces
{n,}  - n o más veces
{n,m} - Entre n y m veces
"""

# Ejemplos prácticos:
print(re.findall(r'\d{3}', '12 456 7890'))      # ['456', '789'] (grupos de 3)
print(re.findall(r'\d{2,4}', '1 23 456 7890'))  # ['23', '456', '7890']
print(re.findall(r'ho+la', 'hola hoola hooola')) # ['hola', 'hoola', 'hooola']
print(re.findall(r'colou?r', 'color colour'))    # ['color', 'colour']


# ---------------------------------------------------------------------------
# 5. CONJUNTOS [ ] - Definir tus propios grupos de caracteres
# ---------------------------------------------------------------------------

# [abc]    - a, b o c
# [a-z]    - Cualquier letra minúscula
# [A-Z]    - Cualquier letra mayúscula
# [0-9]    - Cualquier dígito
# [^abc]   - Cualquier carácter EXCEPTO a, b o c

texto = "Mi placa es ABC123 y mi código es XYZ789"

# Encontrar letras mayúsculas seguidas de números
placas = re.findall(r'[A-Z]{3}\d{3}', texto)
print(f"Placas: {placas}")  # ['ABC123', 'XYZ789']

# Encontrar vocales
vocales = re.findall(r'[aeiouAEIOU]', "Hola Mundo")
print(f"Vocales: {vocales}")  # ['o', 'a', 'u', 'o']


# ---------------------------------------------------------------------------
# 6. GRUPOS ( ) - Capturar y agrupar partes del patrón
# ---------------------------------------------------------------------------

# Los paréntesis permiten:
# 1. Capturar partes específicas del match
# 2. Aplicar cuantificadores a grupos
# 3. Usar referencias en reemplazos

texto = "Juan Pérez tiene 30 años"
match = re.search(r'(\w+) (\w+) tiene (\d+) años', texto)

if match:
    nombre = match.group(1)     # Juan
    apellido = match.group(2)   # Pérez
    edad = match.group(3)       # 30
    print(f"{nombre} {apellido}, {edad} años")

# Ejemplo: Extraer dominio de email
email = "usuario@ejemplo.com.ar"
match = re.search(r'@([\w.]+)', email)
print(f"Dominio: {match.group(1)}")  # ejemplo.com.ar


# ---------------------------------------------------------------------------
# 7. ALTERNANCIA | - OR lógico
# ---------------------------------------------------------------------------

# Buscar múltiples opciones
texto = "Tengo un perro y un gato"
mascotas = re.findall(r'perro|gato|conejo', texto)
print(f"Mascotas: {mascotas}")  # ['perro', 'gato']

# Validar extensiones de archivo
archivo = "documento.pdf"
if re.search(r'\.(pdf|docx?|txt)$', archivo):
    print("Formato válido")


# ---------------------------------------------------------------------------
# 8. ESCAPAR CARACTERES ESPECIALES - Usar \ para buscar literalmente
# ---------------------------------------------------------------------------

# Si quieres buscar . o * o + literalmente, debes escaparlos con \

texto = "El precio es $100.50"
# Buscar el punto literal y los números
precio = re.search(r'\$(\d+\.\d{2})', texto)
print(f"Precio: ${precio.group(1)}")  # 100.50

# Buscar asteriscos literales
texto2 = "Calificación: ***"
estrellas = re.findall(r'\*', texto2)
print(f"Estrellas: {len(estrellas)}")  # 3


# ---------------------------------------------------------------------------
# 9. ANCLAS - Posiciones en el texto
# ---------------------------------------------------------------------------

# ^  - Inicio del string
# $  - Final del string
# \b - Límite de palabra (word boundary)
# \B - NO límite de palabra

# Validar que un string SOLO contenga letras
print(re.match(r'^[a-zA-Z]+$', 'Hola'))      # Match
print(re.match(r'^[a-zA-Z]+$', 'Hola123'))   # None

# Buscar palabra completa "cat", no dentro de otras palabras
texto = "cat category scatter"
print(re.findall(r'\bcat\b', texto))  # ['cat'] (no encuentra "cat" en category)


# ---------------------------------------------------------------------------
# 10. PATRONES COMUNES - Ejemplos del mundo real
# ---------------------------------------------------------------------------

# EMAIL
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
email = "usuario@ejemplo.com"
if re.match(email_pattern, email):
    print("✓ Email válido")

# TELÉFONO ARGENTINO (ejemplos)
tel_pattern = r'^(?:\+54\s?)?(?:11|[2-9]\d{1,2})\s?\d{4}-?\d{4}$'
telefono = "+54 11 1234-5678"
if re.match(tel_pattern, telefono):
    print("✓ Teléfono válido")

# DNI ARGENTINO (7 u 8 dígitos)
dni_pattern = r'^\d{7,8}$'
dni = "12345678"
if re.match(dni_pattern, dni):
    print("✓ DNI válido")

# URL
url_pattern = r'^https?://[\w\.-]+\.\w+/?.*$'
url = "https://www.ejemplo.com/pagina"
if re.match(url_pattern, url):
    print("✓ URL válida")

# CÓDIGO POSTAL ARGENTINO
cp_pattern = r'^[A-Z]?\d{4}[A-Z]{0,3}$'
cp = "C1234ABC"
if re.match(cp_pattern, cp):
    print("✓ Código postal válido")


# ---------------------------------------------------------------------------
# 11. MODO VERBOSE - Regex más legibles con comentarios
# ---------------------------------------------------------------------------

# Para patrones complejos, usa re.VERBOSE para agregar comentarios
email_pattern_verbose = re.compile(r'''
    ^                    # Inicio del string
    [\w\.-]+             # Usuario: letras, números, puntos, guiones
    @                    # Arroba literal
    [\w\.-]+             # Dominio: letras, números, puntos, guiones
    \.                   # Punto literal
    \w+                  # Extensión: letras
    $                    # Fin del string
''', re.VERBOSE)

if email_pattern_verbose.match("test@ejemplo.com"):
    print("✓ Email válido (patrón verbose)")


# ===========================================================================
# RESUMEN: CHEAT SHEET RÁPIDO
# ===========================================================================
"""
BÁSICO:
  .       - Cualquier carácter
  ^       - Inicio
  $       - Final
  *       - 0 o más
  +       - 1 o más
  ?       - 0 o 1
  {n}     - Exactamente n veces
  {n,m}   - Entre n y m veces

CLASES:
  \d      - Dígito [0-9]
  \w      - Letra/número/_ [a-zA-Z0-9_]
  \s      - Espacio en blanco
  \D      - NO dígito
  \W      - NO letra/número/_
  \S      - NO espacio

CONJUNTOS:
  [abc]   - a, b o c
  [a-z]   - Rango a-z
  [^abc]  - Cualquier cosa excepto a, b o c

ESPECIALES:
  ( )     - Grupos de captura
  |       - OR (alternancia)
  \       - Escapar carácter especial
  \b      - Límite de palabra

FLAGS:
  re.IGNORECASE  - Ignorar mayúsculas/minúsculas
  re.MULTILINE   - ^ y $ funcionan por línea
  re.DOTALL      - . incluye saltos de línea
  re.VERBOSE     - Permite comentarios en el patrón
"""

# ===========================================================================
# CONSEJOS FINALES
# ===========================================================================
"""
1. Usa raw strings (r'...') siempre para evitar problemas con \
2. Prueba tus regex en regex101.com o pythex.org
3. Empieza simple y ve agregando complejidad
4. Los regex son "codiciosos" por defecto (.*), usa .*? para no-codicioso
5. Compila patrones que uses múltiples veces con re.compile()
6. No abuses de regex: para cosas simples usa .split() o .replace()
"""