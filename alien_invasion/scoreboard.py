import pygame.font

class Scoreboard:
    """Class to hold at scoring functions"""

    def __init__(self, ai_game):
        """Initialize scoring attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial score
        self.prep_score()
