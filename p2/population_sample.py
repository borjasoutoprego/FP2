# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:01:04 2021

@author: Nina López Laudenbach (nina.laudenbach) y Borja Souto Prego (borja.souto)
"""
import numpy as np
import random


class uniform_population():
    """Clase para una población con edades equiprobables."""
    def sample(self):
        """Devuelve un número aleatorio entre 1 y 100."""
        return np.random.randint(low = 0, high = 100)
    
class galician_population():
    """Clase para la población de Galicia con sus probabilidades para los diferentes rangos de edades."""
    def sample(self):
        """Devuelve un número entre 0 y 100 según los rangos de probabilidad."""
        value = np.random.random()
        
        if 0 < value < 0.036:
            return np.random.randint(low = 0, high = 5)
        elif value < 0.079:
            return np.random.randint(low = 5, high = 10)
        elif value < 0.125:
            return np.random.randint(low = 10, high = 15)
        elif value < 0.169:
            return np.random.randint(low = 15, high = 20)
        elif value < 0.212:
            return np.random.randint(low = 20, high = 25)
        elif value < 0.260:
            return np.random.randint(low = 25, high = 30)
        elif value < 0.314:
            return np.random.randint(low = 30, high = 35)
        elif value < 0.380:
            return np.random.randint(low = 35, high = 40)
        elif value < 0.466:
            return np.random.randint(low = 40, high = 45)
        elif value < 0.549:
            return np.random.randint(low = 45, high = 50)
        elif value < 0.628:
            return np.random.randint(low = 50, high = 55)
        elif value < 0.702:
            return np.random.randint(low = 55, high = 60)
        elif value < 0.770:
            return np.random.randint(low = 60, high = 65)
        elif value < 0.830:
            return np.random.randint(low = 65, high = 70)
        elif value < 0.886:
            return np.random.randint(low = 70, high = 75)
        elif value < 0.930:
            return np.random.randint(low = 75, high = 80)
        elif value < 0.962:
            return np.random.randint(low = 80, high = 85)
        elif value < 0.985:
            return np.random.randint(low = 85, high = 90)
        elif value < 0.994:
            return np.random.randint(low = 90, high = 95)
        else:
            return np.random.randint(low = 95, high = 101)
