# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))


#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
wall = pygame.image.load("mur.jpg")
wall2 = pygame.image.load("mur.jpg")
position_perso = perso.get_rect()
position_wall = wall.get_rect()
position_wall2 = wall2.get_rect()
position_wall.x = 200
position_wall.y = 200
position_wall2.x = 100
position_wall2.y = 100
fenetre.blit(perso, position_perso)
fenetre.blit(wall, position_wall)
fenetre.blit(wall2, position_wall2)
#Rafraîchissement de l'écran
pygame.display.flip()

pygame.key.set_repeat(10,10)
#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:    #Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(0,3)
            if event.key == K_UP:    #Si "flèche haut"
                #On monte le perso
                position_perso = position_perso.move(0,-3)
            if event.key == K_RIGHT:    #Si "flèche droite"
                #On descend le perso
                position_perso = position_perso.move(3,0)
            if event.key == K_LEFT:    #Si "flèche gauche"
                #On descend le perso
                position_perso = position_perso.move(-3,0)
    
    
    fenetre.fill((55,86,34))
    #Re-collage
    fenetre.blit(perso, position_perso)
    fenetre.blit(wall, position_wall)
    fenetre.blit(wall2, position_wall2)
    #Rafraichissement
    pygame.display.flip()
    

pygame.quit()

