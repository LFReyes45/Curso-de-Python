# Tipos de datos:
#   string (str): Cadenas de texto
#   integer(int): Numeros enteros
#   floating(float): numeros decimales
#   listas(list): Listas de palbras [0,n]
#   diccionarios(dic): Panel de palabras agrupadas Ej. {'arte':'cine','color':'rojo'}
#   tuples (tuple): Parecidos a las listas pero con orden inmutable
#   sets(set): Conjunto ordenado de elementos unicos e irrepetibles
#   booleanos(bool): Para decisiones true or false

# Convenciones para llamar a las variables:
    # 1. Legible
    # 2. Una sola unidad (nombre_de_estudiante)
    # 3. hispanismos (años sería anios y quitar acentos)
    # 4. números, deben inciar con una letra no numeros
    # 5. signos no pueden contener signos
    # 6. nada de palabras reservadas

# Funciones adicionales
    # 'type()': Función para ver el tipo de datos de cierta variable
    # 'format()': Reemplaza a los valores que estan contenidos en las variables por llaves vacías, abajo un ejemplo
    # 'round()': Es para redondear numeros escribiendo el primer parámetro como valor y el segundo como número de ceros

# Para cambiar los tipos de datos se realiza el casting:
#   Implicito: En este tipo, Python convierte el tipo de datos en otro tipo de datos automáticamente. El usuario no debe
#              hacer nada.
#   Explicito: Python necesita que el usuario haga algo para convertir un tipo de dato en otro.

# Ejemplo de implicta
#     num1 = 20
#     num2 = 30.5
#     num1 = 20 + 30.5
#
#     print(type(num1))
#     print(type(num2))

# Ejemplo de explicita
#     num3 = 5.8
#     print(num3)
#     print(type(num3))
#
#     num4 = int(num3)
#     print(num4)
#     print(type(num4))

#   edad = int(input("Dime tu edad: "))
#   nueva_edad = 1+ edad
#   print(nueva_edad)

# Formatear cadenas, para ello podemos utilizar la función format o bien:
    # Cadenas literales: En estas solo hay que insertar una f dentro del parentesis y el nombre de las variables dentro de
    # corchetes.

    # x=10
    # y=5

# Primera manera:
    # print("Mis numeros son: "+ str(x) +" y " + str(y))

# Segunda manera:
    # print("Mis numeros son {} y {}".format(x,y))
    # print("La suma de {} y {}, es igual a {}".format(y,x,x+y))

# Tercera manera:
    # color = "rojo"
    # matricula = 12312312
    # print(f"El color del auto es {color} y el número de matricula es {matricula}")

# Operadores Básicas:
    # x=6
    # y=2
    # z=7
    # print(f"{x} más {y} es igual a: {x+y}")
    # print(f"{x} menos {y} es igual a: {x-y}")
    # print(f"{x} por {y} es igual a: {x*y}")
    # print(f"{x} entre {y} es igual a: {x/y}")

# Divison al piso (solamente devolver el entero):
    # print(f"{z} dividido al piso de {y} es igual a {z//y}")

# Modulo, devuelve el resto de una division (7/2 -> queda una unidad por lo que devuelve uno)
    # print(f"{z} modulo de {y} es igual a {z%y}")

#Potencia
    # print(f"{x} elevado a la {y} es igual a {x**y}")
    # print(f"{y} elevado a la {x} es igual a {y**x}")

#Raíz cuadrada
    # print(f"La raíz cuadrada de {x} es {x**0.5}")
    # print(f"La raíz cuadrada de {8} es {8**0.3333334}")

# Redondeo round(value,number_of_zeros)
    # valor = round(95.6666667)
    # print(valor)
    # print(type(valor))

    # num1=round(13/2)
    # print(type(num1))