import pygame
import math
from colours import colours
from base import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, mouse_x, mouse_y, player_x, player_y, x, y):
        # Calling the parent Classe's __init__ method
        super().__init__()

        # Setting Core attributes
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Setting Key Movement Attributes
        self.speed = 15
        self.angle = math.atan2(player_y-mouse_y, player_x-mouse_x)
        self.direction = pygame.math.Vector2(int(math.cos(self.angle) * self.speed),
int(math.sin(self.angle) * self.speed))
        
        # Filling the tile with grey
        self.image.fill(colours['green'])
    
    def collision_detection(self, tiles, bul_list):
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                # print('Collision')
                bul_list.remove(self)
                del self
    
    def update(self, tiles, bullet_list):
        self.rect.x -= self.direction.x
        self.rect.y -= self.direction.y
        self.collision_detection(tiles, bullet_list)