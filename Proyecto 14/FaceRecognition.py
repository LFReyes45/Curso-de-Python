import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Crear base de datos de la cara
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

# Codificar imagenes
def codificar(imagenes):
    # crear lista nueva
    lista_codificada = []

    #pasar por todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

        # devolver lista codificada
    return lista_codificada


# Registrar los ingresos
def registrar_ingresos(persona):
    f = open('registro.csv','r+')
    lista_datos = f.readlines()
    nombre_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombre_registro.append(ingreso[0])
    if persona not in nombre_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona},{string_ahora}')

lista_empleados_codificada = codificar(mis_imagenes)

# tomar una imagen de camara web
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Leer imagen de la camara
exito,imagen = captura.read()

if not exito:
    print('No se pudo tomar la captura')
else:
    #reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    # Codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen,cara_captura)

    # Buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada,cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada,caracodif)
        distancias = fr.face_distance(lista_empleados_codificada,caracodif)

        indice_coincidencia = numpy.argmin(distancias)

        #mostrar coincidencias

        if distancias[indice_coincidencia]>0.4:
            print('No coincide con ningún empleado')
        else:
            #Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]
            y1,x2,y2,x1 = caraubic
            cv2.rectangle(imagen,(x1,y1),(x2,y2),(255,0,0),2)
            cv2.rectangle(imagen,(x1,y2-35),(x2,y2),(255,0,0),cv2.FILLED)
            cv2.putText(imagen,nombre,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

            registrar_ingresos(nombre)

            #Mostrar la imagen obtenida
            cv2.imshow('Imagen web',imagen)

            #Mantener ventada abierta
            cv2.waitKey(0)

