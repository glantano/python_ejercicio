#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
num3 = int(input("ingrese el tercer numero entero: "))
enteros = [num1,num2,num3]
enteros.sort()
print (enteros)