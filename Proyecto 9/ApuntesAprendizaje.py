# Modulos collections

from collections import Counter

    # numeros = [8, 6, 9, 5, 7, 4, 2, 4, 4, 1, 6, 6, 5, 8, 1, 9, 8]
    # print(Counter(numeros))
    # print(Counter('mississippi'))
    # frase = 'Al pan pan y al vino vino'
    # print(Counter(frase.lower().split()))
    #
    # serie = Counter([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4])
    # print(serie.most_common())            # Imprime en orden los valores más común
    # print(list(serie))

    # from collections import defaultdict
    #
    # # mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
    # # print(mi_dic['cuatro']) # Esto arrojaría error
    #
    # mi_dic2 = defaultdict(lambda: 'Nada')
    # mi_dic2['uno'] = 'verde'
    # print(mi_dic2['dos'])
    # print(mi_dic2) # Lo que hace el default dic es que crea valores si no existen en vez de arrojarnos error como tal
    #
    # from collections import namedtuple
    #
    # mi_tupla = (500,18,65)
    # print(mi_tupla[1])
    #
    # Persona = namedtuple('Persona',['nombre','altura','peso'])
    # ariel = Persona('Ariel',1.79,68)
    # print(ariel.altura)
    # print(ariel.peso)
    # print(ariel[0])

    # from collections import deque
    #
    # lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
    # lista_ciudades.append("Monterrey")
    # lista_ciudades.appendleft("Tokyo")
    # print(lista_ciudades)
    # lista_ciudades.pop()
    # lista_ciudades.popleft()
    # print(lista_ciudades)

# Modulos OS y Shutil

# import os
# archivos = open('curso.txt','w')
# archivos.write('texto de prueba')
# archivos.close()
# # os.unlink(os.getcwd()+'\\curso.txt')
# ruta = "C:\\Users\\luisf\\OneDrive\\Escritorio\\Carpeta_Superior"
#
#
# for carpeta, subcarpeta, archivo in os.walk(ruta):
#     print(f'En la carpeta {carpeta}')
#     print('Las subcarpetas son:')
#     for sub in subcarpeta:
#         print(f'\t {sub}')
#     print('Los archivos son: ')
#     for arc in archivo:
#            print(f'\t {arc}')
#     print()
# #
# import shutil
    #
    # shutil.move('curso.txt', "C:\\Users\\luisf\\OneDrive\\Escritorio")

# import send2trash
    # send2trash.send2trash('curso.txt')

# Modulo Datetime

# import datetime
    # mi_hora = datetime.time(17,35,50,150000)
    # mi_dia = datetime.date(2024, 4, 20)
    # print(type(mi_hora))
    # print(mi_hora)
    # print(mi_hora.minute)
    # print(mi_hora.hour)
    # print(type(mi_dia))
    # print(mi_dia)
    # print(mi_dia.year)
    # print(mi_dia.ctime())
    # print(mi_dia.today())

# from datetime import datetime

    # mi_fecha = datetime(2025,5,15,22,10,15,2500)
    # mi_fecha= mi_fecha.replace(month=11)
    # print(mi_fecha)
    # despierta = datetime(2022,10,5,7,30)
    # duerme = datetime(2022,10,5,23,45)
    # vigilia = duerme - despierta
    # print(vigilia)
    # print(vigilia.seconds)

# from datetime import date
    # nacimiento = date(2021,12,15)
    # defuncion = date(2087,1,1)
    #
    # vida = defuncion - nacimiento
    # print(vida)

# Modulos para medir el Tiempo (time y timeit)

# import time - no es lo suficientemente preciso
# import timeit - es muy preciso según las repeticiones que hagan
    # def prueba_for(numero):
    #     lista = []
    #     for num in range(1,numero+1):
    #         lista.append(num)
    #     return lista

    # def prueba_while(numero):
    #     lista = []
    #     contador = 1
    #     while contador <= numero:
    #         lista.append(contador)
    #         contador += 1
    #     return lista


    # inicio = time.time()
    # prueba_for(10)
    # final = time.time()
    # print(final-inicio)
    #
    # comienzo = time.time()
    # prueba_while(10)
    # fin = time.time()
    # print(fin-comienzo)

    # declaracion = '''
    # prueba_for(10)
    # '''
    # mi_setup ='''
    # def prueba_for(numero):
    #     lista = []
    #     for num in range(1,numero+1):
    #         lista.append(num)
    #     return lista
    # '''

    # duracion = timeit.timeit(declaracion, mi_setup, number = 10000000)
    # print(duracion)
    #
    # declaracion2 = '''
    # prueba_while(10)
    # '''
    # mi_setup2 ='''
    # def prueba_while(numero):
    #     lista = []
    #     contador = 1
    #     while contador <= numero:
    #         lista.append(contador)
    #         contador += 1
    #     return lista
    # '''
    #
    # duracion2 = timeit.timeit(declaracion2, mi_setup2, number = 10000000)
    # print(duracion2)

# Modulo math

# import math
    # resultado = math.ceil(89.6510)
    # resultado2 = math.floor(89.6510)
    # pai = math.pi
    # resultado3 = math.log(25,5)
    #
    # resultado4 = math.factorial(7)
    #
    # print(resultado)
    # print(resultado2)
    # print(pai)
    # print(resultado4)

# Modulo RE (Regular Expressions)

# • Carácteres especiales:
# car - descripción - ejemplo

