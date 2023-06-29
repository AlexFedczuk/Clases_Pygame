import pygame, sys

# Ventana
ANCHO_DE_VENTANA = 800
ALTO_DE_VENTANA = 800
screen_size = (ANCHO_DE_VENTANA, ALTO_DE_VENTANA)

# Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

pygame.init()
VENTANA = pygame.display.set_mode(screen_size)

# TEXTO A MOSTRAR EN LA BARRA DE LA VENTANA
pygame.display.set_caption("Prueba de texto lalalalala")

# TEXTO A MOSTRAR EN LA PANTALLA
fuente = pygame.font.SysFont("consolas", 60)
texto = fuente.render("Hola mundo!", False, VERDE, AZUL_CLARO)

flag = True
while flag:
    lista_de_eventos = pygame.event.get()
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT:
            flag = False
    VENTANA.blit(texto, (ANCHO_DE_VENTANA/2,ALTO_DE_VENTANA/2))
    pygame.display.update()
pygame.quit()
