import pygame

class Bang(pygame.sprite.Sprite):

    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenDisparo = pygame.image.load("../Imagenes/disparo.png").convert_alpha()
        self.ImagenDisparo = pygame.transform.flip(self.ImagenDisparo, False, False)
        self.rect = self.ImagenDisparo.get_rect()
        self.VelDis = 20
        self.rect.top=posY
        self.rect.left=posX

    def shoot(self):
        self.rect.left = self.rect.left+self.VelDis

    def dibuja(self, superficie):
        superficie.blit(self.ImagenDisparo, self.rect)
