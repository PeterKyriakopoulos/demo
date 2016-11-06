# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:21:19 2016

@author: PET3RtheGreat
"""

import pygame, sys
#from classes import ray

def interaction(Hero, FPS, total_frames):
    pygame.mouse.set_cursor("images/democursor.png")

    Mpos = pygame.mouse.get_pos    
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#target = Mpos - (Hero.x, Hero.y)
#for event in pygame.event.get():
#   if event.type == pygame.MOUSEBUTTONDOWN:
#       shoot???    