import pygame, sys
from Clases import Imagen

# Contantes
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
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

imagen_vertical = Imagen((100,100), VERDE, (ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2))
imagen_horizontal = Imagen((100,100), ROJO, (ANCHO_PANTALLA - 100, ALTO_PANTALLA / 2))

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    PANTALLA.fill(AZUL_CLARO)
    PANTALLA.blit(imagen_vertical.imagen, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.imagen, imagen_horizontal.rectangulo)

    # MOVIMIENTOS
    imagen_horizontal.mover_imagen("horizontal", 10, (ANCHO_PANTALLA, ALTO_PANTALLA))
    imagen_vertical.mover_imagen("vertical", 10, (ANCHO_PANTALLA, ALTO_PANTALLA))

    # COLISIONES
    imagen_horizontal.detectar_colision(imagen_vertical, VERDE, BLANCO)

    eje_x = pygame.draw.line(PANTALLA, AZUL, (400,0), (400,800), 1)
    eje_y = pygame.draw.line(PANTALLA, AZUL, (0,300), (800,300), 1)
    pygame.display.flip()