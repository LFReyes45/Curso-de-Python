# Métodos - Son funciones de los objetos. Permiten manipularlos, analizarlos, ejecutar acciones
# Las funciones nos permiten crear bloques de codigo que pueden ser facilmente ejecutados muchas veces y en distintos
# contextos sin necesidad de escribir constantemente el bloque entero.
# La sintaxis de la funcion es:
# def nombre_de_funcion (parámetros[ej, nombre]):

    # def saludar_personas(nombre):
    #     '''
    #     Esta función es
    #     para saludar a
    #     las personas
    #     '''
    #     print("Hola " + nombre)
    # saludar_personas("Fernando")

# return - sirve para devolver cosas, como resultados

    # def multiplicar(num1,num2):
    #     return num1*num2
    #
    # result = multiplicar(5,10)
    # print(result)

#Funciones dinámicas

    # def checar_3_cifras (lista):
    #     lista3 = []
    #     for i in lista:
    #         if i in range(100,1000):
    #             lista3.append(i)
    #         else:
    #             pass
    #     return lista3
    #
    # resultado = checar_3_cifras([555,99,600])
    # print(resultado)
    #
    # def suma_menores(lista_numeros):
    #     sum = 0
    #     for n in lista_numeros:
    #         if 0 < n < 1000:
    #             sum += n
    #         else:
    #             pass
    #     return sum
    #
    # lista_numeros = [5, 51, 45, 14, 51, 45, 51]
    #
    # print(suma_menores(lista_numeros))

# Ejemplos

    # precios_cafe = [('capuchino',1.50),('Expresso',2.2),('Moka',1.9)]
    #
    # def cafe_mas_caro(lista_precios):
    #     precios_mayor = 0
    #     cafe_mas_caro = ''
    #     for cafe,precio in lista_precios:
    #         if precio>precios_mayor:
    #             precios_mayor = precio
    #             cafe_mas_caro = cafe
    #         else:
    #             pass
    #     return (cafe_mas_caro,precios_mayor)
    #
    # cafe,precio = cafe_mas_caro(precios_cafe)
    #
    # print(f'El café más caro es \'{cafe}\' a ${precio}')


    # # Interacción entre funciones - Elige el palito
    # from random import shuffle
    #
    # # Lista incial
    # palitos = ['-','--','---','----']
    #
    # # Mezclar los palitos
    # def mezlcar(lista):
    #     shuffle(palitos)
    #     return lista
    #
    # # Solicitar al usuario que pida un numero
    # def suerte():
    #     tries = ''
    #     while tries not in ['1','2','3','4']:
    #         tries = input('Elige un número del 1 al 4: ')
    #     return int(tries)
    #
    # # Comprobar cual era el mas largo o corto
    # def comprobacion(lista,intento):
    #     if lista[intento - 1] == '-':
    #         print('Mala suerte;(')
    #     else:
    #         print('Que suerte')
    #     print(f'Has elegido el {lista[intento-1]}')
    #
    # palitos_mezclados = mezlcar(palitos)
    # seleccion = suerte()
    # comprobacion(palitos_mezclados,seleccion)

# *args
    # def suma(*args):
    #     total = 0
    #     for arg in args:
    #         total += arg
    #     return total
    #
    # print(suma(5,6,7))
    #
    # def suma_cuadrados(*args):
    #     total = 0
    #     for arg in args:
    #         total += arg**2
    #     return total
    #
    # print(suma_cuadrados(1,2,3))
    #
    # def suma_absolutos(*args):
    #     total= 0
    #     for arg in args:
    #         total += abs(arg)
    #     return total
    #
    # print(suma_absolutos(1,2,3,-4,5))

    # def numeros_persona(nombre,*args):
    #     suma = sum(args)
    #     return f'{nombre}, la suma de tus números es {suma}'
    #
    # name = "Luis Fernando"
    # valor = numeros_persona(name,34,343,3423)
    # print(valor)

#**kwargs 'Key words args'

    # def prueba(num1,num2,*args,**kwargs):
    #     print(f'el primer valor es {num1}')
    #     print(f'el segundo valor es {num2}')
    #
    #     for arg in args:
    #         print(f'arg = {arg}')
    #
    #     for clave,valor in kwargs.items():
    #         print(f'{clave} = {valor}')
    #
    # args = [100,300,400,200,800,100]
    # kwargs= {'x':'uno','y':'dos','z':'tres'}
    #
    # prueba(15,50,*args,**kwargs)

    # def cantidad_atributos(**kwargs):
    #     cont = 0
    #     for i in kwargs.items():
    #         cont+=1
    #     return cont
    #
    #
    # print(cantidad_atributos(x='uno',y='dos',z='tres'))

    # def lista_atributos(**kwargs):
    #     lista = []
    #     for i in kwargs.values():
    #         lista.append(i)
    #     return lista
    #
    #
    # print(lista_atributos(x='uno', y='dos', z='tres'))

    # def describir_persona(nombre,**kwargs):
    #     print(f'Características de {nombre}:')
    #     for ojos_pelo, color in kwargs.items():
    #         print(f'{ojos_pelo}: {color}')

    # from random import randint
    # # Obtener dos números al azar
    #
    # def lanzar_dados():
    #     dado1 = randint(1,7)
    #     dado2 = randint(1,7)
    #     return dado1,dado2
    #
    # def evaluar_jugada (resultado):
    #     suma = 0
    #     for i in resultado:
    #         suma+=i
    #     if suma <= 6:
    #         return(f"La suma de tus datos es {suma}. Lamentable")
    #     elif suma>=6 and suma<10:
    #         return(f"La suma de tus dados es {suma}. Tienes buenas chances")
    #     else:
    #         return(f"La suma de tus dados es {suma}. Parece una jugada ganadora")
    #
    # resultado = lanzar_dados()
    # print(evaluar_jugada(resultado))

    # def reducir_lista(lista):
    #     i=0
    #     while i < len(lista)-1:
    #         if lista[i] == lista[i+1]:
    #             lista.pop(i)
    #         else:
    #             i+=1
    #     lista.pop(-1)
    #     return lista
    #
    # def promedio (value):
    #     return (sum(value)/len(value))
    #
    # lista_numeros = [1, 2, 15, 7, 2, 8]
    # lista_numeros.sort()
    # value = reducir_lista(lista_numeros)
    # prom = promedio(value)
    #
    # print(value)
    # print(prom)

    # import random
    # def lanzar_moneda():
    #     moneda = ['Cara', 'Cruz']
    #     aleatorio = random.choice(moneda)
    #     return aleatorio
    #
    # def probar_suerte(result, lista):
    #     if result == 'Cara':
    #         lista = []
    #         print("La lista se autodestruirá")
    #         return lista
    #     else:
    #         print("La lista se salvó")
    #         return lista
    #
    #
    # lista_numeros = [2, 5, 8, 52, 4, 4, 1]
    # coin = lanzar_moneda()
    # suerte = probar_suerte(coin, lista_numeros)
    # print(suerte)