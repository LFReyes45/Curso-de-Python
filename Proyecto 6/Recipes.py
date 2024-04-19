import os
from pathlib import Path

directorio = Path.cwd() / 'Recetas'


def limpiar_consola():
    os.system('cls')


def numero_archivos():
    contador = 0
    for _ in directorio.glob('**/*.txt'):
        contador += 1
    return contador


def elegir_categoria(base):
    subcat = []
    var2 = True
    for i in base.iterdir():
        if i.is_dir():
            subcat.append(str(i.relative_to(base)))
    while var2:
        var = input(
            f'Estos son las carpetas que se encuentran en el recetario: {subcat} \n¿A cuál carpeta deseas acceder?\n').capitalize()
        if var in subcat:
            carpeta = Path(base, var)
            var2 = False
        else:
            print('No existe dicha carpeta\n')
    return carpeta


def elegir_receta(direccion):
    recetas = []
    var2 = True
    print('Las recetas con las que contamos son las siguientes:')
    for txt in Path(direccion).glob("**/*.txt"):
        recetas.append(txt.stem)
        print(f'•{txt.stem}')
    while var2:
        var = input('¿Cuál archivo quieres elegir? (procura escribir bien el nombre)\n')
        if var in recetas:
            direccion_extension = f'{direccion}/{var}.txt'
            var2 = False
        else:
            print('No existe dicho archivo\n')
    return direccion_extension


def crear_receta(direccion):
    nombre_archivo = input('¿Cómo se llama la receta que quieres agregar?\n')
    archivo = f'{direccion}/{nombre_archivo}.txt'
    creacion = open(Path(archivo), 'w')
    escritura = input('Escribe la receta que quieres agregar: \n')
    creacion.write(escritura)
    creacion.close()
    return 'Se ha escrito correctamente el archivo'


def crear_directorio(base):
    nuevo_directorio = input('¿Qué nueva carpeta quieres crear? \n')
    nueva = f'{base}/{nuevo_directorio}'
    Path.mkdir(Path(nueva))
    return 'Se ha creado correctamente el directorio'


def eliminar_receta(receta):
    Path.unlink(Path(receta))
    return f'Se ha eliminado correctamente el archivo \'{Path(receta).stem}\''


def eliminar_categoría(directorio):
    try:
        Path.rmdir(directorio)
    except OSError as e:
        print(f'No se pudo eliminar el directorio, ya que contenía archivos')
    return 'El proceso se ha completado'

print('Bienvenido al recetario, nos gustaría informarte primeramente de varias cosas')
print(f'\t•Actualmente el recetario se encuentra en: \n\t  →{directorio}')
print(f'\t•Y, este recetario, cuenta con: {numero_archivos()} recetas')

caso = 0

while caso != 6:
    caso = input('''\nElige de las siguientes opciones lo que deseas realizar:
        1. Mostrar contenido de una receta
        2. Crear nueva receta (dentro de una carpeta)
        3. Crear nueva categoría
        4. Eliminar receta
        5. Eliminar categoría
        6. Finalizar sistema\n→''')
    if caso.isdigit():
        caso_transf = int(caso)
        caso = caso_transf
        if 0 < caso <= 6:
            match caso:
                case 1:
                    categoria = elegir_categoria(directorio)
                    archivos = elegir_receta(categoria)
                    lectura = open(Path(archivos))
                    print(lectura.read())
                    input("Presiona cualquier tecla para continuar")
                    lectura.close()
                    pass
                case 2:
                    categoria2 = elegir_categoria(directorio)
                    creacion = crear_receta(categoria2)
                    print(creacion)
                    input("Presiona cualquier tecla para continuar")
                    pass
                case 3:
                    crear_categoria = crear_directorio(directorio)
                    print(crear_categoria)
                    input("Presiona cualquier tecla para continuar")
                    pass
                case 4:
                    print('El siguiente archivo que elijas será eliminado, en caso de querer detenerte sal del sistema')
                    buscar_carpeta = elegir_categoria(directorio)
                    buscar_archivos = elegir_receta(buscar_carpeta)
                    eliminar_recipe = eliminar_receta(buscar_archivos)
                    print(eliminar_recipe)
                    input("Presiona cualquier tecla para continuar")
                    pass
                case 5:
                    print('La siguiente carpeta que elijas será la eliminada, en caso de querer detenerte, sal del sistema')
                    buscar_categoria = elegir_categoria(directorio)
                    eliminar_directorio = eliminar_categoría(buscar_categoria)
                    print(eliminar_directorio)
                    input("Presiona cualquier tecla para continuar")
                    pass
        else:
            print('No está dentro de los parámetros')
        limpiar_consola()
    else:
        limpiar_consola()
        print('Elige un número, no una letra (Ej. 1,2,3,4,5,6)')
