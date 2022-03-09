# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:38:36 2021

@author: Borja Souto Prego (borja.souto), Nina López Laudenbach (nina.laudenbach)
"""

def print_list(pl):
    """ Show a positional list in a terminal. """
    print("[", end=" ")
    for x in pl:
        print(x, end=" ")
    print("]")
    
def findItem(positional_list, name):
    """ Return the position of the first instance of e
    in a positional list pl. Return None if e
    is not an element of pl."""
    marker = positional_list.first() # None si lista vacía
    while marker != None and positional_list.get_element(marker).get_name() != name:
        marker = positional_list.after(marker) # None si es la última
    return marker

def findInsertPosition(pl, position_element):
    """ Return the position l where e has to be inserted, if it is between other
    elements, and None if it has to be inserted as the first element"""
    l = pl.before(position_element)
    element = pl.get_element(position_element)
    while l != None:
        element1 = pl.get_element(l)
        if element.get_puntuation() < element1.get_puntuation():
            return l
        else:
            l = pl.before(l)
    return l

def insertInPlace(pl, oldposition, newposition, element):
    """ Takes element from oldposition and inserts it in newposition of the
    positional list pl"""
    if newposition == oldposition:
        pass
    elif newposition == None:
        pl.delete(oldposition)
        pl.add_first(element)
    else:
        pl.delete(oldposition)
        pl.add_after(newposition, element)
              