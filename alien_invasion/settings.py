class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 15
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 50
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien Settings
        self.alien_speed = 7.5
        self.fleet_drop_speed = 50.0
        # directions are represented by 1 = right & -1 = left
        self.fleet_direction = 1

