from random import randint
import pygame
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import HAMMER_TYPE, HEART_TYPE, SHIELD_TYPE, SOUND_POWERUP, VOLUME


class PowerUpManager:
    def __init__(self):
        self.power_ups: list[PowerUp] = []
        self.when_appears = 0
        
    def generate_power_up(self, score):
        if not self.power_ups and self.when_appears == score:
            power_random = randint(0, 2)
            if power_random == 0:
                self.power_ups.append(Shield())
            elif power_random == 1:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(Heart())
 
            self.when_appears += randint(200, 300)
        
    def update(self, game_speed, score, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            #? Valido que el tipo de pu sea distinto al heart
            if power_up.rect.colliderect(player.rect):
                self.sound_powerup()
                if (power_up.type == SHIELD_TYPE) or (power_up.type == HAMMER_TYPE):
                    power_up.start_time = pygame.time.get_ticks()
                    player.on_pick_power_up(power_up)
                    self.power_ups.remove(power_up)
                    
                elif power_up.type == HEART_TYPE:
                    if power_up.rect.colliderect(player.rect): #
                        self.power_ups.remove(power_up)
                        player.lifes += 1
                                   
              
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
     
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = randint(200, 300)
     
    def sound_powerup(self):
        pygame.mixer.Sound.play(SOUND_POWERUP)
        pygame.mixer.Sound.set_volume(SOUND_POWERUP, VOLUME)
        
        
