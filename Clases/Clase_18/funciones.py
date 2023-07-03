import pygame

def aplicar_gravedad(pantalla:object, jugador:object, suelo:object):
    if jugador.bandera_esta_saltando:
        if jugador.ultima_direccion == "Derecha":
                animar_personaje(pantalla, jugador, jugador.saltando_mirando_derecha)
        elif jugador.ultima_direccion == "Izquierda":
                animar_personaje(pantalla, jugador, jugador.saltando_mirando_izquierda)
        
        jugador.rectangulo.y += jugador.desplazamiento_y

        if jugador.desplazamiento_y + jugador.gravedad < jugador.velocidad_limite_caida:
            jugador.desplazamiento_y += jugador.gravedad
        if jugador.rectangulo.colliderect(suelo.rectangulo):
            jugador.bandera_esta_saltando = False
            jugador.desplazamiento_y = 0
            jugador.rectangulo.bottom = suelo.rectangulo.top

def mover_personaje(jugador:object, velocidad_de_movimiento:int):
    jugador.rectangulo.x += velocidad_de_movimiento

def animar_personaje(pantalla:object, jugador:object, accion_personaje:list) -> None:
    largo = len(accion_personaje)

    if jugador.contador_pasos >= largo:
        jugador.contador_pasos = 0

    pantalla.pantalla.blit(accion_personaje[jugador.contador_pasos], jugador.rectangulo)
    # pygame.transform.flip(self.imagen, True, False), self.rectangulo
    jugador.contador_pasos += 1

def actualizar_pantalla(pantalla:object, jugador:object, suelo:object) -> None:
    
    pantalla.pantalla.blit(pantalla.fondo, (0,0))

    match jugador.que_hace:
        case "Derecha":
            if not jugador.bandera_esta_saltando:
                animar_personaje(pantalla, jugador, jugador.corriendo_mirando_derecha)
            mover_personaje(jugador, jugador.velocidad_de_movimiento)
        case "Izquierda":
            if not jugador.bandera_esta_saltando:
                animar_personaje(pantalla, jugador, jugador.corriendo_mirando_izquierda)
            mover_personaje(jugador, -jugador.velocidad_de_movimiento)
        case "Salta":
            if not jugador.bandera_esta_saltando:
                jugador.bandera_esta_saltando = True
                jugador.desplazamiento_y = jugador.potencia_salto
                pass
        case "Quieto":
            if not jugador.bandera_esta_saltando:
                if jugador.ultima_direccion == "Derecha":
                    animar_personaje(pantalla, jugador, jugador.quieto_mirando_derecha)
                elif jugador.ultima_direccion == "Izquierda":
                    animar_personaje(pantalla, jugador, jugador.quieto_mirando_izquierda)
    aplicar_gravedad(pantalla, jugador, suelo)

def girar_lista_imagenes(lista:list) -> list:
    retorno = []
    for imagen in lista:        
        retorno.append(pygame.transform.flip(imagen, True, False))
    return retorno

def registrar_ingreso_teclas(lista_teclas_presionadas:list, pantalla:object, jugador:object) -> None:
    if (lista_teclas_presionadas[pygame.K_RIGHT] and jugador.rectangulo.colliderect(pantalla.rectangulo) and jugador.rectangulo.right != pantalla.rectangulo.right):# jugador.rectangulo.right < ANCHO_PANTALLA - jugador.velocidad_de_movimiento
        jugador.que_hace = "Derecha"
        jugador.ultima_direccion = "Derecha"
    elif (lista_teclas_presionadas[pygame.K_LEFT] and jugador.rectangulo.colliderect(pantalla.rectangulo) and jugador.rectangulo.left != pantalla.rectangulo.left):
        jugador.que_hace = "Izquierda"
        jugador.ultima_direccion = "Izquierda"
    elif (lista_teclas_presionadas[pygame.K_UP]):
        jugador.que_hace = "Salta"
    else:
        jugador.que_hace = "Quieto"