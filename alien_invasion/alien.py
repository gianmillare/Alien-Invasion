import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class for the aliens and alien fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set the rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start a new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens position
        self.x = float(self.rect.x)
