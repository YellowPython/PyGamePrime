# Snakeworld is an example game that was written in pygame prime.
# The comments explain how to build your own games in pygame prime


import pygameprime     #this loads the code that implements the pygame prime functions
import simulation      #this loads the simulation engine that processes mouse and keyboard events
import pygame          #this loads the pygame framework that pygame prime uses
import wrapper_functions        #this loads a set of functions to make using pygameprime easier
import random                   #this loads a random number generator
from pygame.locals import *     #this loads a set of pygame variables




print("hello")   #print "hello" to the screen so that you know the code got to this point

# definitions imported from simulator.  These let you call functions from the simulator without having to use simulator.function
load_image = simulation.load_image
get_sprite_manager = simulation.get_sprite_manager

#definitions imported from wrapper functions

#The textbox object lets you print formatted text boxes to the game window.  This command creates a textbox object to use
#in the game

TextBox = wrapper_functions.TextBox

#Colors in pygameprime are represented by RGB values (Red, Green,Blue) - you represent each amount of red, green, or bule with
#a number between 0 and 255.  You can give these numbers names so that you can easily use them.  For example BLUE = (0,0,255)
#this translates to 0 red, 0 green, and 255 (maximum) bule.  Green is (0,255,0),  you can make other colors by makeing different
#combinations of red, green and blue.

BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
WHITE_ALPHA = (255,255,255,255)

#set the initial score to 0.  Every time the snake eats a mouse, the score witll increment

score = 0

#Now, define the Snake object - to do this you implement methods to tell the snake what to do when mouse and keyboard events
#are sent to it by the simulator.

#All pygameprie sprites "inherit" the pygrameprime "PyGamePrimeSprite" object.  This will allow the Snake object to use all the code
#from the base sprite pbject implemented in pygame prime.  This inheritance is don by including "pygameprime.PyGamePrimeSprite, in the
#parenthesis below:

class Snake(pygameprime.PyGamePrimeSprite):

#Initialize the sprite, you have to do this for every sprite you use

    def __init__(self, image_name):  #pass the name of the image you want to use for the sname as "image_name"
        pygameprime.PyGamePrimeSprite.__init__(self,image_name)  # init the sprite superclass
        self.rect.center = 100, 80 #define the size of the snake sprite
        self.active = 0 #in this example, the active variable is used to determine whether to repsond to keyboard and mouse events -
    # the snake starts out inactive.

    def did_eat_mouse(self):   #check if the snake has eaten a mouse
        global score           #when the snake eats a mose we will increment the score, so define this here

        #Next we will see if the snake has run into any mice - we use the pygame prime function "collide_list" to check
        #if the snake has collided with any of the mice that are still uneated.  The mice are kept in the "rodent_group".\
        #we will show how the rodent_group is defined later in the code.   The mice that are eaten are returned in the variable
        #"eaten_list".

        eaten_list =  pygameprime.collide_list(self,rodent_group,1)

        #loop through all the mice in the "eaten_list" and add one to the score for each mouse.

        for e in eaten_list :
            print (e)
            score += 1

    #now we will respond to an update

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