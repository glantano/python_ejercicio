#Escribe un programa que reciba como parámetro el día y el mes del cumpleaños de una persona (como números enteros) y que imprima el signo del zodíaco al que pertenece.

#Para determinar las fechas de cada signo utiliza la columna Tropical Zodiac en la tabla de fechas que aparece en este link (Wikipedia).

dia = int(input("Ingrese dia de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento: "))

if mes == 1:
    if dia <= 20:
        print("Capricornio")
    else:
        print("Acuario")
elif mes == 2:
    if dia <= 18:
        print("Acuario")
    else:
        print("Piscis")
elif mes == 3:
    if dia <= 20:
        print("Piscis")
    else:
        print("Aries")
elif mes == 4:
    if dia <= 20:
        print("Aries")
    else:
        print("Tauro")
elif mes == 5:
    if dia <= 21:
        print("Tauro")
    else:
        print("Géminis")
elif mes == 6:
    if dia <= 21:
        print("Géminis")
    else:
        print("Cáncer")
elif mes == 7:
    if dia <= 22:
        print("Cáncer")
    else:
        print("Leo")
elif mes == 8:
    if dia <= 23:
        print("Leo")
    else:
        print("Virgo")
elif mes == 9:
    if dia <= 23:
        print("Virgo")
    else:
        print("Libra")
elif mes == 10:
    if dia <= 23:
        print("Libra")
    else:
        print("Escorpio")
elif mes == 11:
    if dia <= 22:
        print("Escorpio")
    else:
        print("Sagitario")
elif mes == 12:
    if dia <= 21:
        print("Sagitario")
    else:
        print("Capricornio")

else: 
    print("Datos incorrecto")