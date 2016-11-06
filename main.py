# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:42:45 2016

@author: PET3RtheGreat
"""

import pygame, sys
from classes import *
from interaction import interaction


pygame.init()
pygame.font.init()
pygame.mixer.init()

scwidth = 1600
scheight = 900


screen = pygame.display.set_mode((scwidth, scheight))
clock = pygame.time.Clock()
FPS = 60
total_frames = 0

#background = pygame.image.load("images/forest.jpg")
background = pygame.image.load("images/demoback.png")
hero = Hero(scwidth - 1900, scheight - 400, "images/demochar.png")
target = (scwidth - 1500, scheight - 400, "images/demotarget.png")

while True:
    interaction(hero, FPS, total_frames)
#   LOGIC (ex. movement)
    hero.motion(scwidth, scheight)
    total_frames += 1
#   LOGIC
#   DRAW
    screen.blit(background, (0,0))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()
    
    clock.tick(FPS)
