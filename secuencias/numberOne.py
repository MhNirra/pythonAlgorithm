#Diseñar un programa que muestre los números impares entre 0 y 100 y que imprima cuantos impares hay

print("Todos los numeros impares entre el 0 y el 100 son los siguientes: ")
print([t for t in range(1, 101) if t % 2])
