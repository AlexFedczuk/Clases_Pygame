import pygame
from niveles.configuraciones import *
from funciones.funciones import *

class Jugador:
    def __init__(self, imagen):
        # Imagen
        self.imagen = imagen
        # Rectangulo
        self.rectangulo = self.imagen.get_rect() # Obtengo el rectangulo de la imagen!
        self.rectangulo.x = 1000 / 2
        self.rectangulo.y = 750
        self.diccionario_rectangulos = {}
        # -
        self.velocidad_de_movimiento = 10
        self.contador_pasos = 0
        self.contador_imagenes_salto = 0
        # Gravedad
        self.gravedad = 1
        self.potencia_salto = -15
        self.velocidad_limite_caida = 15
        self.bandera_esta_saltando = False
        self.desplazamiento_y = 0
        # Que hace?
        self.que_hace = "Quieto"
        self.ultima_direccion = "Derecha"
        # animaciones
        self.quieto_mirando_derecha = PERSONAJE_QUIETO_MIRANDO_DERECHA
        self.quieto_mirando_izquierda = PERSONAJE_QUIETO_MIRANDO_IZQUIERDA
        self.corriendo_mirando_derecha = PERSONAJE_CORRIENDO_MIRANDO_DERECHA
        self.corriendo_mirando_izquierda = PERSONAJE_CORRIENDO_MIRANDO_IZQUIERDA
        self.saltando_mirando_derecha = PERSONAJE_SALTANDO_MIRANDO_DERECHA
        self.saltando_mirando_izquierda = PERSONAJE_SALTANDO_MIRANDO_IZQUIERDA

        obtener_rectangulos(self)
        print(self.diccionario_rectangulos)

    def obtener_rectangulos(self):
        self.diccionario_rectangulos["rectangulo_inferior"] = pygame.Rect(self.rectangulo.left, self.rectangulo.bottom - 6, self.rectangulo.width, 6)
        self.diccionario_rectangulos["rectangulo_derecho"] = pygame.Rect(self.rectangulo.right - 2, self.rectangulo.top, 2, self.rectangulo.height)
        self.diccionario_rectangulos["rectangulo_izquierdo"] = pygame.Rect(self.rectangulo.left, self.rectangulo.top, 2, self.rectangulo.height)
        self.diccionario_rectangulos["rectangulo_superior"] = pygame.Rect(self.rectangulo.left, self.rectangulo.top, self.rectangulo.width, 6)    

    """def aplicar_gravedad(self, pantalla:object, suelo:object) -> None:
        if self.bandera_esta_saltando:
            if self.ultima_direccion == "Derecha":
                    self.animar(pantalla, self.saltando_mirando_derecha)
            elif self.ultima_direccion == "Izquierda":
                    self.animar(pantalla, self.saltando_mirando_izquierda)
            
            self.rectangulo.y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.velocidad_limite_caida:
                self.desplazamiento_y += self.gravedad
            if self.rectangulo.colliderect(suelo.rectangulo):
                self.bandera_esta_saltando = False
                self.desplazamiento_y = 0
                self.rectangulo.bottom = suelo.rectangulo.top

    def animar(self, pantalla:object, accion_personaje:list) -> None:
        largo = len(accion_personaje)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.pantalla.blit(accion_personaje[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1

    def mover(self):
        self.rectangulo.x += self.velocidad_de_movimiento"""

    def actualizar_pantalla(self, pantalla:object, suelo:object) -> None:
    
        pantalla.pantalla.blit(pantalla.fondo, (0,0))

        match self.que_hace:
            case "Derecha":
                self.animar(pantalla, self.corriendo_mirando_derecha)
                self.mover(self, self.velocidad_de_movimiento)
            case "Izquierda":
                self.animar(pantalla, self.corriendo_mirando_izquierda)
                self.mover(self, -self.velocidad_de_movimiento)
            case "Salta":
                if not self.bandera_esta_saltando:
                    self.bandera_esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    pass
            case "Quieto":
                if self.ultima_direccion == "Derecha":
                    self.animar(pantalla, self.quieto_mirando_derecha)
                elif self.ultima_direccion == "Izquierda":
                    self.animar(pantalla, self.quieto_mirando_izquierda)
        self.aplicar_gravedad(pantalla, suelo)