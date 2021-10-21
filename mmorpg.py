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

print("Welcome to Mega Man: Overtaken RPG!")
print("I am SEMBLANCE, Mega Mans AI subconscious. you will use me to controll Mega Man and his actions")
print("Use the arrow keys to walk around. Press i to open your inventory and check stats, and press enter to use an item.")
print("_______________________________________________________________________")

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
    maxhp = 15
    pnrg = 5
    pdmg = 5
    pxp = 0
    plvl = 1
    pnxtlvl = 15
    ehp = 0
    exp = 0
    
    inventory = []
    inventory.append("Small HP ball")
    inventory.append("Small Energy ball")
    invslot = 0
    
    while not done:
        # Level up function
        if pxp >= pnxtlvl:
            pxp = 0
            plvl += 1
            print("Holy smokes! You leveled up!")
            if plvl < 15:
                maxhp += 15
            if plvl >= 15:
                maxhp *= mod
            pnxtlvl = maxhp * mod
            
        mod = (plvl / 10) + 1
            
        if php > maxhp:
            php = maxhp
        
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
                    
                    # CHEATKODES FOR TESTING THE GAME!!!!
                if event.key == pygame.K_3:
                    cheat_code = input()
                    if cheat_code == "lvl.up":
                        plvl += 1
                    if cheat_code == "item.rain":
                        inventory.append("Small HP ball")
                        inventory.append("Small Energy ball")
                        inventory.append("e-TANK")
                        
                        # Inventory
                if event.key == pygame.K_i:
                    x = 0
                    print("____________________________________________")
                    print("HP:", php)
                    print("Max HP:", maxhp)
                    print("Energy:", pnrg)
                    print("XP:", exp)
                    print("XP till levelup:", pnxtlvl - pxp)
                    print("Level:", plvl)
                    print("Your inventory contains:")
                    for i in range(len(inventory)):
                        print(x, inventory[invslot])
                        invslot += 1
                        x += 1
                        
                # Use items
                if event.key == pygame.K_RETURN:
                    x = 0
                    print("____________________________________________")
                    print("Your inventory contains:")
                    for i in range(len(inventory)):
                        print(x, inventory[invslot])
                        invslot += 1
                        x += 1
                    slot = "Use what item? :]"
                    g = input(slot)
                    
                    
                    
                    if g == "0":
                        g = 0
                    if g == "1":
                        g = 1
                    if g == "2":
                        g = 2
                    if g == "3":
                        g = 3
                    if g == "3":
                        g = 4
                    if g == "5":
                        g = 5
                    if g == "6":
                        g = 6
                    if g == "7":
                        g = 7
                    if g == "8":
                        g = 8
                    if g == "9":
                        g = 9
                    
                    if g > len(inventory):
                        print("that item is nonexistant, stupid!")
                        break
                    
                    e = 0
                    while e == 0:
                        if inventory[g] == ("Small HP ball"):
                            php += 5
                            inventory.pop(g)
                            print("HP:", php)
                            e = 1
                        elif inventory[g] == ("Large HP ball"):
                            php += 15
                            inventory.pop(g)
                            print("HP:", php)
                            e = 1
                        elif inventory[g] == ("Small Energy ball"):
                            pnrg += 5
                            inventory.pop(g)
                            print("Energy:", pnrg)
                            e = 1
                        elif inventory[g] == ("Large Energy ball"):
                            pnrg += 15
                            inventory.pop(g)
                            print("Energy:", pnrg)
                            e = 1
                        elif inventory[g] == ("e-TANK"):
                            php += 50
                            inventory.pop(g)
                            print("HP:", php)
                            e = 1
        
            if event.type == pygame.KEYUP:
                player.stop()
                invslot = 0
        
        # Random encounters (working)
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
                    exp = 5
                    loot = random.randint(0, 1)
                    if loot == 0:
                        lootie = commonloot[random.randint(0, 8)]
                    else:
                        pass
                elif elist == 1:
                    ehp = sjhp
                    edmg = 2
                    exp = 10
                    loot = random.randint(0, 1)
                    if loot == 0:
                        lootie = commonloot[random.randint(0, 8)]
                    else:
                        pass
                elif elist == 2:
                    ehp = bosshp
                    edmg = 5
                    exp = 15
                    loot = random.randint(0, 1)
                    if loot == 0:
                        lootie = rareloot[random.randint(0, 8)]
                    else:
                        pass
                    
                    # Fights
                while php > 0 and ehp > 0:
                    if elist == 0:
                        metimg = pygame.image.load('met.jpeg')
                        screen.blit(metimg, (0, 0))
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
                pxp += exp
                print("You earned", exp, "XP!")
                if loot == 0:
                    print("WOWZA! He dropped a", lootie)
                    inventory.append(lootie)
                
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
        # If player gets near the bottom, shift the world down (-y)
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