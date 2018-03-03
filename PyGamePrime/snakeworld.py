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

    def __init__(self, image_name):  #pass the name of the image you want to use for the sprite as "image_name"
        pygameprime.PyGamePrimeSprite.__init__(self,image_name)  # init the sprite superclass
        self.rect.center = 100, 80 #define the size of the snake sprite
        self.active = 0 #in this example, the active variable is used to determine whether to repsond to keyboard and mouse events -
                        #the snake starts out inactive.

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

    #At every timestep, the simuluator will call the "update" method for every sprite.  If you want something done at every
    #timestep, put it in the update method.  In this case, the snake object checks to see if has eaten a mouse.

    def update(self):
        if (self.active) :
            self.did_eat_mouse()

    #The "mouse" method processes a mouse event.  The simulator will send a mouse event every time the user clicks or moves the mosee.
    #In this sprite, the snake will activate or deactivate whenever it is clicked.  We don't use this at the moment, it's jsut
    #there to show processing a mouse event.

    def mouse(self):
        if(self.active):
            print ("deactivating")
            self.deactivate()      #If the snake is currently active, deactivate
        else :
            print ("activating")
            self.activate()        #if the snake is currently inactive, activate

    def activate(self):
        self.active = 1

    def deactivate(self):
        self.active = 0

    #The keypressed method deals with keyboard events sent by the simulator.  Each key has a name.
    #In our case, the keys we are interested in are K_UP (up arrow), K_DOWN (down arrow), K_LEFT (left arrow)
    #and K_RIGHT (right arrow).  When we get these events from the simulator, we will move the snake.

    def keypressed(self, keyinput) :
        if keyinput == K_UP :   #respond to an up arrow key press
            x, y = self.rect.center   #find the current location of the snake
            self.rect.center = x, y - 5  #move 5 pixels up (higher o the screen has a lower y coordinate value)
            self.collision = self.collide( walls) #check if the shanke will collide with the wall sprite
            if self.collision == None :  #if there is no colition, go on to check if the snake ate a mouse
                print ('no collision')
                self.did_eat_mouse()     #call the did_eat_mouse method to check if a mouse was eaten
            else :
                print ('collision')      #there is a collision with the wall sprite, so the snake can't move
                self.rect.center = x , y #set the snake location back to where it was before the mehod call
                return
        #process other keyboard direction events the same way and the K_UP event

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

#The following is a specialized snake class for the snake that appears on the start screen.
#It inherits all the methods from the Snake class.  If it has it's own definition of a method, the
#new one overrides the inherited one.

class StartScreenSnake(Snake):      #The "Snake" in the perenthesis here tells this sprite to inherit from the Snake class.
    def __init__(self, image_name): #The image_name here is the name of the image you wnat for the start screen snake
        Snake.__init__(self,image_name)  # init the sprite superclass (in this case the Snake class)
        self.image=pygame.transform.scale(self.image,(320,240))  #Scale the image to the size you want
        self.rect=self.image.get_rect()  #set the new rectange size - pygame uses this for collisions
        self.rect.center = 320,240  #set the location of the sprite by setting the location of the center

    def mouse(self):  #the sprite will send this event when the sprite is clidked on

        #This method uses the pygame event queue to post an event telling the current simulator to exit and
        #start up the next screen.  There's more on this later in the code where we will talk about moving from
        #screen to screen to create multi-screen games.  This is not needed to create a single screen game.
        # When the sprite is clicked on, move on to the next screen
        next_scene = pygame.event.Event(simulation.NEXT_SCENE)
        pygame.event.post(next_scene)

    # This overrides the keypressed method in the snake class so the start screen snake does not move

    def keypressed(self, keyinput):
        return

#Now we define the Rodent class - these are the mice that ths snake is going to eat

