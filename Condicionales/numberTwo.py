#Diseñar el algoritmo necesario para que habiéndose leído el valor de 2 variables NUM1 y
#NUM2 se intercambien los valores de las variables, es decir que el valor que tenía NUM1 ahora
#lo contenga NUM2 y viceversa.

def trade():
    while True:
        try:
            num1 = int(input("Ingrese el primer valor: "))
            break
        except ValueError:
            print("Ingresa un número!")
    while True:
        try:
            num2 = int(input("Ingrese el segundo valor: "))
            break
        except ValueError:
            print("Ingresa un número!")

    print("Sus valores ingresados son:",num1,"y",num2)
    print("Ahora invertiremos sus variables!")

    name1 = input("Asignele un nombre a su primer valor: ")
    name2 = input("Asignele un nombre a su segundo valor: ")

    add = name1 + ":"
    ad_ = name2 + ":"

    print("ANTES DEL CAMBIO")
    print(add,num1,ad_,num2)

    print("DESPUES DEL CAMBIO")
    
    num1, num2 = num2, num1 #cambio
    print(add,num1,ad_,num2)
trade()

#REALIZADO POR MATIAS NEIRA HENRIQUEZ