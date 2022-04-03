import math
import pygame
from colours import colours

class Gun(pygame.sprite.Sprite):
    def __init__(self, player):
        # Calling the parent Classe's __init__ method
        super().__init__()

        # Setting Core attributes
        self.image = pygame.image.load('./assets/gun.png').convert_alpha()
        self.width, self.height = self.image.get_size()
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect(left=player.rect.left, top=player.rect.top)
        self.correction_angle = 90
        
        # Filling the gun with grey
        self.image.fill(colours['white'])
    
    def rot_center(self, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = self.image.get_rect()
        rot_image = pygame.transform.rotate(self.image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    
    def update(self, player):
        self.rect.center = player.rect.center
        
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
        # angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        
        # w, h = self.image.get_size()
        # box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        # box_rotate = [p.rotate(angle) for p in box]
        # min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        # max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        # origin = (player.rect.center[0] + min_box[0], player.rect.center[1] - max_box[1])
        # self.image = pygame.transform.rotate(self.image, angle)
        # self.rect.topleft = origin