import pygame

class Personaje:
    # Contructor
    # atributos (setters y getters)
    # metodos
    def __init__(self, tamanio, origen, path_imagen) -> None:
        self.superficie = pygame.image.load(path_imagen)
        self.superficie = pygame.transform.scale(self.superficie, tamanio)
        
        self.rectangulo = self.superficie.get_rect()
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

    def detectar_colision(self, otra_imagen, path_sonido, volumen):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            pygame.mixer.music.load(path_sonido)
            pygame.mixer.music.play() # Si pongo -1 el sonido entra en un LOOP, si dejo vacio los parentecis no.
            pygame.mixer.music.set_volume(volumen)