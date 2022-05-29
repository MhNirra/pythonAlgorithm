#Diseñar un algoritmo que calcule la longitud de la circunferencia y el área del círculo de radio dado
from math import pi
from operator import le #importo PI desde la libreria MATH para poder hacer calculos exactos

#VARIABLES
radio = float(input("Escrba el radio del circulo que desee calcular: ")) #solicitamos al usuario el radio que desea calcular
area = pi * radio ** 2 #es la formula para calcular el area.
length = 2 * pi * radio #es la formula para calcular la longitud.

n1 =  round(area, 2) #dejarlo en 2 decimales
n2 = round(length, 2) #dejarlo en 2 decimales
print("El area del circulo es: ",n1)
print("La longitud es: ",n2)

#REALIZADO POR MATIAS NEIRA HENRIQUEZ

