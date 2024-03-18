#Realizar un programa que a partir de un numero entero calculo el factorial de dicho numero ingresado 

x = int(input("Ingrese el número que desee calcular factorial: ")) #le pedimos al usuario ingresar el numero que desea calcular factorial

i = 1 #identificamos un contador 
factorial = 1 #Especificamos el acumulador que comience a multiplicar desde el 1

if x >=0: #el calculo se realiza siempre cuando el numero ingresado es mayor o igual a 0
    while i <= x: 
        factorial = factorial * i #el acumulador 
        i = i + 1 #el contador 
    print ("el factorial del número es", factorial)

else: #en caso que el numero sea menor a 0 notifica el siguiente mensaje
    print("no se puede calcular factorial")

    