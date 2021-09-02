import pygame
import constants
import time
black = (0,0,0)
from spritesheet_functions import SpriteSheet

SCREEN_WIDTH  = 1400
SCREEN_HEIGHT = 550

size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
sprite_sheetd = SpriteSheet("p1_walk_f.png")
def imgloadf(x1, y1, x2, y2):
    image = sprite_sheetd.get_image(x1, y1, x2, y2)
    walking_frames_d.append(image)
    
walking_frames_d = [] 


imgloadf(0, 0, 58, 72)

x = 0

while True:
    surf = walking_frames_d[x]
    screen.fill(black)
    screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    pygame.display.flip()
    x += 1
    time.sleep(1)