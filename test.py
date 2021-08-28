""" This is supposed to take a limit(x) and a limit(y) for the levels, and the current pos (x) and current pos (y) not entirely sure how define works..."""

def setlvl(currentlvl, nextlvl):
    global currnet_level_no
    global player
    if current_level_no == currentlvl:
            current_level_no = nextlvl
            current_level = level_list[current_level_no]
            player.level = current_level
    
    
def lvlchange(limitx, limity, currentx, currenty):
    if currentx < limitx and currenty < limity:
        setlvl(0, 1)
        setlvl(1,2)
        setlvl(2,3)
                
lvlchange (current_level.level_limitx, current_level.level_limity, current_postionx, current_positiony)



#old level change meathod. just in case

        """if current_positionx < current_level.level_limitx and current_positiony < current_level.level_limity:
            if current_level_no == 0:
                current_level_no = 3
                current_level = level_list[current_level_no]
                player.level = current_level
            elif current_level_no == 3:
                current_level_no = 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else: 
                current_level_no = 2
                current_level = level_list[current_level_no]
                player.level = current_level"""