import sys
import pygame

class AlienInvasion:
    """Overall Class"""
    
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        # Backgrounf Color
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Begin game loop"""
        while True:
            #monitor keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each loop
            self.screen.fill(self.bg_color)
                    
            # Make the most recent screen visible
            pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance
    ai = AlienInvasion()
    ai.run_game()
