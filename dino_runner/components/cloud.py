from random import randint
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud:
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.x_pos = self.screen_width + randint(800, 1100)
        self.y_pos = randint(50, 130)
        self.image = CLOUD
        self.width = self.image.get_width()
    
    def update(self, game):
        self.x_pos -= game.game_speed
        if self.x_pos < -self.width:
            self.x_pos = self.screen_width + randint(1000, 2000)
            self.y_pos = randint(50, 100)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))
