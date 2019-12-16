# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

              #fenetre https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/creer-une-simple-fenetre-personnalisable/
import pygame

pygame.init()

ecran = pygame.display.set_mode((750,750))

wall = pygame.image.load("wall brick.png").convert_alpha()
ecran.blit(wall, (50,50))
ecran.blit(wall, (50,0))

pygame.display.flip()

continuer = 1

while continuer :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

pygame.quit()







































class Board (object):
    def __init__(self,size):
        self.size=size

