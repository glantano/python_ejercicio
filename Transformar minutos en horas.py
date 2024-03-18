#transforma minutos en horas

x = int(input("Ingrese minuto: "))

if  x >=60: 
    horas =  int(x//60)
    minuto = int(x%60)
    print(horas,"horas",minuto,"minutos")

elif 0 <= x <60:
    minuto = x
    print(minuto,"minutos") 

elif x < 0: 
    print("Ingrese numero positivo")

else: 
    "Ingrese numero positivo"