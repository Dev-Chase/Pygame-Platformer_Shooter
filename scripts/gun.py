import math
import pygame
from colours import colours

class Gun(pygame.sprite.Sprite):
    def __init__(self, player):
        # Calling the parent Classe's __init__ method
        super().__init__()

        # Setting Core attributes
        self.image = pygame.Surface((28, 10)).convert_alpha()
        self.rect = self.image.get_rect(left=player.rect.left, top=player.rect.top)
        self.correction_angle = 90
        
        # Filling the gun with grey
        self.image.fill(colours['white'])
    
    def update(self, player):
        self.rect.midleft = player.rect.center
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('nice')
                mx, my = pygame.mouse.get_pos()
                dx, dy = mx - self.rect.centerx, my - self.rect.centery
                angle = math.degrees(math.atan2(-dy, dx)) - self.correction_angle

                self.image = pygame.transform.rotate(self.image, angle)
                self.rect = self.image.get_rect(center = player.rect.center)