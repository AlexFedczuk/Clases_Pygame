import pygame, sys
import random

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
AZUL_CLARO = (0,220,255)

pygame.init()
VENTANA = pygame.display.set_mode(screen_size)

# TEXTO A MOSTRAR EN LA BARRA DE LA VENTANA
pygame.display.set_caption("Prueba de FPS")

# TEXTO A MOSTRAR EN LA PANTALLA
fuente = pygame.font.SysFont("consolas", 25)
texto = fuente.render("Hola mundo!", False, VERDE, AZUL_CLARO)


lista_de_circulos = []
# ACA ESTOY CREANDO UNA LISTA DE CORDENADAS (X,Y)
for i in range(77):
    x = random.randint(1, ANCHO_DE_VENTANA - 1)
    y = random.randint(1, ALTO_DE_VENTANA - 1)
    lista_de_circulos.append([x,y])
# print(lista_de_circulos)

reloj = pygame.time.Clock()

flag = True
while flag:
    # ACA MANEJO LOS
    tiempo = reloj.tick(120)

    VENTANA.fill(NEGRO)

    lista_de_eventos = pygame.event.get()
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT:
            flag = False
    # VENTANA.blit(texto, (ANCHO_DE_VENTANA/2,ALTO_DE_VENTANA/2))

    for circulo in lista_de_circulos:
        pygame.draw.circle(VENTANA, AZUL_CLARO, (circulo[0], circulo[1]), 5, 10)

    for circulo in lista_de_circulos:
        circulo[0] += 1
        if circulo[0] > ANCHO_DE_VENTANA:
            circulo[0] = 0
        circulo[1] += 1
        if circulo[1] > ALTO_DE_VENTANA:
            circulo[1] = 1

    pygame.display.update()
    # CON ESTO RETRASO LA FRECUENCIA DE FPSs con la que se disparan!
    # pygame.time.delay(2)
pygame.quit()
