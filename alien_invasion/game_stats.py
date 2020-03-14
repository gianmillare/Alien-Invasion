class GameStats:
    """Tracking statistics from the game"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Statistics change throughout the game"""
        self.ships_left = self.settings.ship_limit
