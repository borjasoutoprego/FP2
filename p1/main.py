# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:01:12 2021

@author: Nina López Laudenbach (nina.laudenbach) y Borja Souto Prego (borja.souto)
"""

from array_stack import *
from infixPosfix import *
from match_delimiters import *
from Errors import *
from operations import *
import math

def posfix_evaluation(posfix_exp):
    """Devuelve el resultado de la expresión posfija."""
    stack = ArrayStack()
    tokenList = posfix_exp.split()
    operators = ['+','-','*','/','**'] 
    for token in tokenList:
        if token=='pi':
            token = math.pi
            stack.push(token)
        elif token == 'e':
            token = math.e
            stack.push(token)
        elif check_floats(token):
            token = float(token) 
            stack.push(token)
        elif (check_integer(token) and not 
            check_floats(token)) or token.isdigit() or token=='-pi' or token=='-e':
            if token=='-e':
                token = math.e * (-1)
                stack.push(token)
            elif token == '-pi':
                token = math.pi * (-1)
                stack.push(token)
            else:    
                token = int(token)
                stack.push(token)
        elif token in operators:
            element1 = stack.pop()
            element2 = stack.pop()           
            result = operations(token, element1, element2)
            stack.push(result)
        else:
            element = stack.pop()
            result = oneelem_operations(token, element)
            stack.push(result)            
        
    return stack.peek()
    
def check_delimiters(infix_exp):
    """Controla que los paréntesis estén balanceados. En caso contrario devuelve un error"""
    if is_matched(infix_exp):
        return
    else:
        raise DelimitersError('Los paréntesis no están balanceados.')
         
if __name__=="__main__":
    infix_exp = input("Introduce una expresión infija: ")
    check_delimiters(infix_exp)    
    posfix_exp = infixToPostfix(infix_exp)
    print("Pasado a expresión posfija: ", posfix_exp)
    result = posfix_evaluation(posfix_exp)
    print("Resultado: ", result)
        
    
    