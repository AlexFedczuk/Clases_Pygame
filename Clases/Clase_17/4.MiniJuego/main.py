import pygame, sys
from Class.Classes import Homero, Dona, Sonido
from Recursos.colores import *
from funciones import *
from configuraciones import *
from musica import *

# INICIO DE PYGAMES
pygame.init()
VENTANA = pygame.display.set_mode(TAMANIO_DE_PANTALLA)

# TEXTO A MOSTRAR EN LA BARRA DE LA VENTANA
pygame.display.set_caption("Los Simpson - The Game: Come todas las donas!")
# ACA CARGO EL LOGO DEL HUEGO
icono = pygame.image.load("Clase_17\\4.MiniJuego\Recursos\\00.png")
pygame.display.set_icon(icono)

# TEXTO A MOSTRAR EN LA PANTALLA
fuente = pygame.font.SysFont("consolas", 60)
# EL SCORE/EL CONTADOR DE PUNTAJE
score = 0

# MUSICA
musica_de_fondo.sonido.play()

# FPS
RELOJ = pygame.time.Clock()
tick = pygame.USEREVENT + 0 # ESTO SERIA UN EVENTO CREADO POR EL PROGRAMADOR
pygame.time.set_timer(tick, 100)

# HOMERO
pj_homero = Homero("Clase_17\\4.MiniJuego\Recursos\\foto_de_homero.png", (200,200), 150, 150, 39)
lista_homer = []
lista_homer.append(pj_homero.imagen)
lista_homer_girada = girar_imagenes(lista_homer, True, False)
pj_homero_girado = pygame.transform.flip(pj_homero.imagen, True, False)

# DONAS
lista_de_donas = crear_lista(50, 0, ANCHO_DE_VENTANA, 0, ALTO_DE_VENTANA, 60)

# FONDO DE PANTALLA
FONDO_DE_PANTALLA = pygame.image.load("Clase_17\\4.MiniJuego\Recursos\FONDO_de_PANTALLA.jpg")
FONDO_DE_PANTALLA_ESCALADO = pygame.transform.scale(FONDO_DE_PANTALLA, TAMANIO_DE_PANTALLA)

flag = True
bandera_movimiento = 0
contador = 0
while flag:
    RELOJ.tick(FPS)
    lista_de_eventos = pygame.event.get()   
    lista_teclas_presionadas = pygame.key.get_pressed()

    # SIEMPRE TIENE QUE ESTAR PRIMERO PARA QUE NO TE QUEDE NADA ATRAS DE LA PANTALLA
    VENTANA.blit(FONDO_DE_PANTALLA_ESCALADO, (0,0))

    # HOMERO
    if lista_teclas_presionadas[pygame.K_LEFT]:
        bandera_movimiento = 1
        nueva_posicion_x_homero = pj_homero.rectangulo.x + (-10)
        nueva_posicion_x_boca_homero = pj_homero.rectangulo_de_la_boca.x + (-10)
    elif lista_teclas_presionadas[pygame.K_RIGHT]:
        bandera_movimiento = 2     
        nueva_posicion_x_homero = pj_homero.rectangulo.x + 10
        nueva_posicion_x_boca_homero = pj_homero.rectangulo_de_la_boca.x + 10 

    if bandera_movimiento == 1:
        if nueva_posicion_x_homero > 0 and nueva_posicion_x_homero < 600:
            pj_homero.rectangulo.x = nueva_posicion_x_homero
            pj_homero.rectangulo_de_la_boca.x = nueva_posicion_x_boca_homero
        for imagen in lista_homer:
            VENTANA.blit(imagen, pj_homero.rectangulo)

    elif bandera_movimiento == 2:
        if nueva_posicion_x_homero > 0 and nueva_posicion_x_homero < 600:
            pj_homero.rectangulo.x = nueva_posicion_x_homero
            pj_homero.rectangulo_de_la_boca.x = nueva_posicion_x_boca_homero
        for imagen in lista_homer_girada:
            VENTANA.blit(imagen, pj_homero.rectangulo)

    elif bandera_movimiento == 0:
        for imagen in lista_homer:
            VENTANA.blit(imagen, pj_homero.rectangulo)
    
    # DONAS    
    for dona in lista_de_donas:
        VENTANA.blit(dona.imagen, dona.rectangulo)
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == tick:
            actualizar_posicion_dona(lista_de_donas)

    for dona in lista_de_donas:
        dona.detectar_colision(dona.rectangulo, pj_homero.rectangulo_de_la_boca, pj_homero, dona)

    score = fuente.render("SCORE: {0}".format(pj_homero.puntaje), True, VERDE)
    VENTANA.blit(score, (0,0))

    pygame.draw.rect(VENTANA, ROJO, pj_homero.rectangulo, 2)
    pygame.draw.rect(VENTANA, ROJO, pj_homero.rectangulo_de_la_boca, 2)
    pygame.display.update()
pygame.quit()