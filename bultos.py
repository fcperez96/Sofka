#!/usr/bin/env python
# -*- coding: utf-8 -*-


def precio_b(peso):
	
	if p < 26:
		precio_bulto = peso*0 

	elif p > 25 and p < 301:
		precio_bulto = peso*1500	
	
	elif p > 300 and p < 501:
		precio_bulto = peso*2500

	return precio_bulto



capacidad = 18000
precio = 0
cont = 0
peso_total = 0
pesos_bultos = [500,500,500,500,500,500,500,600,500,500,500,500,500,500,600,500,5,500,500,500,500,600,500,500,500,500,500,600,500,500,500,500,500,500,500,600,600,600,600,600,500]
pesos_bultos_carga = []

print 'Lista de pesos de los bultos: ',pesos_bultos
print 'Cantidad de bultos a cargar: ',len(pesos_bultos),'\n' 

for p in pesos_bultos:

	if (capacidad - peso_total) >= p:
	
		if p <= 500:
			pesos_bultos_carga.append(p)
			cantidad = len(pesos_bultos_carga)

			pesado = max(pesos_bultos_carga)	
			liviano = min(pesos_bultos_carga)			

			peso_total += p
			prom = peso_total/cantidad

			precio_aux = precio_b(p)
			precio = precio + precio_aux
			precio_doll = precio/3669

	
		
		else:
			cont += 1
			print 'Bulto rechazado por exceder el limite de 500kg. No:',cont

	if capacidad == peso_total:

		print '\nAvion en su capacidad maxima.'
		break


print '\nEl numero total de bultos ingresados para el vuelo es: ', cantidad
print 'Peso del bulto mas pesado: ', pesado,'Kg'
print 'Peso del bulto mas liviano: ', liviano,'Kg'
print 'Peso promedio de los bultos: ', prom,'Kg'
print 'Ingreso en pesos por concepto de carga: COP', precio 
print 'Ingreso en dolares por concepto de carga: USD', precio_doll	