# /d:       digito numérico                   - v\d.\d\d          (v1.02, v1.03, v2.01, v3.02)
# /w:       carácter alfanumérico             - \w\w\w-\w\w       (sol-do,abc-25,ABC-25,Nro-al)
# /s:       Espacio en blanco                 - número\s\d\d      (número 25, número 01, número 99, número 50)
# /D:       No numérico                       - \D\D\D\D          (abcd, AbCd, AB-C, abc?)
# /W:        No alfanumérico                   - \W\W\W            (+=- , ???, ¡*!, ###)
# /S:       No espacio en blanco              - \S\S\S\S          (1234, abcd, ¿si?, v.A1)

# • Cuantificadores:
# car - descripción - ejemplo

# +:        1 o más veces               - código_\d-\+      (código_5-5, código_5-555, código_1-02, código_9-95656)
# {n}:      se repite n veces           - \d-\d{4}          (1-0000, 1-2687, 5-6060, 8-0001)
# {n,m}:    se repite de n a m veces    - \w{3,5}           (hola, sol, mundo, yo256)
# {n,}:     desde n hacia arriba        - -\d{4,}-          (-11111111-, -52635-, -00524665988562256-, -00000-)
# *:        0 o más veces               - \w\s*\w           (a 2, a    b, fm, s4)
# ?:        1 o 0                       - casas?            (casa,casas)
# import re

    # texto = 'Si necesitas ayuda llama al (658)-589-9977 ñas 24 horas al servicio de ayuda online'
    # patron = 'ayuda'
    #
    # palabra = 'ayuda' in texto
    # print(palabra)
    #
    # busqueda = re.search(patron,texto)
    # print(busqueda)
    # print(busqueda.span())
    # print(busqueda.start())
    # print(busqueda.end())
    #
    # busqueda2 = re.findall(patron,texto)
    # print(busqueda2)
    # print(len(busqueda2))
    #
    # for hallazgo in re.finditer(patron,texto):
    #     print(hallazgo.span())

'''EJEMPLO 2'''
    # texto = "Llama al 562-654-7897 ya mismo"
    # patron = r'\d\d\d-\d\d\d-\d\d\d\d'
    # patron2 = r'\d{3}-\d{3}-\d{4}'
    # patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    #
    # buscar = re.search(patron,texto)
    # buscar2 = re.search(patron2,texto)
    # buscar3 = re.search(patron3,texto)
    #
    # # Formas de busqueda de patron
    # print(buscar)
    # print(buscar.group())
    #
    # # Es parecida al anterior solo simplificado el patron
    # print(buscar2)
    # print(buscar2.group())
    #
    # # Distinto a los demáss, ya que nos permite compilar el patron y obtener la posicion deseada dentro del patron
    # print(buscar3)
    # print(buscar3.group(1))
    # print(buscar3.group(2))
    # print(buscar3.group(3))

'''EJEMPLO 3'''
    # clave = input('Clave: ')
    # patron = r'\D{1}\w{7}'          # No puede empezar con un número y deben de ser más de 7 carácteres en total
    # checar = re.search(patron, clave)
    # print(checar)

'''EJEMPLO 4'''
    # texto = 'No atendemos los lunes por la tarde'
    # buscar = re.search(r'lunes|martes',texto)
    # print(buscar)
    #
    # buscar2 = re.search(r'....demos...',texto)
    # print(buscar2)
    #
    # buscar3 = re.search(r'^\D',texto) # El ^ verifica si un patron se encuentra al comienzo de un texto
    # print(buscar3)
    #
    # buscar4 = re.search(r'\D$', texto)  # El $ busca el final del texto
    # print(buscar4)
    #
    # buscar5 = re.findall(r'[^\s]',texto) # El usar el [^] son los patrones que deberá excluir
    # print(buscar5)
    #
    # buscar6 = re.findall(r'[^\s]+',texto) # Al usar el + es que repita una o más veces
    # print(buscar6)
    #
    # buscar7 = re.findall(r'[^\s]+',texto) # El usar el [^] son los patrones que deberá excluir
    # print(''.join(buscar7))

'''Actividad 1:'''
    # def verificar_email(email):
    #     patron = re.compile(r'(\w+)@(\w+)(\.com)')
    #     buscar = re.search(patron,email)
    #     if buscar == None:
    #         print("La dirección de email es incorrecta")
    #     else:
    #         print("Ok")

'''Actividad 2:'''
    # def verificar_saludo(frase):
    #     buscar = re.search(r'Hola+',frase)
    #     if buscar == None:
    #         print("No has saludado")
    #     else:
    #         print("Ok")

'''Actividad 3:'''
    # def verificar_cp(cp):
    #     patron = r'\w{2}\d{4}'
    #     buscar = re.search(patron,cp)
    #     if buscar == None:
    #         print("El código postal ingresado no es correcto")
    #     else:
    #         print("Ok")

# Comprimir y descomprimir archivos con zipfile y shutil

# Con zipfile

# import zipfile

    # mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w') #Crea el archivo comprimido pero vacío
    # mi_zip.write('mi_texto_A.txt')
    # mi_zip.write('mi_texto_B.txt')
    # mi_zip.close()

    # zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')
    # zip_abierto.extractall()  #extract() si requiere argumentos, nombre del archivo a descomprimir

# import shutil

    # carpeta_origen = "C:\\Users\\luisf\\OneDrive\\Escritorio\\Carpeta_Superior"
    # archivo_destino = 'Todo_Comprimido'
    # shutil.make_archive(archivo_destino,'zip',carpeta_origen)
    #
    # shutil.unpack_archive('Todo_Comprimido.zip','Carpeta_que_estaba_comprimida','zip')

