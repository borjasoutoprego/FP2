# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:23:05 2021

@author: Nina López Laudenbach (nina.laudenbach), Borja Souto Prego (borja.souto)
"""
import sys
from Errors import *
import random
import string
from classcountry import *
from utils import * 
from statistics import *

list_to_use = str(sys.argv[1])
N = int(sys.argv[2]) # n ejecuciones

if N < 1:
    raise ArgumentError('El argumento para el número de ejecucuines debe ser al menos 1.')
else:

    if list_to_use == 'array':
        from array_positional_list import ArrayPositionalList as PositionalList
        
    elif list_to_use == 'linked':
        from linked_positional_list import LinkedPositionalList as PositionalList
          
    else:
        raise ArgumentError('El argumento para la implementación de la lista se ha introducido incorrectamente')
        
    winners_list = []   
    loser_list= []
    w_puntuation_list = []
    l_puntuation_list = []
        
    for n in range(N):
        print('\n***** Ejecución número', n, '*****\n')
        results_list = PositionalList() # lista posicional de resultados
        competitor_list = [] # paises que votan
        competitors_number = random.randint(12, 25) # numero arbitrario de participantes entre 12 y 25
    
        for c in range(competitors_number):
            b = Country(string.ascii_uppercase[c])
            competitor_list.append(b)
            
        votes_list = [12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
          
        for _ in range(competitors_number):
            country_who_votes = random.choice(competitor_list) # selecciona el pais que vota al azar
            voted_country_list = []
            for cc in range(competitors_number): #países que pueden ser votados
                b = Country(string.ascii_uppercase[cc])
                voted_country_list.append(b)   
                
            voted_country_list.remove(country_who_votes)
            competitor_list.remove(country_who_votes) #elimina el pais ue está votando para que no vuelva a votar        
            
            for vote in votes_list:
                voted_country_name = random.choice(voted_country_list) #para escoger el pais que quiero votar
                voted_country_list.remove(voted_country_name)
                name = voted_country_name.get_name() #me quedo con el nombre del pais
                p = findItem(results_list, name) #me quedo con la posición en results_list de ese pais: none o una posición real
                if p == None:
                    new_puntuation = voted_country_name.get_puntuation() + vote
                    voted_country_name.set_puntuation(new_puntuation)
                    results_list.add_last(voted_country_name) #si no estaba en la lista lo añado al final
                    p1 = findInsertPosition(results_list, results_list.last())
                    insertInPlace(results_list, results_list.last(), p1, voted_country_name)
    
                else: 
                    voted_country = results_list.get_element(p) # si había un elemento con el mismo nombre en la lista, me quedo con el. 
                    new_puntuation2 = voted_country.get_puntuation() + vote
                    voted_country.set_puntuation(new_puntuation2)
                    p2 = findInsertPosition(results_list, p) # encuentro la posición donde insertarlo
                    insertInPlace(results_list, p, p2, voted_country)
            print('\nActualización de los votos:\n')        
            print_list(results_list) # imprime la lista actualizada cada vez que vota un participante
        print('\n***** Resultado final de la votación: *****\n')
        print_list(results_list)
    
        winner = results_list.get_element(results_list.first()).get_name()
        winner_puntuation = results_list.get_element(results_list.first()).get_puntuation()
        loser = results_list.get_element(results_list.last()).get_name()
        loser_puntuation = results_list.get_element(results_list.last()).get_puntuation()
        winners_list.append(winner)
        w_puntuation_list.append(winner_puntuation)
        loser_list.append(loser)
        l_puntuation_list.append(loser_puntuation)
    
    print('\n***** Estadísticas sobre los resultados: *****\n')
    
    aux_list = []
    for j in range(26):
        d = string.ascii_uppercase[j]
        aux_list.append(d)
        
    for i in aux_list:
        cnt_vict = winners_list.count(i)
        cnt_los = loser_list.count(i)
        percentage_win = round((cnt_vict / N) * 100, 2)
        percentage_los = round((cnt_los / N) * 100, 2)
        print('El país', i, 'ha ganado', cnt_vict, 'veces.') # número de veces que gana cada país
        print('El porcentaje de victorias del país', i, 'es', percentage_win, '%')
        print('El país', i, 'ha quedado de último', cnt_los, 'veces.') # número de veces que pierde cada país
        print('El porcentaje de veces que el país', i, 'ha quedado de último es', percentage_los, '%\n')
    
    if N > 1:
        print("La media de puntos de los ganadores es:", round(mean(w_puntuation_list), 2))
        print("La media de puntos de los que quedan de últimos es:", round(mean(l_puntuation_list), 2)) 
        print("La deviación típica de puntos de los ganadores es:", round(stdev(w_puntuation_list), 2))   
        print("La deviación típica de puntos de los países que quedan de últimos es:", round(stdev(l_puntuation_list), 2))   


