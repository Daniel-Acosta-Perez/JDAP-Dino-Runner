from dino_runner.utils.constants import (BUTTON_RESTART, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH)


class Button:

    X_POS_BUTTON = HALF_SCREEN_WIDTH - 40
    Y_POS_BUTTON = HALF_SCREEN_HEIGHT - 120
    
    def __init__(self):
        self.image = BUTTON_RESTART
        self.rect = self.image.get_rect() 
        self.rect.x = self.X_POS_BUTTON
        self.rect.y = self.Y_POS_BUTTON

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
