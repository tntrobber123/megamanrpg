import pygame
import constants
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    # Set speed vector of player
    change_x = 0
    change_y = 0
    steps = 0
    change_steps = 0
    
    direction = "D"

    # List of sprites we can bump against
    level = None
    
    def imgloadr(self, x1, y1, x2, y2):
        image = self.sprite_sheet.get_image(x1, y1, x2, y2)
        self.walking_frames_r.append(image) 
            
    def imgloady(self, x1, y1, x2, y2):
        image = self.sprite_sheetl.get_image(x1, y1, x2, y2)
        self.walking_frames_l.append(image)
        
    def imgloadf(self, x1, y1, x2, y2):
        image = self.sprite_sheetd.get_image(x1, y1, x2, y2)
        self.walking_frames_d.append(image)
    
    def __init__(self):
        """ Constructor function """
        # This holds all the images for the animated walk left/right of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []
        self.walking_frames_reg = []
    
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = SpriteSheet("p1_walk_lr.png")
        self.sprite_sheetud = SpriteSheet("p1_walk.png")
        self.sprite_sheetl = SpriteSheet("p1_walk_l.png")
        self.sprite_sheetd = SpriteSheet("p1_walk_f.png")
        
        # Load the right facing images
        self.imgloadr(138, 177, 199, 136)
        self.imgloadr(69, 177, 58, 136)
        self.imgloadr(0, 177, 69, 136)
        self.imgloadr(138, 121, 199, 58)
        self.imgloadr(69, 121, 60, 58)
        self.imgloadr(0, 121, 69, 58)
        self.imgloadr(138, 60, 60, 60)
        self.imgloadr(69, 60, 75, 60)
        self.imgloadr(0, 60, 69, 60)
        self.imgloadr(138, 0, 69, 60)
        self.imgloadr(69, 0, 69, 60)
        self.imgloadr(0, 0, 69, 60)
        # Left
        self.imgloady(138, 177, 60, 136)
        self.imgloady(69, 177, 58, 136)
        self.imgloady(0, 177, 60, 136)
        self.imgloady(138, 121, 99, 58)
        self.imgloady(69, 121, 60, 58)
        self.imgloady(0, 121, 60, 58)
        self.imgloady(138, 60, 60, 60)
        self.imgloady(69, 60, 60, 60)
        self.imgloady(0, 60, 60, 60)
        self.imgloady(138, 0, 60, 60)
        self.imgloady(69, 0, 60, 60)
        self.imgloady(0, 0, 60, 60)
        
        # Load the backward facing images
        image = self.sprite_sheetud.get_image(0, 0, 68, 70)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(70, 0, 68, 70)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(131, 0, 68, 75)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(0, 70, 68, 75)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(70, 70, 65, 75)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(0, 70, 68, 75)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(131, 70, 68, 75)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(0, 150, 60, 70)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(70, 150, 60, 70)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(131, 150, 60, 70)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(0, 220, 60, 150)
        self.walking_frames_u.append(image) 
        image = self.sprite_sheetud.get_image(68, 220, 60, 150)
        self.walking_frames_u.append(image)
        
        # Load the forward facing images
        self.imgloadf(58, 0, 58, 72)
        self.imgloadf(115, 0,170, 72)
        self.imgloadf(0, 72, 56, 143)
        self.imgloadf(58, 72, 144, 143)
        
        image = self.sprite_sheetud.get_image(0, 0, 58, 72)
        self.walking_frames_reg.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_reg[0]
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
            frame = (self.rect.y // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        elif self.direction == "D":
            frame = (self.rect.y // 30) % len(self.walking_frames_d)
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
        self.steps += self.change_steps
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

        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def go_left(self):
        self.change_x = -4
        self.change_steps = 1
        self.direction = "L"

    def go_right(self):
        self.change_x = 4
        self.change_steps = 1
        self.direction = "R"
        
    def go_up(self):
        self.change_y = -4
        self.change_steps = 1
        self.direction = "U"
    
    def go_down(self):
        self.change_y = 4
        self.change_steps = 1
        self.direction = "D"

    def stop(self):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = 0
        self.change_y = 0
        self.change_steps = 0
        frame = self.walking_frames_reg
        self.image = self.walking_frames_reg[0]