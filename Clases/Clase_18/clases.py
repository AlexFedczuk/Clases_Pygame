import pygame

class Homero:
    def __init__(self, path_imagen:str, tamanio):
        # Imagen
        self.imagen = pygame.image.load(path_imagen) # "Clase_17\4.MiniJuego\Recursos\01.png"
        self.imagen = pygame.transform.scale(self.imagen, tamanio) # tamanio = (ancho, altura)
        # Rectangulo
        self.rectangulo = self.imagen.get_rect() # Obtengo el rectangulo de la imagen!
        self.rectangulo.x = 500
        self.rectangulo.y = 500
        
    def realizar_movimiento(self, lista_de_inputs:list, valor_de_movimiento:int, tamanio_ventana:tuple):
        if lista_de_inputs[pygame.K_LEFT]:
            nueva_posicion_x_homero = self.rectangulo.x + (-valor_de_movimiento)
            nueva_posicion_x_boca = self.rectangulo_de_la_boca.x + (-valor_de_movimiento)
            self.mover_en_eje_x(nueva_posicion_x_homero, nueva_posicion_x_boca, tamanio_ventana)
        elif lista_de_inputs[pygame.K_RIGHT]:   
            nueva_posicion_x_homero = self.rectangulo.x + valor_de_movimiento
            nueva_posicion_x_boca = self.rectangulo_de_la_boca.x + valor_de_movimiento
            self.mover_en_eje_x(nueva_posicion_x_homero, nueva_posicion_x_boca, tamanio_ventana)
        elif lista_de_inputs[pygame.K_UP]:   
            nueva_posicion_y_homero = self.rectangulo.y + (-valor_de_movimiento)
            nueva_posicion_y_boca = self.rectangulo_de_la_boca.y + (-valor_de_movimiento)
            self.mover_en_eje_y(nueva_posicion_y_homero, nueva_posicion_y_boca, tamanio_ventana)
        elif lista_de_inputs[pygame.K_DOWN]:   
            nueva_posicion_y_homero = self.rectangulo.y + valor_de_movimiento
            nueva_posicion_y_boca = self.rectangulo_de_la_boca.y + valor_de_movimiento
            self.mover_en_eje_y(nueva_posicion_y_homero, nueva_posicion_y_boca, tamanio_ventana)

    def mover_en_eje_x(self, nueva_posicion_x_homero:int, nueva_posicion_x_boca:int, tamanio_ventana:tuple):
        if nueva_posicion_x_homero > (tamanio_ventana[0] - tamanio_ventana[0]) and nueva_posicion_x_homero < (tamanio_ventana[0] - 200):
            self.rectangulo.x = nueva_posicion_x_homero
            self.rectangulo_de_la_boca.x = nueva_posicion_x_boca

    def mover_en_eje_y(self, nueva_posicion_y_homero:int, nueva_posicion_y_boca:int, tamanio_ventana:tuple):
        if nueva_posicion_y_homero > (tamanio_ventana[1] - tamanio_ventana[1]) and nueva_posicion_y_homero < (tamanio_ventana[1] - 200):
            self.rectangulo.y = nueva_posicion_y_homero
            self.rectangulo_de_la_boca.y = nueva_posicion_y_boca
        
    def mostrar_en_pantalla(self, ventana:object, bandera:bool):
        if bandera == False:
            ventana.blit(pygame.transform.flip(self.imagen, True, False), self.rectangulo)
        else:
            ventana.blit(self.imagen, self.rectangulo)

    def detectar_colision(self, otra_imagen, color_original, color_de_colision):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.imagen.fill(color_de_colision)
            otra_imagen.imagen.fill(color_de_colision)
        else:
            self.imagen.fill(color_original)
            otra_imagen.imagen.fill(color_original)