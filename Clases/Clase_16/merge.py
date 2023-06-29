import pygame, sys
from Class_Personaje import Personaje

# Contantes
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
screen_sizes = (800,600)
# Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
# Frame per second
FPS = 30

pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
clock = pygame.time.Clock()

# fondo
fondo = pygame.image.load("Recursos\Game_Over.jpg")
fondo_escalado = pygame.transform.scale(fondo, screen_sizes)
PANTALLA.blit(fondo_escalado, (0,0))

homero = Personaje((200,200),(ANCHO_PANTALLA/2, ALTO_PANTALLA/2), "foto_de_homero.png")
dona = Personaje((100,100),(ANCHO_PANTALLA/2, ALTO_PANTALLA), "Recursos\dona.png")

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.blit(fondo_escalado, (0,0))
    PANTALLA.blit(dona.superficie, dona.rectangulo)
    PANTALLA.blit(homero.superficie, homero.rectangulo)

    # MOVIMIENTOS
    homero.mover_imagen("horizontal", 10, (ANCHO_PANTALLA, ALTO_PANTALLA))
    dona.mover_imagen("vertical", 10, (ANCHO_PANTALLA, ALTO_PANTALLA))
    homero.detectar_colision(dona, "Recursos\\acierto.wav", 0.1)

    # COLISIONES
    # homero.detectar_colision(dona, VERDE, BLANCO)

    eje_x = pygame.draw.line(PANTALLA, AZUL, (400,0), (400,800), 1)
    eje_y = pygame.draw.line(PANTALLA, AZUL, (0,300), (800,300), 1)
    pygame.display.flip()