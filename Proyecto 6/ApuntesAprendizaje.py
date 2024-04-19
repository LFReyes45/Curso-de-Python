'''
E/S (I/O), algunas de las funciones para la modificacion de archivos de texto son:
    + abrir (open())
    + leer (read())
    + escribir (write())
    + cerrar (close())
'''

# Para modificar el archivo en variables
    # mi_archivo = open("prueba.txt")
    # print(mi_archivo.read())
    # una_linea = mi_archivo.readline()
    # print(una_linea.upper())
    #
    # una_linea = mi_archivo.readline()
    # print(una_linea.rstrip())
    #
    # una_linea = mi_archivo.readline()
    # print(una_linea)
    #
    # for l in mi_archivo:
    #     print(f"Aquí dice: {l}")
    # todas = mi_archivo.readlines()
    # todas = todas.pop()
    # print(todas)
    #
    # mi_archivo.close()

# Para modificar el archivo de origen

# Apertura de un archivo, modos de apertura 'open('archivo.txt','metodo_apertura')'
    # r - solo lectura, no modificaciones
    # w - solo escritura, si tiene algo el archivo borra por completo y reinicia
    # a - escritura pero al final del archivo o crea el archivo si no existe

    # mi_archivo = open('prueba.txt','w')
    # mi_archivo.write('''hola
    # mundo
    # aqui
    # estoy''')
    # lista = ['hola','mundo','aqui','estoy']
    # for i in lista:
    #     mi_archivo.writelines(i + '\n')
    # mi_archivo.write('Bienvenido')
    # mi_archivo.close()

# Modificaciones de archivos que esten en otros directorios
    # Algunos metodos importantes para esto son
        # + getcwd - get current work directory
        # + chdir - change directory
        # + makedirs - make directories
        # + dirname - al crear la ruta y en conjunto con el metodo path.dirname, obtiene el directorio
        # + basename - igual que el anterior pero obtiene el nombre del archivo al que hagas referencia
        # + split - obtiene los dos anteriores dividos en una tupla
        # + rmdir - remove directory

        # import os
        # otro_archivo = open('C:\\Users\\luisf\\PycharmProjects\\Curso-de-Python\\Proyecto 6\\Ejercicio_directorios\\pruebas_directorio.txt')
        # print(otro_archivo.read())

        # from pathlib import Path
        #
        # carpeta = Path('C:/Users/luisf/PycharmProjects/Curso-de-Python/Proyecto 6/Ejercicio_directorios') / 'pruebas_directorio.txt'
        # mi_archivo = open(carpeta)
        # print(mi_archivo.read())

# Pathlib

    # Algunos métodos que obtendremos con la libreria Pathlib son:
      #  + read_text() - leer el contenido del documento en el path
      #  + name - devuelve el nombre del archivo
      #  + suffix - devuelve el sufijo del nombre del archivo (.txt,.pdf)
      #  + stem - nombre del archivo sin la terminación
      #  + exists() - verifica la existencia del archivo


        # from pathlib import Path, PureWindowsPath
        #
        # carpeta = Path('C:/Users/luisf/PycharmProjects/Curso-de-Python/Proyecto 6/Ejercicio_directorios/pruebas_directorio.txt')
        #
        # ruta_windows = PureWindowsPath(carpeta)
        # print(f'La carpeta está en: {ruta_windows}')
        #
        # if not carpeta.exists():
        #     print('Este archivo no existe')
        # else:
        #     print('Genial, existe')

# Una de las clases de pathlib es Path, se usa para representar una ruta a un archivo o directorio en el archivero de
# nuestra computadora. Util para:
    # + crear o mover archivos,
    # + enumerar los archivos o
    # + crear rutas basadas en strings (puede transformar un string en rutas de acceso)

    # Algunas funciones para Path son:
        # + Path.home() - Obtiene la ruta absoluta a un directorio principal del usuario actual, sin será ruta relativa
        # + with_name - agrega otra guía que te manda al archivo que definas dentro
        # + parent - te permite obtener el padre inmediato de la ultima ubicación puesta
        # + relative_to() - es para recuperar una porcion de una ruta de archivos larga


    #from pathlib import Path #acepta strings como objetos preexistentes de path

    # base = Path.home()
    # guia = Path(base,"Europa","España",Path("Barcelona", "Sagrada_Familia.txt"))
    # guia2 = guia.with_name("La_Pedrera.txt")
    # print(guia, guia2)

    # guia = Path(Path.home(),"PycharmProjects/Curso-de-Python/Proyecto 6","Europa")
    #
    # for txt in Path(guia).glob("**/*.txt"):  #Esta linea se resume al final que buscará en todas
    #                                          # las carpetas y subcarpetas '**' a todos los archivos '*' que cumplan
    #                                          # con la coincidencia
    #     print(txt)

    # from pathlib import Path
    #
    # guia = Path('Europa','España','Barcelona','Sagrada_Familia.txt')
    # en_europa = guia.relative_to(Path("Europa"))
    # en_espania = guia.relative_to(Path("Europa","España"))
    # print(en_europa)
    # print(en_espania)

#Limpiar la consola
    # from os import system
    # nombre = input('Dime tu nombre: ')
    # edad = input('Dime tu edad: ')
    # system('cls')
    # print(f'tu nombre es {nombre} y tu edad es {edad} años')

# Archivos y funciones
