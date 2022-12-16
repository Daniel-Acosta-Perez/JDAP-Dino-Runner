import pygame
from dino_runner.components.button import Button
from dino_runner.components.cloud import Cloud
from dino_runner.components.dino import Dinosaur
from dino_runner.components.obstaculo.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.powerUpManager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import (BG, DINO_START, GAME_OVER, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, HAMMER_TYPE, 
                                         ICON, INICIAL_GAME_VELOCITY, LIFES, SCREEN_HEIGHT, 
                                         SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS)
from dino_runner.utils.text_draw import text_draw

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.playing = False
        self.game_speed = INICIAL_GAME_VELOCITY
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        
        self.score = Score()
        self.cloud = Cloud() 
        self.death_count = 0 
        self.button = Button()
        self.executing = False
        
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
            
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        #self.reset_game() #TODO: Se puede usar pero no cuenta las muertes
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()                   

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False           

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.power_up_manager.update(self.game_speed, self.score.points, self.player)
        self.score.update(self)
        self.cloud.update(self) 

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.cloud.draw(self.screen) 
        self.player.draw(self.screen)
        self.player.draw_active_power_up(self.screen)
        self.player.draw_life(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.screen)
        
        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.screen.fill((255, 248, 220)) 
        
        if self.player.lifes > 0:
            self.screen.blit(DINO_START, (HALF_SCREEN_WIDTH - 40, HALF_SCREEN_HEIGHT - 140))        
            text_draw("Press any key to start.",self.screen, pos_y_center= HALF_SCREEN_HEIGHT + 50, font_size=40)
            text_draw(f"Left lifes: : {self.player.lifes}", self.screen, font_size = 20, pos_y_center = HALF_SCREEN_HEIGHT + 80)
        elif self.player.lifes < 1:
            self.screen.blit(GAME_OVER, (HALF_SCREEN_WIDTH - 190, HALF_SCREEN_HEIGHT - 200))
            self.button.draw(self.screen) 
            text_draw("Press any key to continue.", self.screen, pos_y_center=HALF_SCREEN_HEIGHT-60)
            text_draw(f"Your score is: {self.score.points}", self.screen, font_size = 25, pos_y_center = HALF_SCREEN_HEIGHT + 20)
            
        pygame.display.update()        
        
        self.handle_menu_events()
        
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN and self.player.lifes > 0:
                self.score.reset_score()
                self.game_speed = INICIAL_GAME_VELOCITY
                self.obstacle_manager.reset_obstacles()
                self.power_up_manager.reset_power_ups()
                self.run()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_button(mouse_pos)

#? Metodos nuevos        
        
    def check_button(self, mouse_pos):
        if self.button.rect.collidepoint(mouse_pos):
            self.reset_game()
            self.run()

    def reset_game(self):
        self.player.lifes = LIFES
        self.game_speed = INICIAL_GAME_VELOCITY
        self.obstacle_manager.reset_obstacles()
        self.score.reset_score()
        self.power_up_manager.reset_power_ups()
        
    def on_death(self):
        has_shield = (self.player.type == SHIELD_TYPE) or (self.player.type == HAMMER_TYPE)
        if not has_shield:
            self.player.on_dino_dead()
            self.draw()
            self.player.lifes -= 1
            self.playing = False

        return not has_shield

        
    def hammer_colision(self):
        pass