class GameStats:
    """Tracking statistics from the game"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game at an inactive state
        self.game_active = False

        # High scores do not reset
        self.high_score = 0


    def reset_stats(self):
        """Statistics change throughout the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0 #This resets the scoreboard
        self.level = 1 #This displays the current level
