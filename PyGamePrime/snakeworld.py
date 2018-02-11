import pygameprime
import simulation
import pygame
import wrapper_functions
import random
from pygame.locals import *

print("hello")

# definitions imported from simulator
load_image = simulation.load_image
get_sprite_manager = simulation.get_sprite_manager

#definitions imported from wrapper functions

TextBox = wrapper_functions.TextBox

BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
WHITE_ALPHA = (255,255,255,255)

score = 0

class Snake(pygameprime.PyGamePrimeSprite):

    def __init__(self, image_name):
        pygameprime.PyGamePrimeSprite.__init__(self,image_name)  # init the sprite superclass
        self.rect.center = 100, 80
        self.active = 0

    def did_eat_mouse(self):
        global score
        eaten_list =  pygameprime.collide_list(self,rodent_group,1)
        for e in eaten_list :
            print (e)
            score += 1

    def update(self):
        if (self.active) :
            pos=pygame.mouse.get_pos()
            self.rect.midtop = pos
            self.did_eat_mouse()

    def mouse(self):
        if(self.active):
            print ("deactivating")
            self.deactivate()
        else :
            print ("activating")
            self.activate()

    def activate(self):
        self.active = 1

    def deactivate(self):
        self.active = 0

    def keypressed(self, keyinput) :
        if keyinput == K_UP :
            x, y = self.rect.center
            self.rect.center = x, y - 5
            self.collision = self.collide( walls)
            if self.collision == None :
                print ('no collision')
                self.did_eat_mouse()
            else :
                print ('collision')
                self.rect.center = x , y
                return
        elif keyinput == K_DOWN :
            x, y = self.rect.center
            self.rect.center = x, y + 5
            self.collision = self.collide(walls)
            if self.collision == None :
                self.did_eat_mouse()
            else :
                self.rect.center = x , y
                return
        elif keyinput == K_LEFT :
            x, y = self.rect.center
            self.rect.center = x - 5, y
            self.collision = self.collide(walls)
            if self.collision == None :
                self.did_eat_mouse()
            else :
                self.rect.center = x , y
                return
        elif keyinput == K_RIGHT :
            x, y = self.rect.center
            self.rect.center = x + 5, y
            self.collision = self.collide(walls)
            if self.collision == None :
                self.did_eat_mouse()
            else :
                self.rect.center = x , y
                return

    def keyreleased(self, keyinput):
        return

class StartScreenSnake(Snake):
    def __init__(self, image_name):
        Snake.__init__(self,image_name)  # init the sprite superclass
        self.image=pygame.transform.scale(self.image,(320,240))
        self.rect=self.image.get_rect()
        self.rect.center = 320,240
        self.active = 0

    def mouse(self):
        next_scene = pygame.event.Event(simulation.NEXT_SCENE)
        pygame.event.post(next_scene)

    def keypressed(self, keyinput):
        return

class Rodent(pygameprime.PyGamePrimeSprite) :
    def __init__(self,image_name):
        pygameprime.PyGamePrimeSprite.__init__(self, image_name)  # init the sprite superclass
        print("rodent:", self.image)
        self.scale((40, 30))
        print("rodent:", self.image)
        self.y_direction = 1
        self.x_direction = 1
        y = random.randint(0, 400)
        x = random.randint(0, 600)
        self.rect.center = x, y
        self.collision = self.collide (walls)
        if self.collision == None :
            return
        else :
            print ('found collision')
            while self.collision != None :
                y = random.randint(0, 400)
                x = random.randint(0, 600)
                self.rect.center = x, y
                self.collision = self.collide(walls)
            print ('moved rodent')
            return

    def update (self) :
        x , y = self.rect.center
        snakex, snakey = snake1.location()
        print ("snake is at:", snakex, snakey)
        snakex_distance = snakex - x
        if (0 >= snakex_distance) :
            self.rect.center = x + 5 , y+(self.y_direction*5)
        else :
            self.rect.center = x-5, y+(self.y_direction*5)
        self.collision = self.collide (walls)
        if (self.collision == None) and (y <= 475) and (y>=5) :
            return
        else :
            self.y_direction = self.y_direction * (-1)
            print (self.y_direction)
            self.rect.center = x , y+(self.y_direction*6)

class Walls(pygameprime.PyGamePrimeSprite) :
    def __init__(self,image_name):
        pygameprime.PyGamePrimeSprite.__init__(self,image_name)  # init the sprite superclass
        self.rect.center = 320,240
        print ('Number of mask bits set', self.mask.count())

snake1 = Snake("python3.png")
snake1.scale((30,30))
test_costume = snake1.create_costume("python2.png")
snake1.set_costome(test_costume)
print ("test costume tuple" , test_costume)
snake1.scale((30,30))
snake3 = StartScreenSnake('python1.jpg')
textbox1 = TextBox("Click the snake to start",40,BLUE,(320,100))
walls = Walls('Bush_Walls.png')

start_screen = get_sprite_manager()
start_screen.add_sprite(snake3)
start_screen.add_sprite(textbox1)

game_screen = get_sprite_manager()
game_screen.add_sprite(snake1)
game_screen.add_sprite(walls)



rodent_group = pygame.sprite.Group()
barrier_group = pygame.sprite.Group()
barrier_group.add(walls)

for i in range (1,21) :
    new_rodent = Rodent('rodent1.png')
    print (new_rodent.image)
    game_screen.add_sprite(new_rodent)
    rodent_group.add(new_rodent)

def main():
    simulation.simulator(start_screen, WHITE)
    print (game_screen)
    simulation.simulator(game_screen, GREEN)
    print ('Your score is', score)

if __name__ == "__main__":
    main()