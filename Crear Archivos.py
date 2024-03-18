archivo = open("animales.txt","w") #crea archivo txt, la "w" indica

archivo.write("Perro\n") #escribe perro dentro del archivo txt
archivo.write("Gato\n") #al escribir \n lo escribe como listado hacia abajo

archivo.writelines(["Perro\n","Gato\n","Hola\n"]) #tambien es una forma para escribir un listado hacia abajo

for i in range(1,101): #solicita los numero entre el 1 y 100
    if i < 10: 
        archivo.write(f"0{i} ") #si el numero es menor a 10 imprimir con un 0 en su izquierda
    else:
        archivo.write(f"{i} ")
    if i%10 == 0:   #cada 10 numero saltar aplicar un salto de linea
       archivo.write("\n")

