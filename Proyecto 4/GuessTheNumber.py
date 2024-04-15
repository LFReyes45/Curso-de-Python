# Hacer que el programa genere un número aleatorio del 1-100, el usuario solo tiene 8 intentos y debe realizar lo siguiente:
    # + Preguntar al usuario su nombre
    # + Generar un print de presentación que le de instrucciones al usuario
    # + Si el número excede estos limites, hacerle saber al usuario que ha gastado una oportunidad y que está fuera de los límites
    # + Si es menor el número,hacerle saber al usuario que se le falta para llegar
    # + Si es mayor, hacerle saber que se ha pasado
    # + Cuando acierte el número hacerle saber que ha ganado y cuántos intentos le ha tomado

# Mi código

from random import randint

secret_num = randint(1, 101)
get_it = False

name = input('Bienvenido jugador, ¿Cuál es tu nombre?\n')
print(f'Hola {name}, hemos pensado en un número entre el 1 y 100, tienes 8 intentos para acertar el número, solo se '
      f'aceptan números enteros\nEmpecemos el juego')

for i in range(8):
    user_num = input(f'Intento {i + 1}: ¿Cuál número crees que es? \t')
    if user_num.isdigit():
        user_try = int(user_num)
        if (user_try < 1) or (user_try > 100):
            print('Número fuera de los parámetros, has gastado una oportunidad erroneamente;)')
        elif user_try > secret_num:
            print('Te has pasado, vuelve a intentar más bajo')
        elif user_try < secret_num:
            print('Te ha faltado, vuelve a intentarlo con un número más alto')
        else:
            print(f'Correcto, lo has acertado, el número es {secret_num}, lo has logrado en {i + 1} intentos')
            get_it = True
            break
    else:
        print('No es un número entero')

if not get_it:
    print(f'La respuesta era: {secret_num}. Más suerte a la próxima')

# Solución del instructor
# from random import randint
#
# intentos = 0
# estimado = 0
# numero_secreto = randint(1,100)
# nombre = input("Dime tu nombre: ")
#
# print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")
#
# while intentos < 8:
#     estimado = int(input("Cuál es el número?: "))
#     intentos += 1
#
#     if estimado < numero_secreto:
#         print("Mi numero es mas alto")
#     elif estimado > numero_secreto:
#         print("Mi numero es mas bajo")
#     else:
#         print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
#         break
#
# if estimado != numero_secreto:
#     print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")