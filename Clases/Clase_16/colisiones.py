import pygame, sys

# Contantes
ANCHO_PANTALL = 800
LARGO_PANTALLA = 600
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

PANTALLA = pygame.display.set_mode((ANCHO_PANTALL, LARGO_PANTALLA))

clock = pygame.time.Clock()

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)
rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (ANCHO_PANTALL /2, LARGO_PANTALLA / 2)

imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(ROJO)
rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (ANCHO_PANTALL - 100, LARGO_PANTALLA / 2)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    PANTALLA.fill(AZUL_CLARO)
    PANTALLA.blit(imagen_vertical, rectangulo_vertical)
    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)

    rectangulo_vertical.y += 10
    if rectangulo_vertical.top > LARGO_PANTALLA:
        rectangulo_vertical.bottom = 0
    rectangulo_horizontal.x += 20
    if rectangulo_horizontal.left > ANCHO_PANTALL:
        rectangulo_horizontal.right = 0

    if rectangulo_horizontal.colliderect(rectangulo_vertical):
        imagen_horizontal.fill(BLANCO)
        imagen_vertical.fill(BLANCO)
    else:
        imagen_horizontal.fill(VERDE)
        imagen_vertical.fill(AZUL)

    eje_x = pygame.draw.line(PANTALLA, AZUL, (400,0), (400,800), 1)
    eje_y = pygame.draw.line(PANTALLA, AZUL, (0,300), (800,300), 1)
    pygame.display.flip()