#Diseñar el algoritmo que me permita leer un número decimal que representa una cantidad de
#grados Celsius y convierta dicho valor a la cantidad equivalente en grados Fahrenheit. La salida
#del programa puede ser de la siguiente forma: 100 grados Celsius son 212 grados Fahrenheit.

#VARIABLES

pedir = float(input("Ingrese un valor en decimal para calcular de CELCIUS a FAHRENHEIT: "))

gF = 9.0/5.0 * pedir + 32

print("La transformación de",pedir, "grados Celcius a fahrenheit es: ",gF)

#REALIZADO POR MATIAS NEIRA HENRIQUEZ