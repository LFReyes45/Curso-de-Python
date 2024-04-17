'''
El juego es el ahorcado, el programa elegirá una palabra secreta, y le mostraremos al usuario solamente los guiones,
que son la cantidad de letras de la palabra. El jugador deberá elegir una letra y si se encuentra, el sistema mostrará
las posiciones en las que se encuentra. Pero si no pierde una vida.

El jugador contará con 6 vidas y le iremos descartando vidas cada que se equivoque. Si se agotan antes de terminar,
el jugador perderá, en caso contrario ganará.
    • Primero, ocupamos un código que implemente el código choice para que el sistema pueda elegir una palabra al azar
    • Segundo, se pueden crear tantas funciones se crean necesarias
    • Por último, escribir primero las funciones y luego el código (tip)
'''
from random import choice

vidas = 6


# Primero se crea la palabra secreta mediante el método de choice
def palabra_secreta():
    palabras = ["computadora", "escritorio", "mesa", "silla", "cable"]
    secreta = choice(palabras)
    return secreta


# Reemplazar todos los carácteres por _ en la cadena
def hacer_lista(kwpass):
    lista = list(palabra)
    return lista


def no_mostrado(kwpass2):
    hidden_word = []
    for i in range(len(kwpass2)):
        hidden_word.append('_')
    return hidden_word


def intentos():
    letra = ''
    while len(letra) != 1 and not letra.isdigit():
        letra = input('¿Qué letra quieres intentar? ;)\n').lower()
    return letra


def comprobacion(letra, palabra, ocultar):
    global vidas
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                ocultar[i]=letra
    else:
        print('No se encuentra tu palabra -1 ♥')
        vidas = vidas - 1
        return vidas
    return ocultar


palabra = palabra_secreta()
cambio = hacer_lista(palabra)
ocultar = no_mostrado(cambio)

print(f"Bienvenido al ahorcado, empecemos entonces con el juego, tienes 6 ♥ vidas \n "
      f"y tu palabra es la siguiente: \n{ocultar}")
while '_' in ocultar:
    letra = intentos()
    checo = comprobacion(letra,cambio,ocultar)
    print(checo)
    if vidas == 0:
        print('Mala Suerte se te acabaron las vidas')
        break
if '_' not in ocultar:
    print(f'\nFelicidades!!, hemos terminado el juego, la palabra era {palabra}')