import pygame

pygame.mixer.init()  # Inicializar el módulo mixer de Pygame
sound = pygame.mixer.Sound('C:\Users\Alex Yago Fedczuk\Desktop\Clases\clic.wav')  # Cargar un archivo de sonido

print(type(sound))  # Imprimir el tipo del objeto de sonido

pygame.mixer.quit()