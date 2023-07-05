# https://youtu.be/otC1ddlFAsk

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
    Plataforma((200, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 800, 800),
    Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 1050, 705),
    Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 800, 650),
    Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 500, 650),
    Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 300, 520)
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

    # Identificacion de teclas ingresadas en los eventos.
    identificar_input(teclas_presionadas, pantalla, jugador)
    # Funcion donde se realiza la logica del juego.
    actualizar_pantalla(pantalla, jugador, suelo, lista_plataformas)

    if get_mode():
        dibujar_rectangulos(pantalla, jugador.diccionario_rectangulos, "Red", 2)
        for plataforma in lista_plataformas:
            dibujar_rectangulos(pantalla, plataforma.diccionario_rectangulos, "Yellow", 2)
        dibujar_rectangulos(pantalla, suelo.diccionario_rectangulos, "Blue", 2)

    pygame.display.update()