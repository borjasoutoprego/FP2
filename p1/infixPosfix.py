# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:31:56 2020

@author: Nina López Laudenbach (nina.laudenbach) y Borja Souto Prego (borja.souto)
"""

"""Módulo para la correcta conversión de expresión infija a posfija."""

from array_stack import ArrayStack as Stack
from Errors import ExpressionError

def check_integer(num):
    """Devuelve True si el string empieza por "-" y su longitud es mayor que 1."""
    if num.startswith('-') and len(num) > 1:
        return True
    
def check_floats(num):
    """Devuelve True si el string contiene un "."."""
    if '.' in num:
        return True

def check_expr(tokenList):
    """Comprueba si la expresión infija se ha introducido correctamente. En caso contrario devuelve un error."""
    operatorslist = ['+', '-', '*', '/','**']
    operators = 0
    operands = 0
    for token in tokenList:
        if token in operatorslist:
            operators += 1
        elif check_integer(token) or check_floats(token) or token.isdigit() or token=='pi' or token=='e':
            operands += 1        
        else: 
            pass

    if (operators + 1) != operands:
        raise ExpressionError('La expresión infija se ha escrito incorrectamente.')
    else:
        return True
    
def infixToPostfix(infixexpr):
    """Realiza la conversión de expresión infija a posfija."""
    oneelemlist = ['sin','cos','tan','arccos','arcsin','arctan','csc','sec','ctan','sqrt']
    prec = {}
    prec['**'] = 5
    for element in oneelemlist:
        prec[element] = 4
    prec["*"] , prec["/"] = 3, 3
    prec["+"] , prec["-"] = 2, 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split(" ")
    
    if check_expr(tokenList):
        for token in tokenList:
            if token.isnumeric() or check_integer(token) or check_floats(token) or token=='pi' or token=='e':
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.is_empty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)
        
        while not opStack.is_empty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)


if __name__ == '__main__':
    print("A*B+C*D -> {}".format(infixToPostfix("A * B + C * D")))
    print("(A+B)*C-(D-E)*(F+G) -> {}".format(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")))
    print("10 + 3 * 5 / ( 16 - 4 ) -> {}".format(infixToPostfix("10 + 3 * 5 / ( 16 - 4 )")))