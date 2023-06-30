import pygame

def girar_lista_imagenes(lista:list) -> list:
    retorno = []
    for imagen in lista:        
        retorno.append(pygame.transform.flip(imagen, True, False))
    return retorno

TAMANIO = (150, 150)

PERSONAJE_QUIETO_MIRANDO_DERECHA = [
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (1).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (2).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (3).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (4).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (5).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (6).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (7).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (8).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (9).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (10).png"), TAMANIO)
]

PERSONAJE_QUIETO_MIRANDO_IZQUIERDA = girar_lista_imagenes(PERSONAJE_QUIETO_MIRANDO_DERECHA)


PERSONAJE_CORRIENDO_MIRANDO_DERECHA = [
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (1).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (2).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (3).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (4).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (5).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (6).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (7).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (8).png"), TAMANIO)
]

PERSONAJE_CORRIENDO_MIRANDO_IZQUIERDA = girar_lista_imagenes(PERSONAJE_CORRIENDO_MIRANDO_DERECHA)


personaje_saltando = [
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (1).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (2).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (3).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (4).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (5).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (6).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (7).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (8).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (9).png"), TAMANIO),
    pygame.transform.scale(pygame.image.load("Clases\Clase_18\Recursos\jugador\saltando\Jump (10).png"), TAMANIO)
]