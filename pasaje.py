#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Constantes
precio_km = 35.00
porcentaje_descuento = 30.00/100.00

#Entradas 
distancia = input('Ingrese la distancia a recorrer (km): ')
dias_estancia = input('Ingrese el numero de dias de estancia: ')

#Salida
valor_pasaje = distancia*precio_km


if distancia > 1000 and dias_estancia > 7:

	descuento = valor_pasaje*porcentaje_descuento
	pago = valor_pasaje - descuento

else:

	pago = valor_pasaje
	descuento = 0

print 'El valor del pasaje es: $',pago 
print 'Con un descuento de: $',descuento
