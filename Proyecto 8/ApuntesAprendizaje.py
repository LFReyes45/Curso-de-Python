# Instalar modulos y paquetes
# Usar pip install para instalar paquetes, ahora usaremos el PyPi. Tod0 esto desde el cmd, lo que hicimos fue:
    # pip install colored
    # python
    # from colored import fg, bg, attr
    # color = fg(1) + bg(15)
    # print(color+"Hola Mundo!"+attr(0))

# Modulos y paquetes
# Modulo: Cualquier codigo de Python guardado en un archivo .py (módulo = archivo."py"). Para importarlo es solor
#         ponerlo dentro de un import
# Paquetes: Son un grupo de modulos, es decir, es una carpeta que contiene varios modulos. Cada paquete debe contener
#           siempre un archivo "__init__.py" para que Python entienda de que se trata de un paquete

# Los ejemplos de esto último realizado se encuentran en las carpetas de Mi_Paquete (para los paquetes) y Mis_Modulos
# para los modulos

'''Manejos de Errores'''
# El manejo de errores puede hacerse gracias a tres palabras claves que son try (intentar → Intenta esto...),
# except (excepción → Si sale mal, haz esto...) y finally (finalmente → pase lo que pase, haz esto...). Sintaxis
    # try:
    #     # Código que queremos probar
    # except:
    #     # Código a ejecutar si hay error
    # else:
    #     # Código a ejecutar si no hay error
    # finally::
    #     # Código que se ejecutará de todos modos

'''EJEMPLO UNO'''
    # def suma():
    #     n1= int(input('Número 1: '))
    #     n2 = int(input('Número 2: '))
    #     print(n1+n2)
    #     print('Gracias por sumar')
    #
    # try:
    #     suma()
    # except TypeError:
    #     print('Tipos distintos concatenados')
    # except ValueError:
    #     print('Ese no es un número')
    # else:
    #     print('Hiciste alles bien')
    # finally:
    #     print('Eso fue alles')

'''EJEMPLO DOS'''
    # def pedir_numero():
    #     while True:
    #         try:
    #             numero = int(input('Dame un número'))
    #         except:
    #             print("Ese no es un número")
    #         else:
    #             print(f'Ingresaste el numero {numero}')
    #             break
    #
    #     print('Gracias')
    #
    # pedir_numero()

# Busqueda de Errores

# Herramientas de pruebas de código:
# •pyling: Es una biblioteca que analiza el código e informa sobre ciertos posibles problemas. Ya sea, problemas de
#          estilo o tal vez algún código no válido.
# •unittest: Biblioteca incorporada en Python que permitirá probar los programas y luego verificar si estás obteniendo
    #            los resultados deseados

    # Empezamos entonces con pylint, tras su instalación con pip install pylint, seguimos con el ejemplo:
        # def una_funcion():
        #     numero1 = 500
        #     print(numero1)
        #
        #
        # una_funcion()

    # Abrimos entonces el cmd para hacer el chequeo y solamente pondremos:
        # pylint .\BusquedaErrores.py -r y

# Seguimos entonces con la biblioteca integrada de unittest, todas las pruebas se realizaron en la carpeta de
    # ModulosPrueba, cosas importantes a destacar, se debe crear otro archivo para hacer las pruebas

# Decoradores: Son funciones que modifican el comportamiento de otras funciones y ayudan a acortar nuestro codigo. Ej.


    # def decorar_saludo(funcion):
    #
    #     def otra_funcion(palabra):
    #         print('Hola')
    #         funcion(palabra)
    #         print('Adios')
    #     return otra_funcion
    #
    #
    # def mayusculas (texto):
    #     print(texto.upper())
    #
    # def minusculas (texto):
    #     print(texto.lower())
    #
    #
    # mayuscula_decorada = decorar_saludo(minusculas)
    # mayuscula_decorada('Python')

'''Seguimos con los generadores'''

# Generadores: Son un tipo especial de funcion que en vez de devolvernos un valor terminado, va produciendose el valor
# poco a poco a medida que lo vayamos necesitando. Ej de un generador de numeros:

    # def crear_lista():
    #     lista = []
    #     for n in range(1,6):
    #         lista.append(n)
    #     return lista

# Ocupa más espacio en la memoria porque genera todos los números y ya eres tu el que los usa. Y una función generadora
# solo te da el número que requieres en el momento.

'''EJEMPLO'''
    # def mi_funcion():
    #     return 4
    #
    # def mi_generador():
    #     yield 4
    #
    # print(mi_funcion())
    # print(mi_generador())
    #
    # g = mi_generador()
    #
    # print(next(g))

'''SEGUNDO EJEMPLO'''

    # def mi_funcion():
    #     lista = []
    #     for x in range(1,5):
    #         lista.append(x*10)
    #     return lista

    # def mi_generador():
    #     for x in range(1,5):
    #         yield x*10

    # print(mi_funcion())
    # print(mi_generador())
    #
    # g = mi_generador()
    #
    # print(next(g))
    # print(next(g))
    # print(next(g))
    # print(next(g))

'''TERCER EJEMPLO'''
    # def mi_generador():
    #     x = 1
    #     yield x
    #
    #     x+=1
    #     yield x
    #
    #     x+=1
    #     yield x
    #
    # g = mi_generador()
    #
    # print(next(g))
    # print(next(g))
    #
    # print('HOLA MUNDO AOISJDNA SD09AOJSMD KH90IJAM SD90IAHKN SD')
    #
    # print(next(g))