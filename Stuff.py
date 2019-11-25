# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
class Stuff (object):
    def __init__(self):
      self.locate=[]
        
    def addstuff(self,x,y,look):
        self.locate.append((x,y,look))
        
        
         
stuff1=Stuff()

stuff1.addstuff(3,3,"fraise")
stuff1.addstuff(5,5,"banane")
i = 0


for element in stuff1.locate:
    element[0]
    print()
    print(element[0])