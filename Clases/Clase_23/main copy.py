# https://youtu.be/otC1ddlFAsk

import pygame, sys
from configuraciones import *
from modo import *
from clases import Jugador, Suelo, Pantalla, Plataforma
from funciones import *
from niveles.nivel_uno import NivelUno

# Pantalla 
WIDHT, HEIGHT = 1900
TAMANIO_PANTALLA = (WIDHT, HEIGHT)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)
nivel_actual = NivelUno(PANTALLA)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    nivel_actual.update(eventos)
    pygame.display.update()