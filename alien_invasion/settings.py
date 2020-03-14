class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game STATIC settings"""
        # Screen Settings
        # self.screen_width = 1200
        # self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien Settings
        self.fleet_drop_speed = 30.0

        # How quickly the game will speed up
        self.speedup_scale = 1.3
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize the game settings that change throughout the game"""
        self.ship_speed = 15
        self.bullet_speed = 50
        self.alien_speed = 4.0

        # directions are represented by 1 = right & -1 = left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed settings and difficulty"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

