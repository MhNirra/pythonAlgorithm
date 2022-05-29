#Diseñar algoritmo que nos permita introducir un número por teclado y nos informe si es par o impar

def pares():
    while True:
        try:
            number = int(input("Ingrese un número para saber si es par o impar: "))
            break
        except ValueError:
            print("Debe ingresar un número!")

    if number % 2 == 0:
        print("El número",number,"es par!")
    else:
        print("El número",number,"es impar!")
pares()

#REALIZADO POR MATIAS NEIRA HENRIQUEZ