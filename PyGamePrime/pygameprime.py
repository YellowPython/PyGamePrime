import random

import pygame
import os
import sys
from pygame.locals import *
import simulation
import wrapper_functions

class PyGamePrimeSprite(pygame.sprite.Sprite):

    def __init__(self, image_name):
        pygame.sprite.Sprite.__init__(self)  # init the sprite superclass
        self.image, self.rect = simulation.load_image(image_name)
        self.active = 0
        print ("pygameprime init:", self.image)
        self.mask = pygame.mask.from_surface(self.image)

    def scale(self,pixel_size):
        self.image = pygame.transform.scale(self.image, pixel_size)
        self.rect = self.image.get_rect()
#        print("pygame scale", self.image)
        self.mask = pygame.mask.from_surface(self.image)

    def create_costume (self, image_name) :
        costume , size = simulation.load_image(image_name)
        mask = pygame.mask.from_surface(costume)
        return (costume,size,mask)

    def set_costome(self,costume) :
        self.image = costume[0]
        self.rect = costume[1]
        self.mask = costume[2]

    def update (self):
        pass

    def mouse(self):
        pass

    def keypressed(self, keypressed) :
        pass

    def keyreleased(self, keyreleased) :
        pass

    def location(self):
        return self.rect.center

    def collide (self, sprite1) :
        return pygame.sprite.collide_mask(self, sprite1)

def collide_list (sprite1, sprite_list, delete):
    return pygame.sprite.spritecollide(sprite1, sprite_list, delete)
