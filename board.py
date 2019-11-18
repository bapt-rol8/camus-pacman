# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

              #fenetre https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/creer-une-simple-fenetre-personnalisable/
import pygame

pygame.init()

ecran = pygame.display.set_mode((300,200))

continuer = True

while continuer :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()







































class Board (object):
    def __init__(self,size):
        self.size=size

