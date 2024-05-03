import pygame
import random
import math
from pygame import mixer
import io

# Se inicializa la libreria
pygame.init()

# Creamos la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e iconos
pygame.display.set_caption("Attack on Aliens")
icono = pygame.image.load("juego.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('Galaxy.jpg')

# Agregar música
mixer.music.load('Musica.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Variables del prota
img_jugador = pygame.image.load("astronave.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("ovni.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(50)

# Variables de la bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0.4
bala_y_cambio = 3
bala_visible = False


def fuentes_bytes(fuente):
    with open(fuente, 'rb') as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)


# Variable para puntaje
puntaje = 0
fuente = pygame.font.Font("zephyr_jubilee.ttf", 32)
texto_x = 10
texto_y = 10

# texto final del juego
fuente_final = pygame.font.Font("zephyr_jubilee.ttf", 40)


# Funciones del juego

# Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Función disparar la bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Detectar si hay colisiones
def colisiones(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Funcion del puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion del final del juego

def texto_final():
    mi_fuente_final = fuente_final.render(('JUEGO TERMINADO'), True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


# Loop que mantendrá la pantalla activa
se_ejecuta = True
while se_ejecuta:

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # Iterar los eventos
    for evento in pygame.event.get():

        # Condicional por si se cierra la pantalla
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Condicionales para checar si se presiona o suelta una tecla y cuál
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('Disparo.mp3')
                sonido_bala.set_volume(0.3)
                sonido_bala.play()
                nueva_bala = {
                    'x': jugador_x,
                    'y': jugador_y,
                    'velocidad': -5
                }
                balas.append(nueva_bala)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Se realiza la suma del jugador dandole movimiento, modificando posicion del jugador
    jugador_x += jugador_x_cambio

    # Prevenir a que no salga la nave de la pantalla
    if jugador_x <= 0:
        jugador_x_cambio = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Se realiza la suma del jugador dandole movimiento, modificando posicion del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Prevenir a que no salga el enemigo de la pantalla
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.4
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.4
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colisiones
        for bala in balas:
            choque = colisiones(enemigo_x[e], enemigo_y[e], bala['x'], bala['y'])
            if choque:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.set_volume(0.1)
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)
        enemigo(enemigo_x[e], enemigo_y[e], e)

    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    # Hacer la bala persistente
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Llamada de las funciones
    jugador(jugador_x, jugador_y)

    # Mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar pantalla
    pygame.display.update()
