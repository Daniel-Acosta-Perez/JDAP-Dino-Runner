import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

jumping_action = "jumping"
running_action = "running"
ducking_action = "ducking"

class Dinosaur(Sprite):
    y_pos = 310
    x_pos = 80
    
    JUMP_VELOCITY = 8.5
    
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0
        self.action = running_action
        self.y_pos_duck = 340
              
    def update(self, user_input):
        if self.action == running_action:  
            self.run()
            
        elif self.action == jumping_action:
            self.jump()
        
        elif self.action == ducking_action:
            self.duck()
            
        if self.action != jumping_action:
            if (user_input[ pygame.K_UP]) and (self.action != jumping_action):
                self.action = jumping_action
            
            elif user_input[pygame.K_DOWN]:
                self.action = ducking_action
                
            else:
                self.action = running_action
        
        if self.step >= 9:
            self.step = 0
            
    def run(self):
        self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.rect.y = self.y_pos
        self.rect.x = self.x_pos
        self.step += 1
        
    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
            
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.rect.y = self.y_pos
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = running_action
            
    def duck(self):
        self.image = DUCKING[0] if self.step < 5 else DUCKING[1]
        self.rect.y = self.y_pos_duck
        self.step += 1
        

        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))
        
        
    


