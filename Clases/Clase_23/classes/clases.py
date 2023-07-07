import pygame
from configuraciones import *
from funciones import *

class Suelo:
    def __init__(self, path_imagen:str, tamanio:int, rectangulo_x:int, rectangulo_y:int, ancho_rectangulo:int, alto_rectangulo:int, jugador:object):
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, tamanio)
        self.rectangulo = pygame.Rect(rectangulo_x, rectangulo_y, ancho_rectangulo, alto_rectangulo)
        self.rectangulo.top = jugador.rectangulo.bottom
        self.diccionario_rectangulos = {}
        
        obtener_rectangulos(self)

class Plataforma:
    def __init__(self, tamanio:tuple, path_imagen:str, rectangulo_x, rectangulo_y):
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, tamanio)
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = rectangulo_x
        self.rectangulo.y = rectangulo_y
        self.diccionario_rectangulos = {}
        
        obtener_rectangulos(self)

class Pantalla:
    def __init__(self, tamanio:tuple, path_imagen:str):
        self.pantalla = pygame.display.set_mode(tamanio)
        self.fondo = pygame.image.load(path_imagen)
        self.fondo = pygame.transform.scale(self.fondo, tamanio)
        self.rectangulo = self.fondo.get_rect()
        self.diccionario_rectangulos = {}
        
        obtener_rectangulos(self)