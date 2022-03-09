# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:02:29 2021

@author: Borja Souto Prego (borja.souto), Nina López Laudenbach (nina.laudenbach)
"""

import random
import string
import datetime
from datetime import date

def createDNI():
    """ Creates a random DNI"""
    dni = ''
    for i in range(8):
        n = str(random.randint(0, 9))
        dni += n
    dni += string.ascii_uppercase[random.randint(0, 25)]
    
    return dni
 
   
def createsurname():
    """ Chooses a random surname from a file"""
    with open('apellidos-es.txt', encoding=('utf-8')) as f:
        content = f.read()
        lines = content.split('\n')
            
    return random.choice(lines)

    
def createname():
    """ Chooses a random name from a file"""
    with open('nombres-propios-es.txt', encoding=('utf-8')) as f2:
        content2 = f2.read()
        lines2 = content2.split('\n')
            
    return random.choice(lines2)
    

def createbirthdate():
    """ Creates a random birthdate for a person over 18"""
    start_date = datetime.date(1921, 1, 1)
    end_date = datetime.date(2021, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return str(random_date)


def createlocation():
    """ Creates a random stadium location"""
    list_locations = ['tribuna', 'preferencia', 'fondoNorte', 'fondoSur']
    
    return random.choice(list_locations)


