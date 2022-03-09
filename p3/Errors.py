# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:14:42 2021

@author: Nina López Laudenbach (nina.laudenbach) y Borja Souto Prego (borja.souto)
"""

"""Módulo con las diferentes clases de errores"""

class Error(Exception):
    """Base class for other exceptions"""

    
class ArgumentError(Error):
    """Raised when the argument is not correct"""
    