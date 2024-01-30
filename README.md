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

el codigo  se va hasta las lineas 254 pero muchos son comentario explicando algunos conseptos
tambien tiene muchas lineas vacias que estas po comida como tal el codigo termina en la linea 236 pero seguramente son mucho menos 
por lo espacion que estas puestos por comodidad 

el codigo realmente esta dividido en dos partes la primera parte es donde esta toda la parte que calcula la generacion buscada con la condiciones iniciales 
para dar el resultado correcto, todo echo con python

y la segunda es la parte grafica echo por medio de el modulo de tkinter y mas concretamente con su funcionalidad de canvas

[![Captura2.png](https://i.postimg.cc/mDJHGnB3/Captura2.png)](https://postimg.cc/WFm3GXDt)

la divicion la tengo alli en la linea 129 por comodidad visial para mi en el momento que estaba creando el programa 

[![Captura3.png](https://i.postimg.cc/nL78kjMH/Captura3.png)](https://postimg.cc/Ff9nFKjq)

este serie como se veria el progrma en ejecucion tiene varios detalles visuales:

tiene el nombre del programa 

el indicacion del numero de generacion actual 

y el  grafico que muestra las casillas muertas de color azul

y la casillas vivas en color rojo  

y los numeros contando las casillas como en un plano

[![Captura4.png](https://i.postimg.cc/xTbPqKZT/Captura4.png)](https://postimg.cc/hfcm57gH)

y pues tiene un pequeño campo de texto que nos permite ir a otra generacion, no importa si es posterior o superior en este caso vamos a la cero 
que la generacion cero, es la misma que la matriz de la condicion inicial que le dimos para iniciar el programa 

[![Captura5.png](https://i.postimg.cc/2SRg5j2M/Captura5.png)](https://postimg.cc/tYkBSb0N)

y cerraria y volveria abrir pero ahora con la generacion cero de las condiciones iniciales 
tambien podemos hacerlo con una genracion superior 

![image](https://github.com/Rhema1517/Juego-de-la-vida-de-Conway/assets/111716153/f8627248-1856-4295-9d36-96bad9aa9e56)

entonces ponemos el numero de la generacion que queremos ir y le damos a crear 

![image](https://github.com/Rhema1517/Juego-de-la-vida-de-Conway/assets/111716153/7a5291f0-e67b-417e-9c31-260dd205a1ab)

se genero la generacion 9 segun las condiciones iniciales del programa 

tambien podemos poner el ejemplo de cambiar las condiciones iniciales y el programa funcionara perfectamente eso es lo que pueba precisamente los test 
de echo yo recomiento que si descargas el programa puebes por ti mismo los test ya que algunos dan patrones muy interesantes 

![image](https://github.com/Rhema1517/Juego-de-la-vida-de-Conway/assets/111716153/f72d8a3d-28b0-4608-bebb-94f16dee6ae8)

entonces cambimoas la condiciones iniciales y ejecutamos el programa 

![image](https://github.com/Rhema1517/Juego-de-la-vida-de-Conway/assets/111716153/f106d0f2-99eb-4621-92fb-43fafb122cbb)


![image](https://github.com/Rhema1517/Juego-de-la-vida-de-Conway/assets/111716153/56c81f98-39ae-4269-ae34-675a1747bf0e)


inclusive podemos ver como el programa funciona en condiciones mucho ma grandes 
y da los resultados que corresponden segun el juego 
espero les guste mi programa de practica 
