## Práctica 2 (Colas)

Vamos a simular la administración de vacunas a la población durante N días. Supongamos
que tenemos tres vacunas A, B, y C. Utilizaremos una cola para cada vacuna y otra cola
Población para las personas a vacunar. Cada día ocurrirá lo siguiente:

1. Recibimos un número x de dosis de A, un número y de dosis de B y un número z de
dosis de , C que se añaden a sus colas respectivas.
2. Llamamos a un número p de personas a vacunar que se añaden a la cola de
población, cada una con una edad entre 0 y 100 años. Para cada persona:
a. Se extrae de la cola
b. si es mayor de 70 años le administramos la vacuna A
c. si tiene entre 50 y 70 años le administramos la vacuna B
d. si tiene menos de 50 años le administramos la vacuna C (en todos los casos
la vacuna administrada se elimina de su cola correspondiente)
e. Si una persona no se pudo vacunar por no haber vacuna disponible para su
grupo de edad, se añade a la cola (por el final).

La simulación se ejecutará 20 veces para unos valores dados de N, x, y, z y p. Finalmente
indicaremos la media y la desviación típica de las personas vacunadas por tipo de vacuna,
las que han quedado sin vacunar y las vacunas utilizadas y las que han quedado sin utilizar.

Se recomienda seguir un desarrollo incremental:
1. Se crea una solución correcta y documentada de la simulación para N=90; x=100, y=
200, z = 400; p=700 con una distribución uniforme entre todas las edades.
2. Se amplían los experimentos con diferentes valores para los parámetros. Se puede
suponer que la población se distribuye por edad según la actual en Galicia 
[](https://www.ige.eu/web/mostrar_actividade_estatistica.jsp?idioma=gl&codigo=02010
01006).
3. Se amplía considerando más marcas de vacunas con su correspondiente rango de
edad recomendado. Un experimento interesante sería replicar los experimentos del
paso 2 para ver si, teniendo el mismo número total de dosis pero aumentando las
categorías de edad, es posible vacunar a más gente. Esto permitiría aproximar los
parámetros óptimos de acuerdo con la distribución por edad de la población con vistas
a elaborar una estrategia de compra de vacunas a las empresas farmacéuticas.
4. Se amplía de cualquier otra manera que se considere relevante.
