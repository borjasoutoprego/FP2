## Práctica 4 (Árboles)

Los equipos deportivos A y B han decidido fusionarse para dar lugar al equipo C, de tal forma
que los socios de A y B pasarán a ser socios de C. Para gestionar esta fusión, partiremos de
dos árboles AVL, uno con los datos de los socios de A y otro con los de B, ambos con el DNI
como clave. A partir de ellos crearemos un nuevo AVL con los socios de C (hay que tener en
cuenta que habrá personas que sean socios de ambos equipos). Se seguirá un desarrollo
incremental:

1. Implementar una primera versión en la que los datos de A y B estén almacenados en
archivos de texto equipoA.txt y equipoB.txt. El formato de cada línea será:
dni, apellidos, nombre, fecha_de_nacimiento, ubicación donde
“ubicación” puede tomar los valores tribuna, preferencia, fondoNorte o
fondoSur. Al finalizar el programa se escribirá el archivo de texto equipoC.txt
correspondiente a C
2. Realizar una ampliación que contemple la existencia del abono familiar, de tal manera
que con un mismo DNI pueda incluirse un adulto y varios menores de edad. Para ello,
cada nodo del AVL contendrá una clave y una lista con los socios de un abono familiar.
3. Realizar una ampliación para calcular la cuota anual de un abono en función del tipo
de cada localidad y edad de todos los que pertenecen al abono (para ello habrá que
disponer de una tabla de precios en función de la edad y ubicación en el estadio).
4. Realizar cualquier otra ampliación que se considere relevante.