class Rodent(pygameprime.PyGamePrimeSprite) :  #the rodent class interits the PyGamePrimeSprite - same as the Snake class
    def __init__(self,image_name):
        #initialize the Rodent class with the image you want for the rodent
        pygameprime.PyGamePrimeSprite.__init__(self, image_name)  # init the sprite superclass
        self.scale((40, 30))   #Scale the image to the size you want
        y = random.randint(0, 400)  #Pick a random number for where to place the rodent in y and x
        x = random.randint(0, 600)
        self.rect.center = x, y     #Place the rodent in that random location
        self.collision = self.collide (walls)  #Check if our random location is inside a wall
        if self.collision == None :  #IF it's not inside a wall, we are done
            return
        else :
            print ('found collision')   #Our rodent is inside a Wall, so we need to move it
            while self.collision != None :
                y = random.randint(0, 400)  #Get a new random location and place the rodent
                x = random.randint(0, 600)
                self.rect.center = x, y
                self.collision = self.collide(walls) #Check again if it is inside a wall
            print ('moved rodent')
            return    #Our rodent is placed, somewhere not in a wall, so return

    def update (self) :   #Update the rodent - it is supposed to run away from the snake, and not run through walls
        x , y = self.rect.center  #get the current location of this rodent
        snakex, snakey = snake1.location() #get the current location of the snake (call the location method for snake1)
        print ("snake is at:", snakex, snakey)  #print where the snake is
        snakex_distance = snakex - x   #Get the x and y distance to the snake
        snakey_distance = snakey - y
        if (0 >= snakex_distance and 0>=snakey_distance) :   #Move the rodent away from the snake unless it has collided with a wall
            self.rect.center = x + 5 , y+5
        elif (0 >= snakex_distance and 0<=snakey_distance) :
            self.rect.center = x + 5,  y-5
        elif (0 <= snakex_distance and 0>=snakey_distance) :
            self.rect.center = x - 5,  y+5
        elif (0 <= snakex_distance and 0>=snakey_distance) :
            self.rect.center = x - 5,  y-5
        self.collision = self.collide (walls)                #Check for a wall collision
        if (self.collision == None) and (y <= 475) and (x<=635) and (y>=5) and (x>=5):
            return   #If there is no collision and the rodent hasn't gone off the screen, return
        else :
            self.rect.center = x , y  #if we would run into a wall or the edge to move away from the snake, stay in our original location

class Walls(pygameprime.PyGamePrimeSprite) :   #Create the wall sprite
    def __init__(self,image_name):
        pygameprime.PyGamePrimeSprite.__init__(self,image_name)  # init the sprite superclass
        self.rect.center = 320,240   #put the wall sprite in the center
        print ('Number of mask bits set', self.mask.count())

 #Create a snake object with the image file "python3.png".  To change what the snake looks like, use a different image
snake1 = Snake("python3.png")
#Make the snake sprite size 30x30
snake1.scale((30,30))
#Create a different image costume for the snake object
test_costume = snake1.create_costume("python2.png")
#Change the costume of the snake to "python2.png"
snake1.set_costome(test_costume)
#Scale the new constume to the right size
snake1.scale((30,30))
#Create a start screen snake opject for the start screen
snake3 = StartScreenSnake('python1.jpg')
#Create a textbox object to put an instruction on the screen
textbox1 = TextBox("Click the snake to start",40,BLUE,(320,100))
#Create a walls object
walls = Walls('Bush_Walls.png')


#Now a bit about the sprite manager.  Each screeen in your game needs a sprite manager to keep track of all the sprites
#This game has 2 screens, the intro screen and the game screen.  We create 2 sprite managers with get_sprite_manager: start_screen
#and game_screen.Then we all the sprites for the start screen to start_screen and the sprites for the game screen to game_screen.
#For every screen, you need to create a sprite manager and add its sprites before the game starts.

start_screen = get_sprite_manager()
start_screen.add_sprite(snake3)
start_screen.add_sprite(textbox1)

game_screen = get_sprite_manager()
game_screen.add_sprite(snake1)
game_screen.add_sprite(walls)

#Next we create the sprite objects - for convenience, we put some of them in groups - rodent_group (for mice)
#and barrier_group for walls.

rodent_group = pygame.sprite.Group()
barrier_group = pygame.sprite.Group()
barrier_group.add(walls)

#We create 21 mice with the for loop - each mouse is added to the game_screen sprite manager, since they will be on the
#game screen.  The are also added to the rodent_group so they are easier to manager later.

for i in range (1,21) :
    new_rodent = Rodent('rodent1.png')
    print (new_rodent.image)
    game_screen.add_sprite(new_rodent)
    rodent_group.add(new_rodent)

def main():
    #call the simululator to start the game.
    simulation.simulator(start_screen, WHITE)
    print (game_screen)
    #when the start screen exits, start the game screen by calling the simulator again
    simulation.simulator(game_screen, GREEN)
    #If you wanted to add a 3rd screen you would call the simulator again here.
    print ('Your score is', score)

if __name__ == "__main__":
    main()