import pygame, random

class Homero:
    # Contructor
    # Atributos (setters y getters)
    # Metodos
    def __init__(self, path_imagen:str, tamanio, x_de_la_boca:int, y_de_la_boca:int, ancho_de_la_boca:int):
        # Imagen
        self.imagen = pygame.image.load(path_imagen) # "Clase_17\4.MiniJuego\Recursos\01.png"
        self.imagen = pygame.transform.scale(self.imagen, tamanio) # tamanio = (ancho, altura)
        # Rectangulo
        self.rectangulo = self.imagen.get_rect() # Obtengo el rectangulo de la imagen!
        self.rectangulo.x = 400
        self.rectangulo.y = 600 
        # El rectangulo de la boca de Homero
        self.rectangulo_de_la_boca = pygame.Rect(x_de_la_boca, y_de_la_boca, ancho_de_la_boca, ancho_de_la_boca)
        self.rectangulo_de_la_boca.x = 490
        self.rectangulo_de_la_boca.y = 668
        # El contador del Score del pj
        self.puntaje = 0

    def aumentar_puntaje(self, puntos_aumentados):
        self.puntaje += puntos_aumentados

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

class Dona:
    # Contructor
    # Atributos (setters y getters)
    # Metodos
    def __init__(self, path_imagen:str, x:int, y:int, ancho:int, alto:int):
        # Imagen
        self.imagen = pygame.image.load(path_imagen) # "Clase_17\4.MiniJuego\Recursos\01.png"
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto)) # tamanio = (ancho, altura)
        # Rectangulo
        self.rectangulo = self.imagen.get_rect() # Obtengo el rectangulo de la imagen!
        self.rectangulo.x = x
        self.rectangulo.y = y
        # Diccionario con datos
        dona = {}
        dona["superficie"] = self.imagen
        dona["rectangulo"] = self.rectangulo
        dona["velocidad_de_movimiento"] = random.randrange(10, 20, 1)

        # return dona
    
    def crear_lista(cantidad:int, ancho_minimo_pantalla:int, ancho_maximo_pantalla:int, alto_minimo_pantalla:int, alto_maximo_pantalla:int, intervalos:int):
        lista = []

        for i in range(cantidad):
            x = random.randrange(ancho_minimo_pantalla, ancho_maximo_pantalla, intervalos)
            y = random.randrange(alto_minimo_pantalla, alto_maximo_pantalla, intervalos)
            dona_creada = Dona("Clase_17\4.MiniJuego\Recursos\00.png", x, y, 60, 60)
            lista.append(dona_creada)
        return lista

    def mover_imagen(self, sentido:str, velocidad_desplazamiento:int, tamanio_pantalla):# (LARGO,ALTO)
        if sentido == "vertical":
            self.rectangulo.y += velocidad_desplazamiento
            if self.rectangulo.top > tamanio_pantalla[1]:
                self.rectangulo.bottom = 0
        else:
            self.rectangulo.x += velocidad_desplazamiento
            if self.rectangulo.left > tamanio_pantalla[0]:
                self.rectangulo.right = 0

    def detectar_colision(self, rectangulo_dona:object, rectangulo_boca:object, homero:object, dona:object,):
        if rectangulo_boca.colliderect(rectangulo_dona):
            homero.aumentar_puntaje(100)
            print("La comio!")
            self.producir_sonido("Clases\Clase_17\\4.MiniJuego\Recursos\clic.wav", 0.1)
            dona.regenerar_dona()
        elif rectangulo_dona.y > 800:
            dona.regenerar_dona()

    def producir_sonido(self, path_sonido:str, volumen:float):
        sonido = Sonido(path_sonido, volumen)
        sonido.sonido.play()
    
    def regenerar_dona(self):
        self.rectangulo.x = random.randrange(0, 740, 60)
        self.rectangulo.y = random.randrange(-1000, 0, 60)
    
class Sonido:
    # Contructor
    # Atributos (setters y getters)
    # Metodos
    def __init__(self, path_grabacion:str, volumen:float):
        self.sonido = pygame.mixer.Sound(path_grabacion) # "Clase_17\4.MiniJuego\Recursos\musica_de_fondo.wav"
        self.sonido.set_volume(volumen)
        # self.sonido.play()