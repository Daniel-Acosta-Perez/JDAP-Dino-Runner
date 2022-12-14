from random import randint
import pygame
from dino_runner.components.obstaculo.cactus import Cactus, CactusLarge
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            self.cactus_use()
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False
                       
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def cactus_use(self):
        self.INDEX_LIST = randint(0, 1)

        if self.INDEX_LIST == 0:
            return self.obstacles.append(Cactus(SMALL_CACTUS))
        else:
            return self.obstacles.append(CactusLarge(LARGE_CACTUS))
        