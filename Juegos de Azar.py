#importar libreria random para las funciones de nuestro programa
import random

retorno = "S"
while retorno == "S":
    #se crea una lista vacia para almacenar los numeros que ingrese el usuario
    numeros_usuario = []
    #se define 6 numeros entre el 1 y 40 que determine el usuario
    for i in range (0,6): 
        numero = int(input("Ingrese un numero entre el 1 y el 40: "))
        #en el caso que un numero ingresado sea repetido, menor a 1 o mayor a 40, el programa informa que debe ingresar otro numero
        while (numero in numeros_usuario or numero<1 or numero>40):
            print("Numero invalido, favor ingresar otro numero")
            numero = int(input("Ingrese un numero entre el 1 y el 40:  "))
        #se agrega los numeros ingresado por el usuario a la lista seleccionada
        numeros_usuario.append(numero)
    #ordena la lista con los numeros de menor a mayor
    numeros_usuario.sort()

    #se define función para determinar los numeros del sorteo
    def juego_de_azar (juego):
        numero_loteria = []
        #se define 6 numeros entre el 1 y 40 que determine el juego
        for i in range (juego): 
            numero = random.randint(1,40)
            #con el while impide que se repitan numeros
            while numero in numero_loteria:
                numero = random.randint(1,40)
            #se agrega los numeros ingresado por el usuario a la lista seleccionada
            numero_loteria.append(numero)
        #ordena la lista con los numeros de menor a mayor
        numero_loteria.sort()
        return numero_loteria

    sorteo = juego_de_azar(6)

    #entrega mensaje de los numeros de la loteria y los numeros seleccionados por el usuario
    print("Los numeros de loteria para hoy es:", sorteo)
    print("Tu seleccion de numeros es:", numeros_usuario)

    #se agrega un contador para obtener el numero de aciertos del usuario
    contador = 0
    for numero in numeros_usuario:
        if numero in sorteo:
            contador +=1
    #Entrega el mensaje de acuerdo al numero de aciertos del usuario
    print("Haz acertado a",contador, "numero(s) correctos")
    if contador < 3: 
        print("Usted ha ganado $0 en este sorteo")
    elif contador == 4: 
        print("Usted ha ganado $9.080 en este sorteo")
    elif contador == 5: 
        print("Usted ha ganado $294.440 en este sorteo")
    else:
        print("Usted ha ganado $272.279.360 en este sorteo")

    #A continuacion se le pregunta al usuario si desea volver a intentarlo para repetir el proceso.
    volver_intentarlo = input("¿Quieres volver a intentarlo? (S/N): ")
    retorno= volver_intentarlo.upper() 
