import numpy
import pygame
import sys
from random import seed, randint
from colours import colours
from base import *
from tile import Tile
from player import Player

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
players = pygame.sprite.GroupSingle()

# Creating Sprites
floor = Tile((0, SCREEN_HEIGHT-100), (SCREEN_WIDTH-200, 75))
player = Player((SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (32, 64))

# Adding Sprites to Sprite Groups
tiles.add(floor)
players.add(player)

seed(randint(0, 9999999999999999999999999999999))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Game Logic goes here
    player.update(tiles)
    
    display.fill(colours['black'])
    
    # Drawing Code goes here
    tiles.draw(display)
    players.draw(display)
    
    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), offs)
    
    pygame.display.update()
    clock.tick(60)