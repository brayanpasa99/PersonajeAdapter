#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php
# https://www.pythonmania.net/es/2010/03/25/tutorial-pygame-2-ventana-e-imagenes/

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import sys

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 237

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------

def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Personaje")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("F:/Proyectos Python/Personaje/Imagenes/fondo.jpg").convert()
    personaje = pygame.image.load("F:/Proyectos Python/Personaje/Imagenes/Guason.png").convert_alpha()
    disparo = pygame.image.load("F:/Proyectos Python/Personaje/Imagenes/disparo.png").convert_alpha()
    risajoker = pygame.mixer.music.load("F:/Proyectos Python/Personaje/Sonido/joker.mp3")

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))
    screen.blit(personaje, (50, 10))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    #El bucle principal del juego

    ejecutando = True
    while ejecutando:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                sys.exit()

        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:

            pygame.mixer.music.play(1)
            screen.blit(disparo, (50, 10))
            pygame.display.flip()


if __name__ == "__main__":
    main()