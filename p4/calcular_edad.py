# -*- coding: utf-8 -*-

# documentación del módulo datetime en 
# https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes
from datetime import date, datetime

def calcular_edad(fecha_nacimiento):
    """ calcula la edad en años de una persona que ha nacido 
        en la fecha indicada en el parametro de tipo date fecha_nacimiento """
    # obtenemos la fecha actual
    hoy = date.today()
    # restamos los años
    resultado = (hoy.year - fecha_nacimiento.year)
    # ajustamos por mes y día
    # pista: True==1, False==0
    resultado -= ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado
    
cadena = "3/5/1990"
# a strptime le pasamos un sring con una fecha y un string con el formato de esa fecha
fecha = datetime.strptime(cadena, "%d/%m/%Y")

