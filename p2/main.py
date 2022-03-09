# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:54:05 2021

@author: Nina López Laudenbach (nina.laudenbach) y Borja Souto Prego (borja.souto)
"""

from array_queue import * 
import sys
import random
import numpy 
from population_sample import *
from Errors import *
from classvaccine import *

config = int(sys.argv[1]) 
e = int(sys.argv[2]) 
N = int(sys.argv[3]) 
x = int(sys.argv[4]) 
y = int(sys.argv[5])
z = int(sys.argv[6]) 
a = int(sys.argv[7]) 
b = int(sys.argv[8]) 
p = int(sys.argv[9]) 
t = sys.argv[10] 

if config == 1:
    configs = [('A', 70, 100, x), ('B', 50, 70, y), ('C', 0, 50, z)]
    
elif config == 2:
    configs = [('A', 80, 100, x), ('B', 60, 80, y), ('C', 40, 60, z), ('D', 20, 40, a), ('E', 0, 20, b)]
    
else:
    raise ArgumentError('El argumento "config" se ha introducido incorrectamente.')

def queue_composition(queue, elements):
    """Añade un "1" a "queue" tantas veces como se indique en "elements"."""
    for element in range(elements):
        queue.enqueue(1)
        
def queue_evaluation1(N, x, y, z, a, b, p, e, config):
    """Realiza todos los cálculos necesarios sobre el proceso de vacunación."""
    listcnt = {}
    list_people = {}
    cnt = {}
    for name, low, high, quantity in configs:
        listcnt[name] = []
        list_people[name] = []
        cnt[name] = 0
        
    uniform = uniform_population()
    galicia = galician_population()
    
    for i in range(e):
        population = ArrayQueue()
        v = {}
        queue = {}
        for name, low, high, quantity in configs: 
            v[name] = Vaccine(name, low, high)
            queue[name] = ArrayQueue()
        
        for day in range(N): 
            for name, low, high, quantity in configs:
                queue_composition(queue[name], quantity)
            
            if t == 'u':
                for _ in range(p):
                    age = uniform.sample()
                    population.enqueue(age)
            elif t == 'g':
                for _ in range(p): 
                    age = galicia.sample()
                    population.enqueue(age)
            else:
                raise ArgumentError('El argumento "t" se ha introducido incorrectamente.')
            
            population_size = len(population)
            
            for _ in range(population_size):
                person = population.dequeue()
                for key in v:
                    if v[key].is_applicable(person):
                        selected = key
                        break
                    
                if queue[selected].is_empty():
                    population.enqueue(person) 
                    
                else:
                    queue[selected].dequeue()
                    list_people[selected].append(person)
                    cnt[selected] += 1
  
        cnt_used = 0
        cnt_not_used = 0
        for name, low, high, quantity in configs:
            listcnt[name].append(cnt[name]) 
            cnt_used += cnt[name]
            cnt_not_used += len(queue[name])
    
    for name, low, high, quantity in configs:
        print("Vacuna", name, ":")
        print("Número de vacunas usadas: ",cnt[name])
        print("Media de edad de las personas vacunadas: ",numpy.mean(list_people[name]))
        print("Desviación típica de la edad de las personas vacunadas: ",numpy.std(list_people[name]))
        print("Media de la cantidad de personas vacunadas: ", numpy.mean(listcnt[name]))
        print("Desviación típica de personas vacunadas: ", numpy.std(listcnt[name]))
        print("*"*50)
  
    print("Personas que quedaron sin vacunar en total: ", len(population))
    print("Vacunas que no se usaron en total: ", cnt_not_used)
    print("Vacunas usadas en total: ", cnt_used)
       
if __name__=="__main__":
    queue_evaluation1(N, x, y, z, a, b, p, e, config)