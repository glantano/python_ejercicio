#Menu
dato_entrada = "2021071929747097487052" #dato de entrada que será separado en las siguientes lineas
año = int(dato_entrada[0:4]) #se separa el año en numero entero desde el dato de entrada
mes = int(dato_entrada[4:6]) #se separa el mes en numero entero desde el dato de entrada
dia = int(dato_entrada[6:8]) #se separa el dia en numero entero desde el dato de entrada
valor_uf = float(int(dato_entrada[8:15])/100) #se separa el valor de uf en float desde el dato de entrada
valor_usd = float(int(dato_entrada[15:20])/100) #se separa el valor de usd en float desde el dato de entrada
tasa_interes = float(int(dato_entrada[20:22])/10) #se separa la tasa de interes en float desde el dato de entrada

while True: #A contiuación se muestra el menú para que el usuario elija la opción que desea
    print("Calculadora Financiera")
    print("")
    print("1.- Indicador de UF y Dolar")
    print("2.- Calculo de UF")
    print("3.- Calculo de Dolar")
    print("4.- Calculo de Valor Futuro")
    print("5.- Salir")
    print("")
    menu_entrada = input(" Ingrese accion a realizar: ") #se le asigna una variable la opción elegida del usuario
    print("")
    if  menu_entrada == "1": #si el usuario elija la opción 1, el programa calcula la UF y el dolar 
        print ("Para el", dia,"/",mes,"/",año) #muestra la fecha segun el dato de entrada 
        print ("El valor de la UF es: {:,.2f}".format(valor_uf).replace(",", "@").replace(".", ",").replace("@", ".")) #muestra valor UF
        print ("El valor del Dolar es: {:,.2f}".format(valor_usd).replace(",", "@").replace(".", ",").replace("@", ".")) #muestra valor Dolar
        print("")
    elif menu_entrada == "2": #si el usuario elija la opción 2, el programa calcula el equivalente en peso un monto ingresado en UF
        importe_uf = int(input("Por favor ingresa un monto en UF : ")) #se solicita ingresar cantidad de UF
        if importe_uf <= 0: #en caso que el usuario ingrese un numero negativo, muestra el mensaje de la siguiente linea
            print ("El numero ingresado no es valido")
        else:
            valor_calculado_uf = round((importe_uf * valor_uf),2) #calcula el valor de la UF en pesos
            print("El valor ingresado en UF es equivalente en pesos a: {:,.2f}".format(valor_calculado_uf).replace(",", "@").replace(".", ",").replace("@", "."))
            print ("")
    elif menu_entrada == "3": #si el usuario elija la opción 3, el programa calcula el equivalente en peso un monto ingresado en dolar
        importe_usd = int(input("Por favor ingresa un monto en Dolar : ")) #se solicita ingresar cantidad de Dolar
        if importe_usd <= 0: #en caso que el usuario ingrese un numero negativo, muestra el mensaje de la siguiente linea
            print ("El numero ingresado no es valido")
        else:
            valor_calculado_usd = round((importe_usd * valor_usd),2) #calcula el valor del Dolar en Pesos
            print("El valor ingresado en USD es equivalente en pesos a: {:,.2f}".format(valor_calculado_usd).replace(",", "@").replace(".", ",").replace("@", "."))
            print ("")
    elif menu_entrada == "4": #si el usuario elija la opción 4, el programa calcula el valor futuro de acuerdo a una serie de información solicitada 
        importe_valor_futuro = int(input("Por favor ingresa el valor presente de un monto en pesos: ")) #se solicita el valor presente
        importe_mes = int(input("Por favor ingresa el periodo de meses: ")) #solicita la cantidad de meses
        if importe_valor_futuro <= 0 or importe_mes < 0: #en caso que el usuario ingrese un numero negativo, muestra el mensaje de la siguiente linea
            print ("Los datos ingresados no son validos")
        else:
            calculo_valor_futuro = round((importe_valor_futuro * ((1 + (tasa_interes/100))**importe_mes)),2) #calcula valor futuro
            calculo_valor_futuro_uf = round((calculo_valor_futuro/valor_uf),2) #el valor futuro lo transforma en UF
            calculo_valor_futuro_usd = round((calculo_valor_futuro/valor_usd),2) #el valor futuro lo transforma en Dolar
            print ("El valor futuro equivalente en pesos es: {:,.2f}".format(calculo_valor_futuro).replace(",", "@").replace(".", ",").replace("@", "."))
            print ("El valor futuro equivalente en UF es: {:,.2f}".format(calculo_valor_futuro_uf).replace(",", "@").replace(".", ",").replace("@", "."))
            print ("El valor futuro equivalente en Dolar es: {:,.2f}".format(calculo_valor_futuro_usd).replace(",", "@").replace(".", ",").replace("@", "."))
            print("") 
    elif menu_entrada == "5": #si el usuario elija la opción 5, el programa se cierra
        break