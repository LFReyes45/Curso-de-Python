# Estas son las fases del reconocimiento facial
# 1 - Reconocimiento facial (reconocer una cara en la camara)
# 2 - Análisis facial (Captura la imagen del rostro y analiza distancias, tamaños, etc.)
# 3 - Convertir imagen en datos
# 4 - Buscar coincidencias

import cv2
import face_recognition as fr

# Cargar imagenes

foto_control = fr.load_image_file('FotoA.jpeg')
foto_prueba = fr.load_image_file('Empleados/Fernando Reyes.jpeg')

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# Localizar cara prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# enmarcar la cara
cv2.rectangle(foto_control,(lugar_cara_A[3],lugar_cara_A[0]),(lugar_cara_A[1],lugar_cara_A[2]),(0,0,255),2)
cv2.rectangle(foto_prueba,(lugar_cara_B[3],lugar_cara_B[0]),(lugar_cara_B[1],lugar_cara_B[2]),(0,0,255),2)

# Realizar comparacion
resultado = fr.compare_faces([cara_codificada_A],cara_codificada_B)

#Medida de la distancia
distancia = fr.face_distance([cara_codificada_A],cara_codificada_B)

# Mostrar resultado en cuadro
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,0,0),
            2)

# mostrar imagenes
cv2.imshow('Foto COntrol',foto_control)
cv2.imshow('Foto Prueba',foto_prueba)

# mantener el programa abierto
cv2.waitKey(0)