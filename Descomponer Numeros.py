#Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue la descomposición en Unidades, Decenas, Centenas y Miles. Ejemplos

#Para 1230 debe imprimir: 1M + 2C + 3D + 0U
#Para 36 debe imprimir: 3D + 6U

numero = int(input("Ingrese numero hasta 4 digitos"))

numero_miles = int(numero/1000)
numero_centena = int((numero - (numero_miles*1000)) / 100)
numero_decena = int((numero - (numero_miles*1000 + numero_centena*100))/ 10)
numero_unidad = int (numero - (numero_miles*1000 + numero_centena*100 + numero_decena*10))

if numero_miles == 0 and numero_centena >= 1:
    print (numero_centena,"C +",numero_decena,"D +",numero_unidad,"U")
elif numero_miles == 0 and numero_centena == 0 and numero_decena >= 1:
    print (numero_decena,"D +",numero_unidad,"U")
elif numero_miles == 0 and numero_centena == 0 and numero_decena == 0 and numero_unidad >= 1:
    print (numero_unidad,"U")
else:
    print (numero_miles,"M +",numero_centena,"C +",numero_decena,"D +",numero_unidad,"U")

