import pygame
import os
import sys
from pygame.locals import *
from pathlib import Path

home = str(Path.home())
image_path = home+"/Documents/PycharmProjects/Data/images"
sound_path = home+"/Documents/PycharmProjects/Data/sounds"


print("Simulator starting")

GREEN = (0,255,0)

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Python game engine")
pygame.mouse.set_visible(0)

NEXT_SCENE=USEREVENT + 1

def load_image(name, colorkey=None) :
    fullname = os.path.join(image_path,name)
#    print (fullname)
    try:
        image = pygame.image.load(fullname)
        image.set_colorkey(colorkey)
    except pygame.error as message:
        print ('cannot find file' , name)
        raise SystemExit(message)
    if name.find('png') != -1 :
        image = image.convert_alpha()
    else :
        image = image.convert()
    return image, image.get_rect()

class sprite_manager  :
    def __init__(self):
        print ("sprite manager started")
        self.sprite_group = pygame.sprite.Group()
        print (self.sprite_group)

    def sprite_list(self):
        return self.sprite_group

    def add_sprite (self,new_sprite):
        self.sprite_group.add(new_sprite)

    def remove_sprite (self,old_sprite):
        self.sprite_group.remove(old_sprite)

def get_sprite_manager ():
    print ('getting sprite manager')
    return sprite_manager()


background = pygame.Surface(screen.get_size())
background = background.convert()
screen.blit(background, (0,0))
pygame.display.flip()
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)


def simulator(manager1,background_color) :
    print ('starting simulation')
    pygame.key.set_repeat(10,10)
    background.fill(background_color)
    while 1:
        clock.tick(60)
        for event in pygame.event.get() :
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE :
                return
            elif event.type == MOUSEBUTTONDOWN :
                pos = pygame.mouse.get_pos()
                for s in manager1.sprite_list() :
                    if s.rect.collidepoint(pos) :
                        s.mouse()
            elif event.type == KEYDOWN :
                for s in manager1.sprite_list():
                    s.keypressed(event.key)
            elif event.type == KEYUP :
                for s in manager1.sprite_list():
                    s.keyreleased(event.key)
            elif event.type == NEXT_SCENE :
                return


        manager1.sprite_list().update()
        screen.blit(background, (0,0))
        manager1.sprite_list().draw(screen)
        pygame.display.flip()

