import pygame
from dino_runner.utils.constants import FONT_STYLE
from dino_runner.utils.text_draw import text_draw

class Score:
    def __init__(self):
        self.points = 0
        
    def update(self, game):
        self.points += 1
        if self.points % 200 == 0:
            game.game_speed += 2
        
        
    def draw(self, screen):
        
        text_draw(
            f"Score: {self.points}",
            screen, font_size = 20, 
            pos_x_center = 1000, 
            pos_y_center = 30
        )
    
    def reset_score(self):
        self.points = 0