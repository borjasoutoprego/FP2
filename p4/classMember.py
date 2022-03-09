# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:49:15 2021

@author: @author: Borja Souto Prego (borja.souto), Nina López Laudenbach (nina.laudenbach)
"""

class Member():
    """ Class member"""
    def __init__(self, dni, surname, name, birthdate, location):
        """ Sets the dni, surname, name, birthdate and location of the member"""
        self.dni = dni
        self.surname = surname  
        self.name = name
        self.birthdate = birthdate 
        self.location = location
            
    def __str__(self): 
      """Creates a string with elements"""
      string = ''
      string += self.dni + ' '
      string += self.surname + ' '
      string += self.name + ' '
      string += self.birthdate + ' '
      string += self.location 
      
      return string
        
        