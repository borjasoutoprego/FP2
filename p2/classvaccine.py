# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 10:10:25 2021

@author: Nina López Laudenbach (nina.laudenbach) y Borja Souto Prego (borja.souto)
"""

class Vaccine():
    """Clase vacuna."""
    def __init__(self, name, low, high): 
        """Función generadora de la clase vacuna."""
        self.name = name
        self.low = low
        self.high = high
    
    def is_applicable(self, age):
        """Devuelve "True" si la edad se encuentra dentro del rango indicado."""
        return self.low < age < self.high


    
        