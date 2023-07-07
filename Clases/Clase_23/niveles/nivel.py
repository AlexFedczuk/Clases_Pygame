import pygame
from modo import *

class Nivel:
    def __init__(self, pantalla, personaje_principal, suelo, lista_plataformas, imagen_fondo) -> None:
        self._slave = pantalla
        self.jugador = personaje_principal
        self.suelo = suelo
        self.plataformas = lista_plataformas
        self.imagen_fondo = imagen_fondo

    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_F1:
                    cambiar_modo()
        self.actualizar_pantalla
        self.leer_inputs()
    
    def actualizar_pantalla(self) -> None:
        self._slave.blit(self.imagen_fondo, (0,0))

        for plataforma in self.plataformas:
            plataforma.draw(self._slave)

        self.jugador.update(self._slave, self.plataformas)

        # renderizar_imagen(pantalla, pantalla.fondo, 0, 0)
        # for plataforma in lista_plataformas:
        #     renderizar_imagen(pantalla, plataforma.imagen, plataforma.rectangulo.x, plataforma.rectangulo.y)
        # renderizar_imagen(pantalla, suelo.imagen, suelo.rectangulo.x, suelo.rectangulo.y)

        # match jugador.que_hace:
        #     case "Derecha":
        #         if jugador.bandera_esta_saltando == False:
        #             animar_personaje(pantalla, jugador, jugador.corriendo_mirando_derecha)
        #         mover_personaje(jugador, jugador.velocidad_de_movimiento)
        #     case "Izquierda":
        #         if jugador.bandera_esta_saltando == False:
        #             animar_personaje(pantalla, jugador, jugador.corriendo_mirando_izquierda)
        #         mover_personaje(jugador, -jugador.velocidad_de_movimiento)
        #     case "Salta":
        #         if jugador.bandera_esta_saltando == False:
        #             jugador.bandera_esta_saltando = True
        #             jugador.desplazamiento_y = jugador.potencia_salto
        #     case "Quieto":
        #         if jugador.bandera_esta_saltando == False:
        #             if jugador.ultima_direccion == "Derecha":
        #                 animar_personaje(pantalla, jugador, jugador.quieto_mirando_derecha)
        #             elif jugador.ultima_direccion == "Izquierda":
        #                 animar_personaje(pantalla, jugador, jugador.quieto_mirando_izquierda)
        # aplicar_gravedad(pantalla, jugador, suelo, lista_plataformas)

    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT]):
            self.jugador.que_hace = "Derecha"
            self.jugador.ultima_direccion = "Derecha"
        elif (keys[pygame.K_LEFT]):
            self.jugador.que_hace = "Izquierda"
            self.jugador.ultima_direccion = "Izquierda"
        elif (keys[pygame.K_UP]):
            self.jugador.que_hace = "Salta"
        else:
            self.jugador.que_hace = "Quieto"

        # if (keys[pygame.K_RIGHT] and self.jugador.rectangulo.colliderect(self._slave.rectangulo) and self.jugador.rectangulo.right != self._slave.rectangulo.right):# jugador.rectangulo.right < ANCHO_PANTALLA - jugador.velocidad_de_movimiento
        #     self.jugador.que_hace = "Derecha"
        #     self.jugador.ultima_direccion = "Derecha"
        # elif (keys[pygame.K_LEFT] and self.jugador.rectangulo.colliderect(self._slave.rectangulo) and self.jugador.rectangulo.left != self._slave.rectangulo.left):
        #     self.jugador.que_hace = "Izquierda"
        #     self.jugador.ultima_direccion = "Izquierda"
        # elif (keys[pygame.K_UP]):
        #     self.jugador.que_hace = "Salta"
        # else:
        #     self.jugador.que_hace = "Quieto"

    def dibujar_rectangulos(self):
        if get_mode():
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Blue", self.jugador.lados[lado], 2)

            for lado in self.suelo.lados:
                pygame.draw.rect(self._slave, "Red", self.suelo.lados[lado], 2)

            for plataforma in self.plataformas:
                pygame.draw.rect(self._slave, "Green", plataforma.lados[lado], 2)