# https://youtu.be/otC1ddlFAsk

import pygame, sys
from configuraciones import *
from modo import *
from clases import Jugador, Suelo, Pantalla, Plataforma
from funciones import *



while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    actualizar_pantalla(pantalla, jugador, suelo, lista_plataformas)

    pygame.display.update()