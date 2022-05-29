#Diseñar algoritmo que nos permita introducir un número por teclado y nos informe si es
#positivo o negativo.

import time 

def wait(): 
    time.sleep(0.5) 

def ciclo():
    while True: 
        try: 
            number = int(input("Digite un número negativo o positivo: "))  
            break
        except ValueError:
            print("Debes ingresar un numero!")
    if number >= 0: 
        wait()
        print("El numero",number, "es positivo!")
    elif number <=0:
        wait()
        print("El numero",number, "es negativo!")
ciclo()

#REALIZADO POR MATIAS NEIRA HENRIQUEZ