# Es un analizador de texto, el cual deberá
#     Solicitar al usuario que ingrese un texto
#     Que ingrese tres letras a su elección
#     Realizar estos 5 análisis
#         1. ¿Cuántas veces aparece cada una de las letras que eligió?
#         2. ¿Cuantas palabras hay a lo largo del texto?
#         3. ¿Cuál es la primera y última letra del texto?
#         4. ¿Cómo quedaría el texto si invirtieramos el orden de las palabras?
#         5. Buscar la palabra Python dentro del texto

# Mi solución

import getpass

usuario = getpass.getuser()

# Presentación
print(f"Hola y bienvenido {usuario.capitalize()}")

# Se solicita el texto que se analizará
# Además de que se transforma en minusculas y se limpia el texto dejandolo sin espacios al inicio ni al final
text = input("¿Qué texto deseas análizar?")
text_lower = text.lower()
text_clean = text_lower.strip()

# Se separa el texto según el espacio de delimitador y se elimina si la ultimo colocado es un punto separado del texto
num_palabras = text_clean.split(" ")
if num_palabras[::-1] == ".":
    num_palabras.pop()

# Se crea una varible de lista para almacenar las palabras a buscar
lista = []

# Se realiza un bucle que solicita tres palabras y se van agregando a una lista
for i in range(3):
    solicitud = input("¿Qué letras deseas buscar?")
    lista.append(solicitud.lower())

# Se imprimen las palabras o letras que se quieren buscar y la cantidad de ocasiones en las que aparece
for i in range(3):
    print(f"La palabra {lista[i]} se encontró {text_clean.count(lista[i])} veces en el texto proporcionado")

# Se imprimen el número de palabras, la primera y última
print(f"\nMencionar además que hay {len(num_palabras)} palabras en el texto")
print(
    f"Siendo que \"{num_palabras[0]}\" es la primera palabra y \"{num_palabras[-1]}\" es la última del texto ingresado")

# Se revierte el texto tanto por palabra (uniendolo despues mediante un join) como por letra
reverse_text = num_palabras[::-1]
joined = " ".join(reverse_text)
print(f"\nAlgo curioso, el texto inverso quedaría como: {joined}")
print(f"O bien, algo más loco: {text_clean[::-1]}")

# Se realiza una busqueda de la palabra Python en el texto (no importa si tiene mayusculas ya que ya esta en minusculas)
# el texto, esto mediante una condicional que almacena una variable booleana y si es positivo lo afirma y si no lo niega
var = ""
Busqueda = "python" in text_clean
if Busqueda:
    var = "SI"
else:
    var = "NO"

print(f"\nLa palabra Python {var} se encuentra en el texto")

# Solución del instructor

    # texto = input("Ingresa un texto a elección: ")
    # letras = []
    #
    # texto = texto.lower()
    #
    # letras.append(input("Ingresa la primera letra: ".lower()))
    # letras.append(input("Ingresa la segunda letra: ".lower()))
    # letras.append(input("Ingresa la tercera letra: ".lower()))
    #
    # print("\n")
    # print("CANTIDAD DE LETRAS")
    # cantidad_letras1 = texto.count(letras[0])
    # cantidad_letras2 = texto.count(letras[1])
    # cantidad_letras3 = texto.count(letras[2])
    #
    # print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
    # print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
    # print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")
    #
    # print("\n")
    # print("CANTIDAD DE PALABRAS")
    # palabras = texto.split()
    # print(f"Hemos encontrado {len(palabras)} palabras en tu texto")
    #
    # print("\n")
    # print("LETRAS DE INICIO Y DE FIN")
    # letra_inicio = texto[0]
    # letra_final = texto[-1]
    # print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")
    #
    # print("\n")
    # print("TEXTO INVERTIDO")
    # palabras.reverse()
    # texto_invertido = ' '.join(palabras)
    # print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")
    #
    # print("\n")
    # print("BUSCANDO LA PALABRA PYTHON")
    # buscar_python = 'python' in texto
    # dic = {True: "sí", False: "no"}
    # print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
