## Práctica 1 (Pilas) 

Implemente un programa modular que mediante la utilización del TAD Pila evalúe una
expresión aritmética en notación infija con las operaciones matemáticas elementales.
Para ello primero se convertirá la expresión infija en su equivalente en notación
posfija, para luego proceder a evaluar esta última. Por ejemplo, la expresión infija
`((5+2)∗(8−3))/5` se convertirá en la expresión posfija `5 2 + 8 3 - ∗ 5 /` cuya
evaluación resulta en 7.

Como implementación del TAD Pila se utilizará la que está en el Moodle de la
asignatura. Para la fase de conversión de infija a posfija se podrá tomar como base
el código disponible en Moodle.
Se recomienda seguir un desarrollo incremental con las siguientes fases:

1. Se crea una solución correcta y documentada para enteros de una cifra y que
supone que la expresión infija inicial es sintácticamente correcta
2. Se amplía con el manejo de errores en la conversión de infija a posfija
3. Se amplía con el trabajo con enteros arbitrarios y números en punto flotante
4. Se amplía con operadores adicionales y llamadas a funciones (p.ej., sin, cos,
etc.)
5. Se amplía con otras funcionalidades adicionales que se consideren relevantes.
