#Realiza un programa para preguntar al usuario cuatro notas:
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprime el resultado redondeado a un decimal.

nota_1 = float(input("Ingresa nota tareas: "))
nota_2 = float(input("Ingresa nota interrogaciones: "))
nota_3 = float(input("Ingresa nota examen: "))
nota_4 = float(input("Ingresa nota presentacion: "))

promedio = round((nota_1*0.3) + (nota_2*0.3) + (nota_3*0.3) + (nota_4*0.1),1)

print ("El promedio final es", promedio)