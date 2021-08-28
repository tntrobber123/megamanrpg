import pygame
import constants
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    # Set speed vector of player
    change_x = 0
    change_y = 0
    
    direction = "D"

    # List of sprites we can bump against
    level = None
    
    def imgloadr(self, x1, y1, x2, y2):
        image = self.sprite_sheet.get_image(x1, y1, x2, y2)
        self.walking_frames_r.append(image) 
            
    def imgloady(self, x1, y1, x2, y2):
        image = self.sprite_sheetl.get_image(x1, y1, x2, y2)
        self.walking_frames_l.append(image)
    
    # -- Methods
    def __init__(self):
        """ Constructor function """
        # This holds all the images for the animated walk left/right of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []
    
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = SpriteSheet("p1_walk_lr.png")
        self.sprite_sheetud = SpriteSheet("p1_walk.png")
        self.sprite_sheetl = SpriteSheet("p1_walk_l.png")
       
        # Load all the right facing images into a list
        
        self.imgloadr(138, 177, 199, 236)
        self.imgloadr(69, 177, 138, 236)
        self.imgloadr(0, 177, 69, 236)
        self.imgloadr(138, 121, 199, 177)
        self.imgloadr(69, 121, 138, 177)
        self.imgloadr(0, 121, 69, 177)
        self.imgloadr(138, 60, 199, 121)
        self.imgloadr(69, 60, 138, 121)
        self.imgloadr(0, 60, 69, 121)
        self.imgloadr(138, 0, 199, 60)
        self.imgloadr(69, 0, 138, 60)
        self.imgloadr(0, 0, 69, 60)
        # Left
        self.imgloady(138, 177, 199, 236)
        self.imgloady(69, 177, 138, 236)
        self.imgloady(0, 177, 69, 236)
        self.imgloady(138, 121, 199, 177)
        self.imgloady(69, 121, 138, 177)
        self.imgloady(0, 121, 69, 177)
        self.imgloady(138, 60, 199, 121)
        self.imgloady(69, 60, 138, 121)
        self.imgloady(0, 60, 69, 121)
        self.imgloady(138, 0, 199, 60)
        self.imgloady(69, 0, 138, 60)
        self.imgloady(0, 0, 69, 60)
        
        # Load the backward facing images
        image = self.sprite_sheetud.get_image(0, 0, 68, 72)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(68, 0, 131, 72)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(131, 0, 199, 72)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(0, 72, 68, 145)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(68, 72, 141, 145)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(0, 62, 135, 145)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(131, 72, 199, 145)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(0, 145, 68, 219)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(68, 145, 131, 219)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(131, 145, 199, 200)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(0, 219, 68, 290)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(68, 220, 131, 290)
        self.walking_frames_u.append(image) 
        
        # Load the forward facing images
        image = self.sprite_sheetud.get_image(0, 0, 68, 72)
        self.walking_frames_d.append(image) 

        # Set the image the player starts with
        self.image = self.walking_frames_d[0]
        self.rect = self.image.get_rect()

    def update(self):
        
        """ Move the player. """

       # Move
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "U":
            frame = (pos // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        elif self.direction == "D":
            frame = (pos // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]
            
        self.rect.y += self.change_y
        pos = self.rect.y + self.level.world_shift

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Left does the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def go_left(self):
        self.change_x = -4
        self.direction = "L"

    def go_right(self):
        self.change_x = 4
        self.direction = "R"
        
    def go_up(self):
        self.change_y = -3
        self.direction = "U"
    
    def go_down(self):
        self.change_y = 3
        self.direction = "D"

    def stop(self):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = 0
        self.change_y = 0
        sprite_sheet = SpriteSheet("p1_walk.png")
        sprite_sheet.get_image(0, 0, 68, 72)