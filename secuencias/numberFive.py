#Diseñar un programa que muestre los múltiplos de 2 y de 3 y de ambos comprendidos entre 0 y 100

def multiple(valor, multiplo):

    return True if valor % multiplo == 0 else False
 

multiplos_2=[]
multiplos_3=[]

for t in range(1, 101):
 
    if multiple(t, 2):
        multiplos_2.append(t)
 
    if multiple(t, 3):
        multiplos_3.append(t)
print("Vamos a mostrar los multiplos de 2 y 3 hasta el 100!")
print ("\nLos multiples de 2 son:", multiplos_2)
print ("\nLos multiples de 3 son:", multiplos_3)

