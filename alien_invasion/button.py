import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Sysfont(None, 48)

        # Build the buttones rect object and center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare the button
        self.prep_msg(msg)
