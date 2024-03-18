resultado = 0
opcion = 1

while opcion != 5:
    #muestro el mensaje de calculador 
    print("Calculadora")
    #declaro una variable a y le asigno un numero entero ingresado por el usuario
    a = int(input("Ingrese el primer numero: "))
    #declaro una variable b y le asigno un numero entero ingresado por el usuario
    b = int(input("Ingrese el primer numero: "))

    #muestro pcion de un menu para que el usuario indique que se debe hacer
    print("¿Que opción desea realizar?")
    print("1-Suma")
    print("2- Resta")
    print("3-Multiplicar")
    print("4-Dividir")

    #almaceno en la variable opcion, lo ingresdo por el usuario 
    opcion = int(input("Ingresu su opcion: "))

    if opcion == 1:
        resultado = a+b
    elif opcion ==2:
        resultado = a-b
    elif opcion ==3:
        resultado = a*b
    elif opcion == 4: 
        resultado =a/b

    print("El resultado es", resultado)