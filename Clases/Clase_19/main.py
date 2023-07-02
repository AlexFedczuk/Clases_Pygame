# https://www.youtube.com/watch?v=WTRXYD1w4hs&list=PLE9qW09sJEPQBZx_WJM46jkrtlY9FFlxb&index=15

import pygame, sys
from configuraciones import *
from modo import *
from clases import Jugador, Suelo, Pantalla, Plataforma
from funciones import *

pygame.init()
RELOJ = pygame.time.Clock()

# Pantalla
pantalla = Pantalla(TAMANIO_PANTALLA, "Clases\Clase_18\Recursos\\fondo_de_pantalla.png")

# Personaje
jugador = Jugador(PERSONAJE_QUIETO_MIRANDO_DERECHA[0])

# Superficie
suelo = Suelo("Clases\Clase_19\Recursos\suelo\\2.png", (ANCHO_PANTALLA, 50), 0, ANCHO_PANTALLA, ANCHO_PANTALLA, 50, jugador)

# Plataforma
lista_plataformas = [
    suelo,
    Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 800, 700)
]

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F1:
                cambiar_modo()

    teclas_presionadas = pygame.key.get_pressed()

    if (teclas_presionadas[pygame.K_RIGHT] and jugador.rectangulo.colliderect(pantalla.rectangulo) and jugador.rectangulo.right != pantalla.rectangulo.right):# jugador.rectangulo.right < ANCHO_PANTALLA - jugador.velocidad_de_movimiento
        jugador.que_hace = "Derecha"
        jugador.ultima_direccion = "Derecha"
    elif (teclas_presionadas[pygame.K_LEFT] and jugador.rectangulo.colliderect(pantalla.rectangulo) and jugador.rectangulo.left != pantalla.rectangulo.left):
        jugador.que_hace = "Izquierda"
        jugador.ultima_direccion = "Izquierda"
    elif (teclas_presionadas[pygame.K_UP]):
        jugador.que_hace = "Salta"
    else:
        jugador.que_hace = "Quieto"

    actualizar_pantalla(pantalla, jugador, lista_plataformas)

    if get_mode():
        pygame.draw.rect(pantalla.pantalla, "Red", jugador.rectangulo, 2)
        pygame.draw.rect(pantalla.pantalla, "Blue", suelo.rectangulo, 2)
        for plataforma in lista_plataformas:
            pygame.draw.rect(pantalla.pantalla, "Yellow", plataforma.rectangulo, 2)

    pygame.display.update()