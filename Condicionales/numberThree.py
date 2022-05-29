#Calcular y mostrar el cuadrado de un número. El número debe ser mayor que cero, en caso de
#error que aparezca el mensaje "ERROR, el número debe ser mayor que cero".

def cuad():
    number = int(input("Ingrese el numero que desee elevar al cuadrado: "))
    result = number ** 2
    if number <= 0:
        print("ERROR, el número debe ser mayor que cero!")
        cuad()
    elif number > 0:
        print("El resultado de",number,"al cuadrado es:",result)
cuad()

#REALIZADO POR MATIAS NEIRA HENRIQUEZ