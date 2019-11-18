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