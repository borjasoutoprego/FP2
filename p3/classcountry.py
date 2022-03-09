# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:11:40 2021

@author: Nina López Laudenbach (nina.laudenbach), Borja Souto Prego (borja.souto)
"""

class Country():
    """ Clase país """
    def __init__(self, name):
        """ establece el nombre y la puntuación del país"""
        self.name = name
        self.puntuation = 0
        
    def set_puntuation(self, puntuation):
        """ Permite establecer la puntuación del país"""
        self.puntuation = puntuation
        
    def get_puntuation(self):
        """ Permite obtener la puntuación del país"""
        return(self.puntuation)
    
    def get_name(self):
        """ Permite obtener el nombre del país"""
        return(self.name)
        
    def __str__(self): # para ver los elementos del país
      """Crea un string con elementos"""
      string = ''
      string += self.name
      string += str(self.puntuation)
      return string
  
    def __eq__(self, other):
        """ Devuelve True si other tiene el mismo nombre"""
        return self.name == other.name 