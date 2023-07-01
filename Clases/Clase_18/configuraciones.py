import pygame

def cargar_imagenes_lista(path_primer_imagen:str, cantidad_imagnes:int) -> list:
    lista_cargada = []

    for i in range(0, cantidad_imagnes - 1):
        lista_cargada.append(path_primer_imagen)

def rescalar_lista_imagenes(lista_imagenes:list, tamanio:tuple) -> list:
    lista_rescalada = []
    
    for imagen in lista_imagenes:
        lista_rescalada.append(pygame.transform.scale(imagen, tamanio))

    return lista_rescalada

def girar_lista_imagenes(lista:list) -> list:
    retorno = []
    for imagen in lista:        
        retorno.append(pygame.transform.flip(imagen, True, False))
    return retorno

TAMANIO = (150, 150)

PERSONAJE_QUIETO_MIRANDO_DERECHA = [
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (1).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (2).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (3).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (4).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (5).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (6).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (7).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (8).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (9).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\quieto\Idle (10).png")
]
# PERSONAJE_QUIETO_MIRANDO_DERECHA = cargar_imagenes_lista(f"Clases\Clase_18\Recursos\jugador\quieto\Idle ({0}).png", 10)
PERSONAJE_QUIETO_MIRANDO_DERECHA = rescalar_lista_imagenes(PERSONAJE_QUIETO_MIRANDO_DERECHA, TAMANIO)
PERSONAJE_QUIETO_MIRANDO_IZQUIERDA = girar_lista_imagenes(PERSONAJE_QUIETO_MIRANDO_DERECHA)

PERSONAJE_CORRIENDO_MIRANDO_DERECHA = [
    pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (1).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (2).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (3).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (4).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (5).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (6).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (7).png"),
    pygame.image.load("Clases\Clase_18\Recursos\jugador\corriendo\Run (8).png")
]
PERSONAJE_CORRIENDO_MIRANDO_DERECHA = rescalar_lista_imagenes(PERSONAJE_CORRIENDO_MIRANDO_DERECHA, TAMANIO)
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