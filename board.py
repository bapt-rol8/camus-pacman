# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

              #fenetre https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/creer-une-simple-fenetre-personnalisable/
import pygame

pygame.init()

H=750
L=750
nbH=15
nbL=15
ecran = pygame.display.set_mode((H ,L))
wall = pygame.image.load("wall brick.png").convert_alpha()

liste_wall = []
with open('lvl1.txt', "r") as file:
    for y,line in enumerate(file):
        for x,carac in enumerate(line):
            if carac=="o":
                print (carac,x,y)
                liste_wall.append((x, y))
                
  






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

