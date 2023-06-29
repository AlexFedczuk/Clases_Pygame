import pygame, sys

# Ventana
ANCHO_DE_VENTANA = 800
ALTO_DE_VENTANA = 800
screen_size = (ANCHO_DE_VENTANA, ALTO_DE_VENTANA)

pygame.init()
VENTANA = pygame.display.set_mode(screen_size)

# TEXTO A MOSTRAR EN LA BARRA DE LA VENTANA
pygame.display.set_caption("Prueba de eventos!")

flag = True
while flag:
    lista_de_eventos = pygame.event.get()
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        # ACA ESTOY DETECTANDO LA POSICION DEL 'INPUT' DEL MOUSE EN LA PANTALLA
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
    
    # ACA ESTOY DETECTANDO CUANDO EL TECLADO SE LE PRESIONO LA TECLA 0, <-, ->, el espacio y el Esc!
    lista_teclas_presionadas = pygame.key.get_pressed()    
    if lista_teclas_presionadas[pygame.K_0]:
        print(pygame.K_0)
    if lista_teclas_presionadas[pygame.K_LEFT]:
        print("<-")
    if lista_teclas_presionadas[pygame.K_RIGHT]:
        print("->")
    if lista_teclas_presionadas[pygame.K_SPACE]:
        print("Espacio")
    if lista_teclas_presionadas[pygame.K_ESCAPE]:
        # ACA APROVECHO Y CIERRO LA APLICACION CUANDO TOCO Esc
        print("Esc")
        flag = False

    pygame.display.update()
pygame.quit()