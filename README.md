# Sofka
Prueba tecnica training calidad

Construcción del algoritmo:

	* Para el primer algoritmo se hizo un desarrollo por medio de condicionales teniendo en cuenta los requerimientos dados en el problema, la entrada la da el usuario compuesta por una distancia a recorrer y los dias de estancia. las salidas del programa son, el valor del pasaje y la cantidad descontada.

	* Para el segundo algoritmo se hizo la definicion de las constantes del programa, luego se desarrollo un ciclo "for" que recorre una lista que corresponde a la tabla de seguimiento, apartir de la tabla base, se constuye una lista nueva donde se ubican los bultos aceptados en el avion, ya con la lista de bultos aceptados, se obtienen las salidas exigidas en el problema, que son numero total de bultos en vuelo, peso del mas pesado y del mas liviano, peso promedio de bultos, para el precio de la carga en el avion se desarrollo una funcion llamada "precio_b" que se encarga de establecer el valor en pesos para cada bulto aceptado en el vuelo, por ultimo se muestra por pantalla los resultados obtenidos.

Tecnologia usada:

	Lenguaje: Python
	Version: 2.7.12
	Versionamiento: Git

Observación:
	
	No se uso ningun IDE, el desarrollo se dio por medio de un texto plano y ejecutado por consola en Linux distro Ubuntu 16.04 a eso se debe las dos primeras lineas de codigo "#!/usr/bin/env python , # -*- coding: utf-8 -*-" que permiten definir la ejecucion en el entorno de python2 y la codificacion del codigo en utf-8, gracias a esto el codigo se puede ejecutar en la consola simplemente usando el comando "$ ./bultos.py". Si las dos primeras lineas de codigo no se colocan, tambien puede ser ejecutado por consola de la siguiente manera "$ python2 bultos.py", en ambos casos es necesario dar los permisos de lectura y ejecucion al script, haciendo uso de la instrucción "chmod". 

