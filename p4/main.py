# -*- coding: utf-8 -*-
"""
Created on Thu May 13 08:52:39 2021

@author: Borja Souto Prego (borja.souto), Nina López Laudenbach (nina.laudenbach)
"""

from crear_ficheros import *
import sys
from avl_tree import *
from classMember import *
from uso_de_arboles_binarios import *
import random
from calcular_edad import *
random.seed(123)

nA = int(sys.argv[1]) # numero de socios
nB = int(sys.argv[2])


def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
       To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1


def createAVL(fichero, tree):
    """ Creates a AVL tree for the teams A and B reading the members from a .txt file"""
    with open(fichero) as f:
        lines = f.readlines()
        for l in lines:
            ls = l.split(' ')
            dni, surname, name, birthdate, location = ls[0], ls[1], ls[2], ls[3], ls[4]
            if key_in_tree(tree, dni) == False:            
                list_members = []
                m = str(Member(dni, surname, name, birthdate, location))
                list_members.append(m)
                tree[dni] = list_members 
            else:
                m = str(Member(dni, surname, name, birthdate, location))
                tree[dni].append(m)
        
    return tree
 
    
def key_in_tree(tree, key):
    """" Returns True if the key is already in the tree. Otherwise it return False."""
    p = tree.find_position(key)
    if p is not None:
        if p.key() == key:
            return True
        else:
            return False
        
    else:
        return False 

                 
def merge_AVL(treeA, treeB):
    """ Merges two trees into one tree without repeated elements"""
    treeC = treeA
    position = treeB.first() 
    while position is not None:
        k = position.key()    #clave de la posicion x en B
        if key_in_tree(treeC, k) == False:   #esa clave no está en C
            treeC[k] = position.value()    #se añade a C
        elif key_in_tree(treeC, k) == True:     #la clave esta en C
            p = treeC.find_position(k)    #posición de la clave en C
            if p.value() != position.value():    #si el valor (persona) de la posición de C es distinto al de la posicion en B
                treeC[k] = position.value()    #se añade a C
        else:  #sería el caso en el que la persona sí que es la misma en los dos árboles
            pass
        
        position = treeB.after(position) 
        
    return treeC 


def price_loc(loc):
    """ Returns the price depending on the location of the seat"""
    if loc == 'tribuna':
        price = prices_dict['tribuna'] 
        return price
        
    elif loc == 'preferencia':
        price = prices_dict['preferencia'] 
        return price
        
    elif loc == 'fondoNorte':
        price = prices_dict['fondoNorte']
        return price
        
    else:
        price = prices_dict['fondoSur'] 
        return price
                

def calculate_price(position):
    """ Calculates the price for each member, looking at the age and location"""
    v = position.value()
    if len(v) == 1:
        v1 = v[0].split(' ')
        date = datetime.strptime(v1[3], "%Y-%m-%d")
        age = calcular_edad(date)
        loc = v1[4]
        if age < 18:
            price = price_loc(loc) * 0.9 # descuento por ser menor
        
        else:
            price = price_loc(loc)
            
        return price
    
    else: 
        price = 0
        for l in v:
            v1 = v[0].split(' ')
            date = datetime.strptime(v1[3], "%Y-%m-%d")
            age = calcular_edad(date)
            loc = v1[4]
            if age < 18:
                p = price_loc(loc) * 0.9 # descuento por ser menor
            
            else:
                p = price_loc(loc)
                
            price += p
            
        return price * 0.9 # descuento por abono familiar

prices_dict = {}
prices_dict['tribuna'] = 110
prices_dict['preferencia'] = 60
prices_dict['fondoNorte'] = 80
prices_dict['fondoSur'] = 80


if __name__ == "__main__":
    
    with open('equipoA.txt', 'w') as f:
        for _ in range(nA):
            memberA = str(createDNI() + ' ' + createsurname() + ' ' + createname() + ' ' + createbirthdate() + ' ' + createlocation() + ' ' + '\n')
            f.writelines(memberA)
        
        # añadimos a mano personas con el mismo DNI para comprobar que el programa funciona con abono familiar
        f.writelines('04164106R Rodríguez Basileo 2006-07-27 tribuna \n')
        f.writelines('47387228O Moya Eduardo 2004-09-16 fondoNorte \n')
        f.writelines('47387228O Garrido Amaro 2009-08-23 preferencia \n')
            
    with open('equipoB.txt', 'w') as f:
        for _ in range(nB):
            memberB = str(createDNI() + ' ' + createsurname() + ' ' + createname() + ' ' + createbirthdate() + ' ' + createlocation() + ' ' + '\n')
            f.writelines(memberB)
            
        f.writelines('05470856L Guerrero Laura 2004-04-01 fondoSur \n')
        f.writelines('05470856L Garrido Amaro 2009-07-14 preferencia \n')
        f.writelines('82776049P Garrido Fausto 2009-07-14 preferencia \n')
    
    treeA = createAVL('equipoA.txt', AVL()) 
    treeB = createAVL('equipoB.txt', AVL()) 
    print("Socios del Equipo A:")
    preorder_indent_BST(treeA, treeA.root(), 0)
    print('\nSocios del Equipo B:')
    preorder_indent_BST(treeB, treeB.root(), 0)
    
    treeC = merge_AVL(treeA, treeB)

    print('\nSocios del aquipo C (A y B fusionados:)')
    
    with open('equipoC.txt', 'w', encoding=('utf-8')) as f:
        p = treeC.first()
        while p is not None:
            memberC = str(p.value()) + '\n'
            f.writelines(memberC)
            p = treeC.after(p)
        
    position = treeC.first()
    
    while position is not None:
        position.value().append(calculate_price(position))
        position = treeC.after(position)
    
    preorder_indent_BST(treeC, treeC.root(), 0)