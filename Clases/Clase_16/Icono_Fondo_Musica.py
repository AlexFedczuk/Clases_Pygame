import pygame, sys

# Contantes
ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 500
screen_sizes = (ANCHO_PANTALLA, ALTO_PANTALLA)

pygame.init()

PANTALLA = pygame.display.set_mode(screen_sizes)

# Icono
icono = pygame.image.load("foto_de_homero.png")
pygame.display.set_icon(icono)

# fondo
fondo = pygame.image.load("Recursos\dona.png")
fondo_escalado = pygame.transform.scale(fondo, screen_sizes)
PANTALLA.blit(fondo_escalado, (0,0))

# musica
pygame.mixer.music.load("Recursos\\acierto.wav")
pygame.mixer.music.play(-1) # Si pongo -1 el sonido entra en un LOOP, si dejo vacio los parentecis no.
pygame.mixer.music.set_volume(0.1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()