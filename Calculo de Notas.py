#Datos prueba 1, prueba 2 y laboratorio.
nota1 = float(input("Ingrese la primera prueba 1: "))
nota2 = float(input("Ingrese la primera prueba 2: "))
nota_laboratorio = float(input("Ingrese la nota del laboratorio: "))

#calculo de nota que necesita para un 5.0
x = (((5.0 - 0.3*nota_laboratorio)/0.7)*3) - nota1 - nota2
x = round(x,1)

print("Necesita un", x,"en la prueba 3")
