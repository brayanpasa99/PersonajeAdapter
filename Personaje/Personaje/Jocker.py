import pygame, sys
from Bang import *


class Jocker(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPersonaje = pygame.image.load("../Imagenes/Guason.png").convert_alpha()

        self.rect = self.ImagenPersonaje.get_rect()

        self.rect.x = 20
        self.rect.y = 10

        self.listaDisparo = []

    def disparando(self, x, y):
        disparo = Bang(x, y)
        self.listaDisparo.append(disparo)

    def dibuja(self, screen):
        screen.blit(self.ImagenPersonaje, self.rect)
