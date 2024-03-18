#Realizar una aplicación que permite determinar el sueldo de una persona con los respectivos descuentos legales

#Datos iniciales para los calculos 
sueldoBruto = int(input("Ingrese el sueldo bruto del trabajador: "))
afp = input("Ingrese la AFP que corresponde: ")

#información de UF y comision de AFP
uf = 29764.36
capital = 0.0114
cuprum = 0.0144
habitat = 0.0127
modelo = 0.0077
planvital = 0.0116
provida = 0.0145
uno = 0.0069

#Realizar el calculo del pago de la AFP y su comisión
if sueldoBruto >0: #Realizar solo en caso que el saldo ingresado sea mayor a $0
    limiteAFP = int(81.7*uf)
    if afp == "capital": 
        calculoAFP = int(sueldoBruto*0.1) #realizar calculo de la AFP
        if sueldoBruto <= limiteAFP: #realizar siguiente orden solo si el sueldo bruto es menor al limite
            print ("El Pago a AFP:", calculoAFP)
            comisionAFP = sueldoBruto*capital
            print ("Comisión AFP:", comisionAFP)
        else: #realizar siguiente orden solo si el limite es mayor al sueldo bruto
            limiteAFP = int(limiteAFP*0.1)
            print ("El Pago a AFP:", limiteAFP)
            comisionAFP = int(limiteAFP*capital)
            print ("Comisión AFP:", comisionAFP)

    elif afp == "cuprum":
        calculoAFP = int(sueldoBruto*0.1)
        if sueldoBruto <= limiteAFP:
            print ("El Pago a AFP:", calculoAFP)
            comisionAFP = int(sueldoBruto*cuprum)
            print ("Comisión AFP:", comisionAFP)
        else:
            limiteAFP = int(limiteAFP*0.1)
            print ("El Pago a AFP:", limiteAFP)
            comisionAFP = int(sueldoBruto*cuprum)
            print ("Comisión AFP:", comisionAFP)

    elif afp == "habitat":
        calculoAFP = int(sueldoBruto*0.1)
        if sueldoBruto <= limiteAFP:
            print ("El Pago a AFP:", calculoAFP)
            comisionAFP = int(sueldoBruto*habitat)
            print ("Comisión AFP:", comisionAFP)
        else:
            limiteAFP = int(limiteAFP*0.1)
            print ("El Pago a AFP:", limiteAFP)
            comisionAFP = int(sueldoBruto*habitat)
            print ("Comisión AFP:", comisionAFP)

    elif afp == "modelo":
        calculoAFP = int(sueldoBruto*0.1)
        if sueldoBruto <= limiteAFP:
            print ("El Pago a AFP:", calculoAFP)
            comisionAFP = int(sueldoBruto*modelo)
            print("Comision AFP:", comisionAFP)
        else: 
            limiteAFP = int(limiteAFP*0.1)
            print ("El Pago a AFP:", limiteAFP)
            comisionAFP = int(sueldoBruto*modelo)
            print ("Comisión AFP:", comisionAFP)

    elif afp == "planvital":
        calculoAFP = int(sueldoBruto*0.1)
        if sueldoBruto <= limiteAFP:
            print ("El Pago a AFP:", calculoAFP)
            comisionAFP = sueldoBruto*planvital
            print ("Comisión AFP:", comisionAFP)
        else:
            limiteAFP = int(limiteAFP*0.1)
            print ("El Pago a AFP:", limiteAFP)
            comisionAFP = int(sueldoBruto*planvital)
            print ("Comisión AFP:", comisionAFP)

    elif afp == "provida": 
        calculoAFP = int(sueldoBruto*0.1)
        if sueldoBruto <= limiteAFP:
            print ("El Pago a AFP:", calculoAFP)
            comisionAFP = int(sueldoBruto*provida)
            print ("Comisión AFP:", comisionAFP)
        else:
            limiteAFP = int(limiteAFP*0.1)
            print ("El Pago a AFP:", limiteAFP)
            comisionAFP = int(sueldoBruto*provida)
            print ("Comisión AFP:", comisionAFP)

    elif afp == "uno": 
        calculoAFP = int(sueldoBruto*0.1)
        if sueldoBruto <= limiteAFP:
            print ("El Pago a AFP:", calculoAFP)
            comisionAFP = int(sueldoBruto*uno)
            print ("Comisión AFP:", comisionAFP)
        else:
            limiteAFP = int(limiteAFP*0.1)
            print ("El Pago a AFP:", limiteAFP)
            comisionAFP = int(sueldoBruto*uno)
            print ("Comisión AFP:", comisionAFP)
    else: 
        print ("La AFP ingresada no existe, favor ingresar de nuevo")

    #Realizar el calculo de ISAPRE
    limiteIsapre = int(80.2*uf)
    if sueldoBruto <= limiteIsapre: #Realizar calculo cuando el sueldo bruto es menor al limite de Isapre
        PagoIsapre = int(sueldoBruto*0.07)
        print ("Pago de ISAPRE:", PagoIsapre)
    else: #Realizar el siguietne calculo cuando el sueldo bruto es mayor al limite de Isapre
        PagoIsapre = int(limiteIsapre * 0.07)
        print("Pago de ISAPRE", PagoIsapre)

    #Realizar calculo de seguro de cesantia 
    limiteCesante = int(122.7*uf)
    if sueldoBruto <= limiteCesante: #Realizar calculo cuando el sueldo bruto es menor al limite de Seguro de Cesantia
        cesantiaTrabajador = int(sueldoBruto*0.006)
        cesantiaEmpleador = int(sueldoBruto*0.024)
        print("Seguro de censantía empleado:", cesantiaTrabajador)
        print("Seguro de cesantía empleador", cesantiaEmpleador)
    else: #Realizar el siguiente calculo cuando el sueldo bruto es mayor al limite de Seguro de Cesantia
        cesantiaTrabajador = int(limiteCesante*0.006)
        cesantiaEmpleador = int(limiteCesante*0.024)
        print("Seguro de censantía empleado:", cesantiaTrabajador)
        print("Seguro de cesantía empleador", cesantiaEmpleador)

    #Realizar calculo de impuesto unico (no contar censantia del empleador ya que no lo paga el trabajador)
    sueldoImponible = sueldoBruto - calculoAFP - comisionAFP - PagoIsapre  - cesantiaTrabajador 

    #Realizar el calculo de renta liquida imponible de acuerdo a los datos del Servicio Impuesto Interno (SII)
    if sueldoImponible > 0 and sueldoImponible <= 704875.5: 
        print("El sueldo liquido imponible:", sueldoImponible )
        print("El sueldo liquido a pagar", sueldoImponible)

    elif sueldoImponible > 704875.51 and sueldoImponible <= 1566390: 
        impuestoUnico = int((sueldoImponible * 0.04) - 28195.02)
        sueldoLiquido = int(sueldoImponible - impuestoUnico)
        print("Sueldo liquido imponible", sueldoImponible)
        print("Impuesto unico segunda categoria a pagar:", impuestoUnico)
        print("Sueldo liquido a pagar:", sueldoLiquido)

    elif sueldoImponible > 1566390 and sueldoImponible <= 2610650:
        impuestoUnico = int((sueldoImponible * 0.08) - 90850.62)
        sueldoLiquido = int(sueldoImponible - impuestoUnico)
        print("Sueldo liquido imponible", sueldoImponible)
        print("Impuesto unico segunda categoria a pagar:", impuestoUnico)
        print("Sueldo liquido a pagar:", sueldoLiquido)

    elif sueldoImponible > 2610650 and sueldoImponible <= 3654910:
        impuestoUnico = int((sueldoImponible * 0.135) - 234436.37)
        sueldoLiquido = int(sueldoImponible - impuestoUnico)
        print("Sueldo liquido imponible", sueldoImponible)
        print("Impuesto unico segunda categoria a pagar:", impuestoUnico)
        print("Sueldo liquido a pagar:", sueldoLiquido)

    elif sueldoImponible > 3654910 and sueldoImponible <= 4699170:
        impuestoUnico = int((sueldoImponible * 0.23) - 581652.82)
        sueldoLiquido = int(sueldoImponible - impuestoUnico)
        print("Sueldo liquido imponible", sueldoImponible)
        print("Impuesto unico segunda categoria a pagar:", impuestoUnico)
        print("Sueldo liquido a pagar:", sueldoLiquido)

    elif sueldoImponible > 4699170 and sueldoImponible <= 6265560:
        impuestoUnico = int((sueldoImponible * 0.304) - 9293910.4)
        sueldoLiquido = int(sueldoImponible - impuestoUnico)
        print("Sueldo liquido imponible", sueldoImponible)
        print("Impuesto unico segunda categoria a pagar:", impuestoUnico)
        print("Sueldo liquido a pagar:", sueldoLiquido)

    elif sueldoImponible > 6265560 and sueldoImponible <= 16186030:
        impuestoUnico = int((sueldoImponible * 0.35) - 1217607.16)
        sueldoLiquido = int(sueldoImponible - impuestoUnico)
        print("Sueldo liquido imponible", sueldoImponible)
        print("Impuesto unico segunda categoria a pagar:", impuestoUnico)
        print("Sueldo liquido a pagar:", sueldoLiquido)

    elif sueldoImponible > 16186030:
        impuestoUnico = int((sueldoImponible * 0.4) - 2026908.66)
        sueldoLiquido = int(sueldoImponible - impuestoUnico)
        print("Sueldo liquido imponible", sueldoImponible)
        print("Impuesto unico segunda categoria a pagar:", impuestoUnico)
        print("Sueldo liquido a pagar:", sueldoLiquido)

    else: 
        print("El sueldo ingresado no es posible calcular")

else: 
    print ("Ingrese el sueldo correctamente")
