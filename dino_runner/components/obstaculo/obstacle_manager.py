from random import randint
import pygame
from dino_runner.components.obstaculo.bird import Bird
from dino_runner.components.obstaculo.cactus import Cactus, CactusLarge
from dino_runner.components.score import Score
from dino_runner.utils.constants import BIRD, DINO_DEAD, LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
    
    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            self.obstacle_use()
            
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.colliderect(player.rect) and on_death():
                pygame.time.delay(500)
                
    def obstacle_use(self):
        self.NUMBER_RANDOM = randint(0, 2)

        if self.NUMBER_RANDOM == 0:
            return self.obstacles.append(Cactus(SMALL_CACTUS))
        elif self.NUMBER_RANDOM == 1:
            return self.obstacles.append(CactusLarge(LARGE_CACTUS))
        else:
            return self.obstacles.append(Bird(BIRD))
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
    def reset_obstacles(self):
        self.obstacles = []
    
