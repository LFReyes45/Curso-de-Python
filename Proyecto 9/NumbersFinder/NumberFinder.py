# Empezamos importando la libreria de zipfile para poder visualizar los archivos
import time
# import zipfile
import os
import re
from datetime import date
import math

# archivocomprimido = zipfile.ZipFile('Proyecto+Dia+9.zip','r')
# archivocomprimido.extractall()
# archivo = open('Instrucciones.txt','r')
# print(archivo.read())

ruta = "C:\\Users\\luisf\\PycharmProjects\\Curso-de-Python\\Proyecto 9\\NumbersFinder\\Mi_Gran_Directorio"
patron = r'N\w{3}-\d{5}'


def sacar_fecha():
    fecha = date.today()
    print(f'Fecha de búsqueda: {fecha.__format__('%d-%m-%Y')}\n')


def obtener_patrones(ruta, patron):
    print('ARCHIVO\t\t\t\tNRO. SERIE')
    print('------------\t\t----------')
    contador = 0
    inicio = time.time()
    for carpeta, _, archivo in os.walk(ruta):
        for arch in archivo:
            ruta_completa = os.path.join(carpeta, arch)
            obtener = open(ruta_completa)
            texto = obtener.read()
            busqueda = re.search(patron, texto)
            if busqueda is None:
                pass
            else:
                print(f'{arch}\t\t{busqueda.group()}')
                contador += 1
    fin = time.time()
    tiempo = fin - inicio
    duracion = math.ceil(tiempo)
    print(f'\nNúmeros de serie encontrados: {contador}')
    print(f'Duración de la busqueda: {duracion} segundo(s)')


print('---------------------------------------')
sacar_fecha()
obtener_patrones(ruta, patron)
print('---------------------------------------')
