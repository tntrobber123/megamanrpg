"""
Module for managing platforms.
"""
import pygame
import sys

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

GRASS_LEFT            = (0, 0, 75, 75)
GRASS_RIGHT           = (0, 0, 75, 75)
GRASS_MIDDLE          = (0, 0, 75, 75)
STONE_PLATFORM_LEFT   = (432, 720, 65, 65)
STONE_PLATFORM_MIDDLE = (648, 648, 65, 65)
STONE_PLATFORM_RIGHT  = (792, 648, 65, 65)

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


    