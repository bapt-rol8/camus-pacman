# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
""" 
import pygame
# BOUCLE DE JEU
clock = pygame.time.Clock()
while True:
    
	
	

# ... A COMPLETER AVEC LE CODE DE VOTRE JEU ...
keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
     print("flèche haut")
	# MAJ DE L'AFFICHAGE
	pygame.display.update()


class Ghost (object):
    def __init__(self,look):
        self.look=look
        self.x=0
        self.y=0
        
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
    
    
    
    





ghost1=Ghost("blue")