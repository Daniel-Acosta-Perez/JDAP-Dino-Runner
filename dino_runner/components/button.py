from dino_runner.utils.constants import BUTTON_RESTART, SCREEN_HEIGHT, SCREEN_WIDTH


class Button:
    half_screen_width = SCREEN_WIDTH // 2 
    half_screen_height = SCREEN_HEIGHT // 2
    
    X_POS_BUTTON = half_screen_width - 40
    Y_POS_BUTTON = half_screen_height - 120
    
    def __init__(self):
        self.image = BUTTON_RESTART
        self.rect = self.image.get_rect() 
        self.rect.x = self.X_POS_BUTTON
        self.rect.y = self.Y_POS_BUTTON

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
