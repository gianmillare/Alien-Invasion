import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class made for bullets"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet at rect (0,0) and set the position as the ship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, seld.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Have the bullet appear on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)