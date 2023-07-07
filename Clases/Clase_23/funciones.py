import pygame

def aplicar_gravedad(pantalla:object, jugador:object, suelo:object, lista_plataformas:list):
    print("Bandera de 'jugador.bandera_esta_saltando':", jugador.bandera_esta_saltando)

    if jugador.bandera_esta_saltando == True:
        if jugador.ultima_direccion == "Derecha":
                animar_personaje(pantalla, jugador, jugador.saltando_mirando_derecha)
        elif jugador.ultima_direccion == "Izquierda":
                animar_personaje(pantalla, jugador, jugador.saltando_mirando_izquierda)
        
        jugador.rectangulo.y += jugador.desplazamiento_y
        
        for clave in jugador.diccionario_rectangulos:
            jugador.diccionario_rectangulos[clave].y += jugador.desplazamiento_y

        if jugador.desplazamiento_y + jugador.gravedad < jugador.velocidad_limite_caida:
            jugador.desplazamiento_y += jugador.gravedad

    lista_aux_plataformas = []
    lista_aux_plataformas.append(suelo)
    for pltaforma in lista_plataformas:
        lista_aux_plataformas.append(pltaforma)

    for plataforma in lista_aux_plataformas:            
        if jugador.diccionario_rectangulos["rectangulo_inferior"].colliderect(plataforma.diccionario_rectangulos["rectangulo_superior"]):
            jugador.desplazamiento_y = 0
            jugador.bandera_esta_saltando = False                
            jugador.rectangulo.bottom = plataforma.rectangulo.top
            break
        else:
            jugador.bandera_esta_saltando = True

def comprobar_contacto_rectangulos(rectangulo_uno:object, rectangulo_dos:object) -> bool:
    if rectangulo_uno.colliderect(rectangulo_dos):
        return True
    else:
        return False

def mover_personaje(jugador:object, velocidad_de_movimiento:int):
    jugador.rectangulo.x += velocidad_de_movimiento
    for clave in jugador.diccionario_rectangulos:
        jugador.diccionario_rectangulos[clave].x += velocidad_de_movimiento

def animar_personaje(pantalla:object, jugador:object, accion_personaje:list) -> None:
    largo = len(accion_personaje)

    if jugador.contador_pasos >= largo:
        jugador.contador_pasos = 0

    pantalla.pantalla.blit(accion_personaje[jugador.contador_pasos], jugador.rectangulo)
    # pygame.transform.flip(self.imagen, True, False), self.rectangulo
    jugador.contador_pasos += 1

def actualizar_pantalla(pantalla:object, jugador:object, suelo:object, lista_plataformas:list) -> None:    
    renderizar_imagen(pantalla, pantalla.fondo, 0, 0)
    for plataforma in lista_plataformas:
        renderizar_imagen(pantalla, plataforma.imagen, plataforma.rectangulo.x, plataforma.rectangulo.y)
    renderizar_imagen(pantalla, suelo.imagen, suelo.rectangulo.x, suelo.rectangulo.y)

    match jugador.que_hace:
        case "Derecha":
            if jugador.bandera_esta_saltando == False:
                animar_personaje(pantalla, jugador, jugador.corriendo_mirando_derecha)
            mover_personaje(jugador, jugador.velocidad_de_movimiento)
        case "Izquierda":
            if jugador.bandera_esta_saltando == False:
                animar_personaje(pantalla, jugador, jugador.corriendo_mirando_izquierda)
            mover_personaje(jugador, -jugador.velocidad_de_movimiento)
        case "Salta":
            if jugador.bandera_esta_saltando == False:
                jugador.bandera_esta_saltando = True
                jugador.desplazamiento_y = jugador.potencia_salto
        case "Quieto":
            if jugador.bandera_esta_saltando == False:
                if jugador.ultima_direccion == "Derecha":
                    animar_personaje(pantalla, jugador, jugador.quieto_mirando_derecha)
                elif jugador.ultima_direccion == "Izquierda":
                    animar_personaje(pantalla, jugador, jugador.quieto_mirando_izquierda)
    aplicar_gravedad(pantalla, jugador, suelo, lista_plataformas)

def girar_lista_imagenes(lista:list) -> list:
    retorno = []
    for imagen in lista:        
        retorno.append(pygame.transform.flip(imagen, True, False))
    return retorno

def identificar_input(lista_teclas_presionadas:list, pantalla:object, jugador:object):
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

def obtener_rectangulos(objeto:object):
    objeto.diccionario_rectangulos["rectangulo_inferior"] = pygame.Rect(objeto.rectangulo.left, objeto.rectangulo.bottom - 10, objeto.rectangulo.width, 10)
    objeto.diccionario_rectangulos["rectangulo_derecho"] = pygame.Rect(objeto.rectangulo.right - 2, objeto.rectangulo.top, 2, objeto.rectangulo.height)
    objeto.diccionario_rectangulos["rectangulo_izquierdo"] = pygame.Rect(objeto.rectangulo.left, objeto.rectangulo.top, 2, objeto.rectangulo.height)
    objeto.diccionario_rectangulos["rectangulo_superior"] = pygame.Rect(objeto.rectangulo.left, objeto.rectangulo.top, objeto.rectangulo.width, 6)

def dibujar_rectangulos(pantalla:object, diccionario_rectangulos:dict, color:str, grosor:int) -> None:
    for clave in diccionario_rectangulos:
            pygame.draw.rect(pantalla.pantalla, color, diccionario_rectangulos[clave], grosor)

def renderizar_imagen(pantalla:object, imagen:object, x:int, y:int):
    pantalla.pantalla.blit(imagen, (x, y))
