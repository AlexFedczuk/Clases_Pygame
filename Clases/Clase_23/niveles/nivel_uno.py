import pygame
from pygame.locals import *

from niveles.configuraciones import *
from niveles.modo import *
from niveles.class_personaje import *
from niveles.nivel import *
from niveles.class_plataforma import *

class NivelUno(Nivel):
    def __init__(self, pantalla:pygame.Surface, personaje_principal, suelo, lista_plataformas, imagen_fondo) -> None:
        pygame.init()
        # RELOJ = pygame.time.Clock()

        # # Pantalla
        # pantalla = Pantalla(TAMANIO_PANTALLA, "Clases\Clase_18\Recursos\\fondo_de_pantalla.png")

        # # Personaje
        # jugador = Jugador(PERSONAJE_QUIETO_MIRANDO_DERECHA[0])

        # # Superficie
        # suelo = Suelo("Clases\Clase_19\Recursos\suelo\\2.png", (ANCHO_PANTALLA, 50), 0, ANCHO_PANTALLA, ANCHO_PANTALLA, 50, jugador)

        # # Plataforma
        # lista_plataformas = [
        #     Plataforma((200, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 800, 800),
        #     Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 1050, 705),
        #     Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 800, 650),
        #     Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 500, 650),
        #     Plataforma((100, 20), "Clases\Clase_19\Recursos\plataforma\\14.png", 300, 520)]
        
        width = pantalla.get_width()
        height = pantalla.get_height()
        fondo = pygame.image.load("Clases\Clase_23\Recursos copy\pantalla\\fondo_de_pantalla.png")
        fondo = pygame.transform.scale(fondo, (width, height))

        diccionario_animaciones = {}
        diccionario_animaciones["quieto_mirando_derecha"] = PERSONAJE_QUIETO_MIRANDO_DERECHA
        diccionario_animaciones["quieto_mirando_izquierda"] = PERSONAJE_QUIETO_MIRANDO_IZQUIERDA
        diccionario_animaciones["quieto_corriendo_derecha"] = PERSONAJE_CORRIENDO_MIRANDO_DERECHA
        diccionario_animaciones["quieto_corriendo_izquierda"] = PERSONAJE_CORRIENDO_MIRANDO_IZQUIERDA
        diccionario_animaciones["quieto_saltando_derecha"] = PERSONAJE_SALTANDO_MIRANDO_DERECHA
        diccionario_animaciones["quieto_saltando_izquierda"] = PERSONAJE_SALTANDO_MIRANDO_IZQUIERDA

        super().__init__(pantalla, personaje_principal, suelo, lista_plataformas, imagen_fondo)




