import pygame

WHITE = (255,255,255)

# Function for scaling a sprite


# Class for creating a text box sprite
class TextBox(pygame.sprite.Sprite):
    def __init__(self, text, size, color,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial" , size)
        self.image = self.font.render(text, 1, color,WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = location

    def mouse(self):
        return
