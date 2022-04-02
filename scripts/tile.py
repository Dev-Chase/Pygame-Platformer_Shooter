import pygame
from colours import colours

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        # Calling the parent Classe's __init__ method
        super().__init__()

        # Setting Core attributes
        self.image = pygame.Surface(size).convert()
        self.rect = self.image.get_rect(topleft=pos)
        
        # Filling the tile with grey
        self.image.fill(colours['grey'])