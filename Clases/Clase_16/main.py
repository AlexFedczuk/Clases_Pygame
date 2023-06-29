import pygame, sys

# Contantes
LARGO_PANTALLA = 500
ANCHO_PANTALL = 400

# Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

pygame.init()

PANTALLA = pygame.display.set_mode((LARGO_PANTALLA, ANCHO_PANTALL))
PANTALLA.fill(AZUL_CLARO)

rectangulo = pygame.draw.rect(PANTALLA, VERDE, (100, 50, 100, 200), 8)
                                            #  (eje X, eje Y, ancho, largo), grosor
linea = pygame.draw.line(PANTALLA, NEGRO, (100,104),(100,150), 10)

circulo = pygame.draw.circle(PANTALLA, NEGRO, (125,250), 25, 3)

elipse = pygame.draw.ellipse(PANTALLA,  ROJO, (275,200, 40, 80), 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

