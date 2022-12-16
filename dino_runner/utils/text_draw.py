import pygame
from dino_runner.utils.constants import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH


FONT_COLOR = (0, 0, 0)
FONT_SIZE = 30
FONT_STYLE = "dino_runner/utils/Fonts/Fixedsys500c.ttf"


def text_draw(message, screen, 
              font_color = FONT_COLOR, 
              font_size = FONT_SIZE, 
              pos_y_center = HALF_SCREEN_HEIGHT, 
              pos_x_center = HALF_SCREEN_WIDTH
              ):
    
   
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)
   