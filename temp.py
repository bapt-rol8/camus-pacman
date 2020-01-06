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
fraise = pygame.image.load("fraise3.png")
banane = pygame.image.load("banane.png")
lampe = pygame.image.load("lampe.png")
position_perso = perso.get_rect()
position_wall = wall.get_rect()
position_wall2 = wall2.get_rect()
position_fraise = fraise.get_rect()
position_banane = banane.get_rect()
position_lampe = lampe.get_rect()
position_wall.x = 200
position_wall.y = 200
position_wall2.x = 100
position_wall2.y = 100
position_fraise.y = 269
position_fraise.x = 512
position_banane.x = 412
position_banane.y = 412
position_lampe.x = 312
position_lampe.y = 312
fenetre.blit(perso, position_perso)
fenetre.blit(wall, position_wall)
fenetre.blit(wall2, position_wall2)
fenetre.blit(fraise,position_fraise)
fenetre.blit(banane,position_banane)
fenetre.blit(lampe,position_lampe)
#Rafraîchissement de l'écran
pygame.display.flip()

pygame.key.set_repeat(10,10)
#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == pygame.QUIT:
            continuer = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:    #Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(0,3)
            if event.key == pygame.K_UP:    #Si "flèche haut"
                #On monte le perso
                position_perso = position_perso.move(0,-3)
            if event.key == pygame.K_RIGHT:    #Si "flèche droite"
                #On descend le perso
                position_perso = position_perso.move(3,0)
            if event.key == pygame.K_LEFT:    #Si "flèche gauche"
                #On descend le perso
                position_perso = position_perso.move(-3,0)
    
    
    fenetre.fill((150,0,255))
    #Re-collage
    fenetre.blit(perso, position_perso)
    fenetre.blit(wall, position_wall)
    fenetre.blit(wall2, position_wall2)
    fenetre.blit(fraise,position_fraise)
    fenetre.blit(banane,position_banane)
    fenetre.blit(lampe,position_lampe)
    #Rafraichissement
    pygame.display.flip()
    

pygame.quit()

