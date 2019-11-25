# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
""" 
import pygame


class Ghost (object):
    def __init__(self,look):
        self.look=look
        self.x=0
        self.y=0
        
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
    
    
   
    
    
    pygame.init()
    
window = pygame.display.set_mode((640, 480))
      
background = pygame.image.load("background.jpg").convert()
window.blit(background, (0,0))

ghost = pygame.image.load("ghost_red.png").convert_alpha()

window.blit(ghost, (200,300))
pygame.display.flip()

continuer = 1
        
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
        

    
        





ghost1=Ghost("blue")