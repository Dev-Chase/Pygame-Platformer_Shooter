import numpy
import pygame
import sys
from random import seed, randint
from colours import colours
from base import *
from tile import Tile
from player import Player
from gun import Gun
from bullet import Bullet

# Pygame Setup
pygame.init()
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
screenshake = 0
offs = (0, 0)
display = pygame.Surface(SCREEN_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Platformer Shooter')

# Creating Sprite Groups
tiles = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle()
player_bullets = pygame.sprite.Group()
gun_group = pygame.sprite.GroupSingle()

# Creating Sprites
floor = Tile((0, SCREEN_HEIGHT-250), (SCREEN_WIDTH-200, 75))
player = Player((SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
gun = Gun(player)

# Adding Sprites to Sprite Groups
tiles.add(floor)
player_group.add(player)
gun_group.add(gun)

# Global Game Variables go here
is_left_btn_dwn = False
gun_cooldown = 0

seed(randint(0, 9999999999999999999999999999999))
while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: is_left_btn_dwn = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: is_left_btn_dwn = False
            
    # Game Logic goes here
    gun_cooldown -= 1
    if is_left_btn_dwn and gun_cooldown < 0:
        player_bullets.add(Bullet(mouse_x, mouse_y, player.rect.center[0], player.rect.center[1], player.rect.midleft[0], player.rect.midleft[1]))
        gun_cooldown = 10
    player_group.update(tiles, gun)
    player_bullets.update(tiles, player_bullets)
        
    display.fill(colours['black'])
    
    # Drawing Code goes here
    tiles.draw(display)
    player_group.draw(display)
    gun_group.draw(display)
    player_bullets.draw(display)
    
    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), offs)
    
    pygame.display.update()
    clock.tick(60)