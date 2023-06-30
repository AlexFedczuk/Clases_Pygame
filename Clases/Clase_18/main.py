# https://www.youtube.com/watch?v=WTRXYD1w4hs&list=PLE9qW09sJEPQBZx_WJM46jkrtlY9FFlxb&index=15

import pygame
from configuraciones import *

######################### FUNCIONES DE MOVIMEINTO ##############################
def mover_personaje(rectangulo_personaje:pygame.Rect, velocidad:int):
    rectangulo_personaje.x += velocidad

def animar_personaje(pantalla, rectangulo_personaje, accion_personaje:list, contador_pasos:int):
    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0

    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1

def actualizar_pantalla(pantalla, rectangulo_personaje, que_hace, velocidad, contador_pasos:int):
    match que_hace:
        case "Derecha":
            animar_personaje(pantalla, rectangulo_personaje, personaje_corriendo, contador_pasos)
            mover_personaje(rectangulo_personaje, velocidad)
        case "Izquierda":
            animar_personaje(pantalla, rectangulo_personaje, personaje_corriendo, contador_pasos)
            mover_personaje(rectangulo_personaje, (-velocidad))
        case "Quieto":
            animar_personaje(pantalla, rectangulo_personaje, personaje_quieto) 
################################################################################

# Configuracion de la pantalla
ANCHO_PANTALLA, ALTO_PANTALLA = 1900, 1000
TAMANIO_PANTALLA = (ANCHO_PANTALLA, ALTO_PANTALLA)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

# Fondo de pantalla
fondo_pantalla = pygame.image.load("Clases\Clase_18\Recursos\\fondo_de_pantalla.png")
fondo_pantalla_rescalado = pygame.transform.scale(fondo_pantalla, TAMANIO_PANTALLA)
PANTALLA.blit(fondo_pantalla_rescalado, (0,0))

# Personaje
x_inicial = ALTO_PANTALLA / 2
y_inicial = 750
velocidad_mivimiento = 10
contador_pasos = 0

rectangulo_personaje = personaje_corriendo[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

posicion_actual_x = 0

que_hace = "Quieto"

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    teclas_presionadas = pygame.key.get_pressed()

    if (teclas_presionadas[pygame.K_RIGHT]):
        que_hace = "Derecha"
    elif (teclas_presionadas[pygame.K_LEFT]):
        que_hace = "Izquierda"
    else:
        que_hace = "Quieto"

    actualizar_pantalla(PANTALLA, que_hace, rectangulo_personaje, velocidad_mivimiento)

    pygame.display.update()