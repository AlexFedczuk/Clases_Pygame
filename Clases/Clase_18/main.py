# https://www.youtube.com/watch?v=WTRXYD1w4hs&list=PLE9qW09sJEPQBZx_WJM46jkrtlY9FFlxb&index=15

import pygame, sys
from configuraciones import *
from modo import *

######################### FUNCIONES DE MOVIMEINTO ##############################
def mover_personaje(rectangulo_personaje:pygame.Rect, velocidad:int):
    rectangulo_personaje.x += velocidad

def animar_personaje(pantalla:object, rectangulo_personaje:pygame.Rect, accion_personaje:list, contador_pasos:int):
    largo = len(accion_personaje)

    if contador_pasos >= largo:
        contador_pasos = 0

    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    # pygame.transform.flip(self.imagen, True, False), self.rectangulo
    contador_pasos += 1

    return contador_pasos

def actualizar_pantalla(pantalla:object, fondo_pantalla:object, rectangulo_personaje:pygame.Rect, que_hace:str, velocidad:int, contador_pasos:int, ultima_direccion:str,
                        bandera_esta_saltando:bool, potencia_salto:int):
    global desplazamiento_y
    
    PANTALLA.blit(fondo_pantalla, (0,0))

    match que_hace:
        case "Derecha":
            contador_pasos = animar_personaje(pantalla, rectangulo_personaje, PERSONAJE_CORRIENDO_MIRANDO_DERECHA, contador_pasos)
            mover_personaje(rectangulo_personaje, velocidad)
        case "Izquierda":
            contador_pasos = animar_personaje(pantalla, rectangulo_personaje, PERSONAJE_CORRIENDO_MIRANDO_IZQUIERDA, contador_pasos)
            mover_personaje(rectangulo_personaje, -velocidad)
        case "Salta":
            if not bandera_esta_saltando:
                bandera_esta_saltando = True
                desplazamiento_y = potencia_salto
                pass
        case "Quieto":
            if ultima_direccion == "Derecha":
                contador_pasos = animar_personaje(pantalla, rectangulo_personaje, PERSONAJE_QUIETO_MIRANDO_DERECHA, contador_pasos)
            elif ultima_direccion == "Izquierda":
                contador_pasos = animar_personaje(pantalla, rectangulo_personaje, PERSONAJE_QUIETO_MIRANDO_IZQUIERDA, contador_pasos)

    return contador_pasos

def girar_lista_imagenes(lista:list) -> list:
    retorno = []
    for imagen in lista:        
        retorno.append(pygame.transform.flip(imagen, True, False))
    return retorno
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

# Personaje
x_inicial = ALTO_PANTALLA / 2
y_inicial = 750
velocidad_mivimiento = 10
contador_pasos = 0

rectangulo_personaje = PERSONAJE_QUIETO_MIRANDO_DERECHA[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial
posicion_actual_x = 0

# SALTO
gravedad = 1
potencia_salto = -15
velocidad_limite_caida = 15
bandera_esta_saltando = False
desplazamiento_y = 0

que_hace = "Quieto"
ultima_direccion = "Derecha"

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

    if (teclas_presionadas[pygame.K_RIGHT]):
        que_hace = "Derecha"
        ultima_direccion = "Derecha"
    elif (teclas_presionadas[pygame.K_LEFT]):
        que_hace = "Izquierda"
        ultima_direccion = "Izquierda"
    elif (teclas_presionadas[pygame.K_UP]):
        que_hace = "Salta"
    else:
        que_hace = "Quieto"

    contador_pasos = actualizar_pantalla(PANTALLA, fondo_pantalla_rescalado, rectangulo_personaje, que_hace, velocidad_mivimiento, contador_pasos, ultima_direccion, bandera_esta_saltando, potencia_salto)

    if get_mode():
        pygame.draw.rect(PANTALLA, "Red", rectangulo_personaje, 2)

    pygame.display.update()