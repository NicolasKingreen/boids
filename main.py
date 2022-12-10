import pygame, sys
from pygame.locals import *

from flock import Flock


#source: http://www.kfish.org/boids/pseudocode.html
#TODO: wind/current, position tendency, anti-flock behaviour


WIN_SIZE = 640, 420
TARGET_FPS = 60


pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('boids')

flock = Flock()


while True:
    frame_time_ms = clock.tick(TARGET_FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    flock.update()
    
    surface.fill((255, 255, 255))
    flock.draw(surface)
    pygame.display.update()