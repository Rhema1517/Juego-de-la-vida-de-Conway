Este es un codigo que hace una simulacion del juego de la vida de Conway
Con buenas pruebas que desmuestran que el codigo funciona en todos los casos que deberia funcionar 


### Explicación del Juego de la Vida

El Juego de la Vida es un autómata celular desarrollado por el matemático John Horton Conway en 1969. Lo nombró en honor a su esposa, Heidi, que había muerto a principios de ese año. El juego consiste en una cuadrícula en la que cada puede o no haber cuadrados pintados (las “células”).
Cada celda contiene un solo número que representa su valor de vida o de muerte (si el valor es cero). En cada turno, cada celda se compara con tres células vecinas. Si la suma de esos números excede algún valor umbral, la celda muere; de lo contrario, sigue vivo.

### Reglas

1.Cualquier célula viva con dos o tres vecinos vivos sobrevive.

2.Cualquier célula muerta con tres vecinos vivos se convierte en una célula viva.

3.Todas las demás células vivas mueren en la próxima generación. Del mismo modo, todas las demás células muertas permanecen muertas.

bueno explicando un poco lo que se vera en el codigo tal vez el unico detalle que no me encanta y espero un dia hacer una nueva version y cambiarlo 
es que en el mismo codigo tenemos que poner la condiciones iniciales que queremos,
la condicion inicial de las celular vivas y muertas por medio de una matriz y ademas un numero con el cual sera la generacion que muestre en la interfas grafica 

[![Captura.png](https://i.postimg.cc/1zMhgxdS/Captura.png)](https://postimg.cc/t11mfcyv)


entonces alli en JD poner la matriz y el numero de que es la generacion que mostrara primero 
