#Montos iniciales
monto_inicial = int(input("Ingrese monto inicial: "))
tasa = int(input("Ingrese tasa de interes (%): "))
duracion = int(input("Ingrese duracion de prestamo (años): "))

#Calculo de prestamo 
resultado = monto_inicial*(1 + (tasa/100))**duracion
resultado = round(resultado,2)

print ("Con un monto inicial de", monto_inicial,"pesos, a una tasa de",tasa,"%","durante",duracion,"años, se tendrá", resultado,"pesos")