# https://www.youtube.com/watch?v=WTRXYD1w4hs&list=PLE9qW09sJEPQBZx_WJM46jkrtlY9FFlxb&index=15

import pygame, sys
from configuraciones import *
from modo import *
from clases import Jugador, Suelo, Pantalla
from funciones import *

pygame.init()
RELOJ = pygame.time.Clock()

# Pantalla
pantalla = Pantalla(TAMANIO_PANTALLA, "Clases\Clase_18\Recursos\\fondo_de_pantalla.png")

# Personaje
jugador = Jugador(PERSONAJE_QUIETO_MIRANDO_DERECHA[0])

# Superficie
suelo = Suelo(jugador.rectangulo)

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

    registrar_ingreso_teclas(teclas_presionadas, pantalla, jugador)

    actualizar_pantalla(pantalla, jugador, suelo)

    if get_mode():
        pygame.draw.rect(pantalla.pantalla, "Red", jugador.rectangulo, 2)
        pygame.draw.rect(pantalla.pantalla, "Blue", suelo.rectangulo, 2)

    pygame.display.update()