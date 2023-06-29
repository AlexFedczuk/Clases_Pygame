import pygame, sys
from Class.Classes import Homero, Dona, Sonido
from colores import *
from funciones import *
from configuraciones import *
from musica import *

# INICIO DE PYGAMES
pygame.init()
VENTANA = pygame.display.set_mode(TAMANIO_DE_PANTALLA)

# TEXTO A MOSTRAR EN LA BARRA DE LA VENTANA
pygame.display.set_caption("Los Simpson - The Game: Come todas las donas!")
# ACA CARGO EL LOGO DEL HUEGO
icono = pygame.image.load("Clases\Clase_17\\4.MiniJuego\Recursos\\00.png")
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
pj_homero = Homero("Clases\Clase_17\\4.MiniJuego\Recursos\\foto_de_homero.png", (200,200), 150, 150, 39)
pj_homero_girado = pygame.transform.flip(pj_homero.imagen, True, False)

# DONAS
lista_de_donas = crear_lista(50, 0, ANCHO_DE_VENTANA, 0, ALTO_DE_VENTANA, 60)

# FONDO DE PANTALLA
FONDO_DE_PANTALLA = pygame.image.load("Clases\Clase_17\\4.MiniJuego\Recursos\FONDO_de_PANTALLA.jpg")
FONDO_DE_PANTALLA_ESCALADO = pygame.transform.scale(FONDO_DE_PANTALLA, TAMANIO_DE_PANTALLA)

flag = True
bandera_mirando_izquierda = True
contador = 0
while flag:
    RELOJ.tick(FPS)
    lista_de_eventos = pygame.event.get()   
    lista_teclas_presionadas = pygame.key.get_pressed()

    # SIEMPRE TIENE QUE ESTAR PRIMERO, PARA QUE NO TE QUEDE NADA ATRAS DE LA PANTALLA!
    VENTANA.blit(FONDO_DE_PANTALLA_ESCALADO, (0,0))

    if detectar_input_teclado(lista_teclas_presionadas, pygame.K_RIGHT) == True and detectar_input_teclado(lista_teclas_presionadas, pygame.K_LEFT) == False:
        bandera_mirando_izquierda = False
    elif detectar_input_teclado(lista_teclas_presionadas, pygame.K_RIGHT) == False and detectar_input_teclado(lista_teclas_presionadas, pygame.K_LEFT) == True:
        bandera_mirando_izquierda = True

    # Homero
    pj_homero.realizar_movimiento(lista_teclas_presionadas, 10, TAMANIO_DE_PANTALLA)
    pj_homero.mostrar_en_pantalla(VENTANA, bandera_mirando_izquierda)
    
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

    if lista_teclas_presionadas[pygame.K_F1]: 
        pygame.draw.rect(VENTANA, ROJO, pj_homero.rectangulo, 2)
        pygame.draw.rect(VENTANA, ROJO, pj_homero.rectangulo_de_la_boca, 2)
    pygame.display.update()
pygame.quit()