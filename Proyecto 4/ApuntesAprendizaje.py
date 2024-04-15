# Operadores de comparación:
#     • Mayor           >
#     • Menor           <
#     • Mayor o igual   >=
#     • Menor o igual   <=
#     • Igual           ==  //Nota. No es igual "=" (asignacion) que "==" (Comparacion"
#     • Diferente       !=

# Igualdad
    # mi_bool = 'blanco' == 'BLANCO'.lower()
    # bool2 = 100 == 100.0
#
# Diferencia
    # mi_bool = 100!=99
    #
# Mayor y Menor
    # mi_bool = 5>=5
    # bool2 = 6<7

# Operadores lógicos:
    # • and
    # • or
    # • not

        # mi_bool = (55 == 55) and ('Perro' == 'perro')
        # mi_bool = (55 == 55) or ('Perro' == 'perro')
        # mi_bool = (55 == 55) and ('Perro' == 'perro')
        #
        # texto = "Esta frase es breve"
        # mi_bool = ('frase' in texto) or ('python' in texto)
        # print(mi_bool)
        #
        # mi_bool = not ('a' == 'a')
        # print(mi_bool)

# Codicionales / Toma de Decisiones
    # • if
    # • elif
    # • else

        # x = True
        # if 5 == 2:
        #     print('Es correcto')
        # else:
        #     print('No es correcto')

        # mascota = 'perro'
        # if mascota == 'gato':
        #     print('Tienes un gato')
        # elif mascota == 'perro':
        #     print('Tienes un perro')
        # else:
        #     print('No se qué animal tienes')

        # edad = 16
        # calificacion = 9
        # if edad < 18:
        #     print('Eres menor de edad')
        #     if calificacion >= 7:
        #         print('Aprobado')
        #     else:
        #         print('No aprobado')
        # else:
        #     print('Eres adulto')

# Loops (Bucles)
    # Loop for, sintaxis
        # for [n] in lista:
        #     imprimir ["x"]

        # lista = ['a','b','c','d']
        #
        # for letra in lista:
        #     print("Letra: " + letra)
        #
        # numeros = [1,2,3,4,5]
        # mi_valor = 0
        #
        # for numero in numeros:
        #     mi_valor += numero
        # print(mi_valor)

        # for a,b in [[1,2],[3,4],[5,6]]:
        #     print(a)
        #     print(b)
        #
        # lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
        # suma_pares = 0
        # suma_impares = 0
        #
        # for suma in lista_numeros:
        #     if(suma%2 == 0):
        #         suma_pares+=suma
        #     elif(suma%2 == 1):
        #         suma_impares+=suma
        #
        # print(suma_pares)
        # print(suma_impares)

    # Loop While sintaxis:
        # while (condicion):
        #     Código
        # else:
        #     Otro_código

        # monedas = 5
        # while monedas>0:
        #     print(f"Tienes {monedas} monedas")
        #     monedas -=  1
        # else:
        #     print("Se acabó el dinero")

        # respuesta = 's'
        #
        # while respuesta == 's':
        #     respuesta=input('¿Quieres seguir? s/n')
        # else:
        #     print('Gracias')
        #
        # nombre = input('Ingresa tu nombre: ')

        # for letra in nombre:
        #     if letra == 'r':
        #         break
        #     print(letra)
        #
        # for letra in nombre:
        #     if letra == 'r':
        #         continue
        #     print(letra)

        # numero = 50
        #
        # while numero >= 0:
        #     if numero % 5 == 0:
        #         print(numero)
        #     else:
        #         pass
        #     numero -= 1

    # Rango
        # for numero in range(20,31,2):
        #     print(numero)

        # lista = list(range(1,101))
        # for rango in lista:
        #     print(rango)

        # Es uno de los ejercicios encargados por parte del instructor
        # suma_cuadrados = 0
        #
        # for rango in list(range(1,16)):
        #     rango **= 2
        #     suma_cuadrados += rango
        #
        # print(suma_cuadrados)

    # Enumerador
        # lista = ['a','b','c']
        # for i in enumerate(lista):
        #     print(i)
        #
        # mis_tuples= list(enumerate(lista))
        # print(mis_tuples[0][1])

        # lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
        #
        # for nombres in enumerate(lista_nombres):
        #     print(f'{nombres[1]} se encuentra en el índice {nombres[0]}')
        # lista_indices = list(enumerate("Python"))
        # print(lista_indices)

        # lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
        # lista = list(enumerate(lista_nombres))
        #
        # for i in lista:
        #     if i[1].startswith("M"):
        #         print(i[0])
        #     else:
        #         pass

    # zip
        # nombres = ['Ana','Hugo','Valeria']
        # edades = [69,29,42]
        # ciudades = ['Lima','Madrid','Mexico']
        #
        # comb = list(zip(nombres,edades,ciudades))
        #
        # for nombre,edad,ciudad in comb:
        #     print(f"{nombre} tiene {edad} años y vive en {ciudad}")
    # Min y Max
        # lista = [51,54,87,62,41]
        # print(f'El menor es {min(lista)} y el mayor es {max(lista)}')
        #
        # nombre = ['juan','Pablo','alicia','Carlos']
        # print(min(nombre))
        #
        # dic = {'c1':21,'c2':32}
        # print(min(dic.values()))

    # Random
        # from random import *
        # aleatorio = randint(1,100)
        # print(aleatorio)
        #
        # aletorio2 = round(uniform(1,5),1)
        # print(aletorio2)
        #
        # aleatorio3 = random()
        # print(aleatorio3)
        #
        # colores = ['azul','rojo','verde','amarillo']
        # aleatorio4 = choice(colores)
        # print(aleatorio4)
        #
        # numeros = list(range(5,50,5))
        # shuffle(numeros)
        # print(numeros)

    # Comprension de listas
        # letra = [n if n*2 > 10 else 'no' for n in range(0,21,2)]
        #
        # print(letra)
        # pies = [10,20,30,40,50]
        # metros = [n/3.281 for n in pies]
        # print(metros)
        #
        # valores = [1, 2, 3, 4, 5, 6, 9.5]
        # valores_pares = [n for n in valores if n%2 == 0 ]
        # print(valores_pares)
    # Match (switch)
        # serie = 'N-02'
        # match serie:
        #     case 'N-01':
        #         print('Samsung')
        #     case 'N-02':
        #         print('Nokia')
        #     case 'N-03':
        #         print('Motorola')
        #     case _:
        #         print('No existe este producto')

        # cliente = {'nombre':'Fernando',
        #            'edad': 22,
        #            'ocupacion': 'aprendiz'}
        #
        # pelicula = {'titulo': 'Matrix',
        #             'ficha_tecnica': {'protagonista': 'Keanu Reeves','director': 'Lana y Lilly'}}
        #
        # elementos = [cliente,pelicula,'libros']
        #
        # for e in elementos:
        #     match e:
        #         case {'nombre':nombre,
        #               'edad':edad,
        #               'ocupacion':ocupacion}:
        #             print('Es un cliente')
        #             print(nombre,edad,ocupacion)
        #         case{'titulo':titulo,
        #              'ficha_tecnica': {'protagonista':protagonista,'director':director}}:
        #             print('Esto es una pelicula')
        #             print(titulo,protagonista,director)
        #         case _:
        #             print('No se qué es esto')
