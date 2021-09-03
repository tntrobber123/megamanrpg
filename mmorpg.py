import pygame
import constants
import levels
import time
import random
from spritesheet_functions import SpriteSheet
from player import Player

def main():
    """ Main Program """
    pygame.init()
    done = False
    clock = pygame.time.Clock()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("MEGAMAN RPG")
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))
    level_list.append(levels.Level_04(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 100
    player.rect.y = 200
    active_sprite_list.add(player)
    
    move = 0
    randenc = random.randint(5, 50)

    php = 10
    pdmg = 5
    pnrg = 5

    ehp = 10
    edmg = 5
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()
                if event.key == pygame.K_ESCAPE:
                    pygame.QUIT()
        
            if event.type == pygame.KEYUP:
                player.stop()  
        
        """CODE FOR RANDOM ENCOUNTERS GOES HERE"""
        if player.steps > randenc:
            enemy = []
            enemy.append("sniper joe")
            enemy.append("boss")
            enemy.append("met")
            
            elist = random.randint(0, 2)
            if php > 0 or ehp > 0:
                eprint = enemy[elist]
                print("You are attacked by a", (eprint) )
                
            player.steps = 0
                
        active_sprite_list.update()
        current_level.update()

        # If player gets near the right side, shift the world left (-x)
        if player.rect.x >= 1000:
            diff = player.rect.x - 1000
            player.rect.x = 1000
            current_level.shift_world(-diff)
        current_positionx = player.rect.x + current_level.world_shift
        current_positiony = player.rect.y   
        # If player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
        current_positionx = player.rect.x + current_level.world_shift
        current_positiony = player.rect.y 
        
        # If player gets near the top, shift the world up (+y)
        if player.rect.y <= 1:
            diff = 1 - player.rect.y
            player.rect.y = 1
            current_level.shift_worldy(diff)
        current_positionx = player.rect.x
        current_positiony = player.rect.y + current_level.world_shifty      

        if player.rect.y >= 460:
            diff = 460 - player.rect.y
            player.rect.y = 460
            current_level.shift_worldy(diff)
        current_positionx = player.rect.x
        current_positiony = player.rect.y + current_level.world_shifty
        
        # Change the level
        if current_positionx < current_level.level_limitx and current_positiony < current_level.level_limity:
            if current_level_no == 0:
                current_level_no = 1
                current_level = level_list[current_level_no]
                player.level = current_level
                
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()