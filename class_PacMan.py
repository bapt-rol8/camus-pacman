# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pygame
class PacMan (object):
    def __init__(self,look):
        self.look=look
        self.x=0
        self.y=0
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
        
        
       
        
        
        
        
pacman1=PacMan("yellow")






import pygame

pygame.init()


fenetre = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

perso = pygame.image.load("PacMan.jpg").convert_alpha()
fenetre.blit(perso, (200,300))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer=0
