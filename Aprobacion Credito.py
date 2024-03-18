#Aprobación de créditos
ingreso = int(input("Ingrese sueldo: "))
nacimiento = int(input("Ingrese año de que nace: "))
hijos = int(input("Ingrese numero de hijos: "))
permanencia = int(input("Ingrese años de permanencia en el banco: "))
estado_civil = input("Ingrese si esta casado (C) o soltero (S): ")
vive = input("Ingrese si vive en zona urbano (U) o rural (R): ")

if (permanencia > 10) and (hijos >= 2):
    print("APROBADO")

elif estado_civil == "C" and 45 < (2021 - nacimiento) < 55: 
    print("APROBADO")

elif ingreso > 2500000 and estado_civil =="C" and vive =="U":
    print("APROBADO")

elif ingreso > 3500000 and (permanencia > 5): 
    print("APROBADO")

elif vive=="R" and hijos <2: 
    print("APROBADO")

else: 
    print("RECHAZADO")