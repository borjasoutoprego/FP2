# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:50:28 2021

@author: Nina López Laudenbach (nina.laudenbach) y Borja Souto Prego (borja.souto)
"""

"""Módulo para operaciones"""

import math

def operations(token, element1, element2): 
    """Realiza el cálculo de operaciones que requieren dos operandos."""         
    if token=='+':                         
        result = element2+element1
    elif token=='*':
        result = element2*element1
    elif token=='-':
        result = element2-element1
    elif token == '**':
        result = element2**element1
    elif token == '/':
        result = element2/element1  
        
    return result
    
def oneelem_operations(token, element):    
    """Realiza el cálculo para operaciones que requieren un único operando."""    
    if token == 'sin':                      
        result = math.sin(element)
    elif token == 'cos':
        result = math.cos(element)
    elif token == 'tan':
        result = math.tan(element)       
    elif token == 'arcsin': 
        result = math.asin(element)
    elif token == 'arccos': 
        result = math.acos(element)
    elif token == 'arctan':
        result = math.atan(element)           
    elif token == 'csc': 
        result = 1/math.sin(element)
    elif token == 'sec': 
        result = 1/math.cos(element)
    elif token == 'ctan':
        result = 1/math.tan(element)
    elif token == 'sqrt':
        result = math.sqrt(element)
        
    return result
     