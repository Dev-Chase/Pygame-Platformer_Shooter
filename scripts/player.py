import pygame
from colours import colours
from base import SCREEN_HEIGHT, SCREEN_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, spwn_pnt=(SCREEN_WIDTH//4, 0)):
        # Calling the parent Classe's __init__ method
        super().__init__()

        # Setting Core attributes
        self.image = pygame.image.load('./assets/player.png').convert()
        self.rect = self.image.get_rect(topleft=pos)
        self.spwn_pnt = spwn_pnt
        
        # Setting Movement Attributes
        self.wlksp = 6
        self.jump_move = -7
        self.grv = .3
        self.can_jump = 0
        self.move = pygame.math.Vector2(0, 0)
        self.is_dead = True
        
        # Setting KeyPress Attributes
        self.left_pressed = False
        self.right_pressed = False
        self.jump_pressed = False
    
    def vertical_collision(self, tiles):
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.move.y > 0:
                    self.can_jump = 6
                    self.rect.bottom = tile.rect.top
                    self.move.y = 0
                elif self.move.y < 0:
                    self.rect.top = tile.rect.bottom
                    self.move.y = 0
                else: print('wtf')

    def horizontal_collision(self, tiles):
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.move.x > 0:
                    self.rect.right = tile.rect.left
                    self.move.x = 0
                elif self.move.x < 0:
                    self.rect.left = tile.rect.right
                    self.move.x = 0
                else: print('wtf')
    
    def update(self, tiles, gun):
        gun.update(self)
        keys = pygame.key.get_pressed()
        
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.right_pressed = True
            self.move.x = 1*self.wlksp
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not (keys[pygame.K_RIGHT] or keys[pygame.K_d]): 
            self.left_pressed = True
            self.move.x = -1*self.wlksp
            
        if keys[pygame.K_SPACE]: self.jump_pressed = True
        
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_d] and not keys[pygame.K_a] and not keys[pygame.K_LEFT]:
            self.move.x = 0
        
        if not keys[pygame.K_SPACE]:
            self.jump_pressed = False
        
        # Applying Gravity
        self.move.y += self.grv
        
        # Checking if Player can Jump
        self.can_jump -= 1
        if self.can_jump > 0 and self.jump_pressed:
            self.move.y = self.jump_move
            self.can_jump = 0
        
        # Applying Vertical Movement
        self.rect.y += self.move.y
        # Checking for Vertical Collision
        self.vertical_collision(tiles)
        
        # Applying Horizontal Movement
        self.rect.x += self.move.x
        # Checking for Horizontal Collision
        self.horizontal_collision(tiles)

        if self.rect.top+30 > SCREEN_HEIGHT:
            self.is_dead = True

        if self.is_dead:
            self.rect.topleft = self.spwn_pnt
            self.is_dead = False

