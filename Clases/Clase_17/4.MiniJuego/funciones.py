import random, pygame
from Class.Classes import Dona

def crear_lista(cantidad:int, ancho_minimo_pantalla:int, ancho_maximo_pantalla:int, alto_minimo_pantalla:int, alto_maximo_pantalla:int, intervalos:int):
        lista = []

        for i in range(cantidad):
            x = random.randrange(ancho_minimo_pantalla, ancho_maximo_pantalla, intervalos)
            y = random.randrange(alto_minimo_pantalla, alto_maximo_pantalla, intervalos)
            dona_creada = Dona("Clase_17\\4.MiniJuego\Recursos\\00.png", x, y, 60, 60)
            lista.append(dona_creada)
        return lista

def actualizar_posicion_dona(lista:list):
      for dona in lista:
            dona.rectangulo.y += 5

def girar_imagenes(lista_original, flip_x, flip_y) -> list:
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada
      