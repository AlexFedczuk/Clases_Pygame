import pygame

def mover_personaje(rectangulo_personaje:pygame.Rect, velocidad:int):
    rectangulo_personaje.x += velocidad

def animar_personaje(pantalla, rectangulo_personaje, accion_personaje:list):
    global contador_pasos

    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0

    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1

def actualizar_pantalla(pantalla, rectangulo_personaje, que_hace, velocidad):

    match que_hace:
        case "Derecha":
            pass
            animar_personaje(pantalla, rectangulo_personaje, personaje_corriendo)
            mover_personaje(rectangulo_personaje, velocidad)
        # mover
        case "Izquierda":
            pass
        # animar
        # mover
        case "Quieto":
            animar_personaje(pantalla, rectangulo_personaje, personaje_quieto)