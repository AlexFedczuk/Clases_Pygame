import pygame

class Imagen:
    # Contructor
    # atributos (setters y getters)
    # metodos
    def __init__(self, tamanio, color, origen) -> None:
        # imagen
        self.imagen = pygame.Surface(tamanio)
        self.color = color
        self.imagen.fill(self.color)
        # rectangulo
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.center = origen

    def mover_imagen(self, sentido:str, velocidad_desplazamiento:int, tamanio_pantalla):#(LARGO,ALTO)
        if sentido == "vertical":
            self.rectangulo.y += velocidad_desplazamiento
            if self.rectangulo.top > tamanio_pantalla[1]:
                self.rectangulo.bottom = 0
        else:
            self.rectangulo.x += velocidad_desplazamiento
            if self.rectangulo.left > tamanio_pantalla[0]:
                self.rectangulo.right = 0

    def detectar_colision(self, otra_imagen, color_original, color_de_colision):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.imagen.fill(color_de_colision)
            otra_imagen.imagen.fill(color_de_colision)
        else:
            self.imagen.fill(color_original)
            otra_imagen.imagen.fill(color_original)