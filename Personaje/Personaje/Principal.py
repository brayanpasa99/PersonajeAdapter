import pygame
import sys
from pygame.locals import *

from Personaje.Jocker import *

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 237


def juego():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Personaje")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("../Imagenes/fondo.jpg").convert()
    risajoker = pygame.mixer.music.load("../Sonido/joker.mp3")

    # El bucle principal del juego

    ejecutando = True

    Jock = Jocker()
    while ejecutando:

        screen.blit(fondo, (0, 0))
        Jock.dibuja(screen)

        if len(Jock.listaDisparo)>0:
            for x in Jock.listaDisparo:
                x.dibuja(screen)
                x.shoot()
                if x.rect.left<-10:
                    Jock.listaDisparo.remove(x)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:
            pygame.mixer.music.play(1)
            x,y = Jock.rect.center
            Jock.disparando(x,y)
        pygame.display.update()


# Llamada a la función principal
juego()
