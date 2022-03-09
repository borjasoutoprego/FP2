## Práctica 3 (Listas posicionales no ordenadas)

Vamos a simular la fase de votación de un concurso tipo Eurovisión. Para ello supondremos
que hay 15 participantes (por simplicidad, sus nombres serán las letras de la A en adelante).
Cada participante otorgará 12, 10, 8, 7, 6, 5, 4, 3, 2, y 1 puntos a otros participantes (no puede
votarse a sí mismo y tiene que conceder todos los puntos y no puede votar más de una vez
a un participante). El proceso será el siguiente:
- Partiremos de una lista posicional de resultados vacía.
- Para cada participante:
	- Determinaremos aleatoriamente a quién va a otorgar cada puntuación.
	- Cuando un participante reciba puntos, si no estaba en la lista posicional se
añadirá, en caso contrario se sumarán los puntos a los que ya tenía. En
cualquier caso, deberá ubicarse en la posición (ordenada) correspondiente a
su número de puntos.
	- Mostraremos la clasificación en este momento ordenada por puntuación (sólo
los participantes que hayan recibido puntos)
- Mostraremos el resultado final de la votación, de más a menos puntos.
Es imprescindible trabajar directamente con la lista posicional de puntuaciones. Por tanto,
realizar el procesamiento sobre una lista de Python y volcarlo en una lista posicional
se considerará como una práctica no presentada.
Se recomienda seguir un desarrollo incremental:
1. Se crea una solución correcta y documentada.
2. Se realiza una simulación N veces, donde N varía de 15, 150, 1500, … y se
proporcionan estadísticas relevantes (p. ej., cuántas veces ha ganado cada
participante)
3. Se amplía la solución considerando en cada ejecución un número arbitrario de
participantes entre 10 y 25. Se proporcionan las estadísticas.
4. Se amplía de cualquier otra manera que se considere relevante. 
