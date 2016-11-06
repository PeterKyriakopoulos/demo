# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:20:57 2016

@author: PET3RtheGreat
"""

import pygame, math
from random import randint

class BaseClass(pygame.sprite.Sprite):
    allsprites = pygame.sprite.Group()    
    def __init__(self, x, y, image_string):
        
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)        
        
        self.image = pygame.image.load(image_string)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        
    def destroy(self, ClassName):
        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self
        
class Hero(BaseClass):
    
    List = pygame.sprite.Group()
    going_right = True    
    
    def __init__(self, x, y, image_string):
        
        BaseClass.__init__(self, x, y, image_string)
        Hero.List.add(self)
        self.velx, self.vely = 0, 10
        self.jumping, self.go_down = False, False
        
    def motion(self, scwidth, scheight):
        
        predicted_location = self.rect.x + self.velx
        
        if predicted_location < 0:
            self.velx = 0
        elif predicted_location + self.rect.width > scwidth:
            self.velx = 0        
        
        
        
class Target(BaseClass):
    
#    List = pygame.sprite.Group()
    
    def __init__(self, x, y, image_string):
        Target.List.add(self)
        self.velx, self.vely = 0,0
        self.jumping, self.go_down = False, False


class Ray(BaseClass):
    
#    List = pygame.sprite.Group()
    
    def __init__(self, x, y, velx, vely, direction, image_string):
        
        self.direction = direction
        self.velx, self.vely = 100, 100
        