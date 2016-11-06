# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:21:19 2016

@author: PET3RtheGreat
"""

import pygame, sys


def interaction(Hero, FPS, total_frames):
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()