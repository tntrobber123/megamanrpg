import pygame
import constants
import levels
import time
import random
import loottable
from loottable import commonloot
from loottable import uncommonloot
from loottable import rareloot
from loottable import weaponloot
from loottable import bossloot
from spritesheet_functions import SpriteSheet
from player import Player

time.sleep(.5)
print("Welcome to the Megaman RPG game!")
time.sleep(.5)
print("I am SEMBLANCE, Megamans AI subconscious.")
time.sleep(.5)
print("Are you ready?")
time.sleep(.5)

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
    randenc = random.randint(100, 1000)
    
    enemy = []
    enemy.append("met")
    enemy.append("boss")
    enemy.append("sniper joe")
    php = 10
    pdmg = 5
    pexp = 0
    plvl = 1
    pnxtlvl = 15
    ehp = 0
    
    inventory = []
    invslot = 0
    
    while not done:
        if ehp < 0:
            ehp = 0
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
                    pygame.quit()
                    
                    # Inventory
                if event.key == pygame.K_i:
                    x = 0
                    print("Your inventory contains:")
                    for i in range(len(inventory)):
                        print(x, inventory[invslot])
                        invslot += 1
                        x += 1
                        
                if event.key == pygame.K_RETURN:
                    x = 0
                    print("Your inventory contains:")
                    for i in range(len(inventory)):
                        print(x, inventory[invslot])
                        invslot += 1
                        x += 1
                        
                    print("Use what item?")
                    slot = 0
                    item_use = input(slot)
                    if slot == 0:
                        php += 1000
        
            if event.type == pygame.KEYUP:
                player.stop()  
                invslot = 0
        
        """CODE FOR RANDOM ENCOUNTERS GOES HERE"""
        if php == 0:
            pygame.quit()
        if player.steps > randenc:
            methp = 5
            sjhp = 10
            bosshp = 20
            
            elist = random.randint(0, 1)
            if php > 0 or ehp > 0:
                eprint = enemy[elist]
                print("You are attacked by a", (eprint))
                if elist == 0:
                    ehp = methp
                    edmg = 1
                    loot = 0 #random.randint(0, 1)
                    if loot == 0:
                        inventory.append(commonloot[random.randint(0, 8)])
                    else:
                        pass
                elif elist == 1:
                    ehp = sjhp
                    edmg = 2
                    loot = 0 #random.randint(0, 1)
                    if loot == 0:
                        inventory.append(commonloot[random.randint(0, 8)])
                    else:
                        pass
                    
                while php > 0 and ehp > 0:
                    if elist == 0:
                        metimg = pygame.image.load('met.jpeg')
                        screen.blit(metimg, (50, 50))
                        pygame.display.flip()
                    print("mega punch:a (5 damage)")
                    print("mega buster:b (10 damage)")
                    attack = input()
                    if attack == "a":
                        ehp -= 5
                    if attack == "b":
                        ehp -= 10
                    php = php - 1
                    print(ehp, "enemy hit points")
                    print(php, "my hit points")
                print("he ded")
                
            player.steps = 0
                
        active_sprite_list.update()
        current_level.update()

        # If player gets near the right side, shift the world left (-x)
        if player.rect.x >= 1150:
            diff = player.rect.x - 1150
            player.rect.x = 1150
            current_level.shift_world(-diff)
        current_positionx = player.rect.x + current_level.world_shift
        current_positiony = player.rect.y   
        # If player gets near the left side, shift the world right (+x)
        if player.rect.x <= 0:
            diff = 0 - player.rect.x
            player.rect.x = 0
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