#Diseñar algoritmo que imprima los números del 100 al 0 en orden decreciente

print("Vamos a imprimir los números del 0 al 100 en orden decreciente")
data = [t for t in range(1, 101)]
data.sort(reverse = True)

print(data)
