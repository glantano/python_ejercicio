#Realizar un programa que calcule el promedio y si el alumno se exime del ramo
#este ejemplo funcionaba con un archivo txt que traia los datos

dato = input("Favor ingrese string:2021073120552060406510661070:")

#Separamos el string y le asigno una variable a cada información
año = dato[0:4] #2021
mes = dato[4:6] #07
dia = dato[6:8] #31
porcentajeSolemne1 = (int(dato[8:10])) #20
notaSolemne1 = (int(dato[10:12])/10) #5.5
porcentajeSolemne2 = (int(dato[12:14])) #20 
notaSolemne2 = (int(dato[14:16])/10) #6.0
porcentajeTarea = (int(dato[16:18])) #40
notaTarea = (int(dato[18:20])/10) #6.5
porcentajeActividad = (int(dato[20:22])) #10
notaActividad = (int(dato[22:24])/10) #6.6
porcentajeEDX = (int(dato[24:26])) #10
notaEDX = (int(dato[26:28])/10) #7.0

#Entrega información de acuerdo al string
print("Con fecha:", dia,"/",mes,"/",año)
print("Nota Solemne 1 que corresponde al", porcentajeSolemne1,"porciento, la nota es:", notaSolemne1)
print("Nota Solemne 2 que corresponed al", porcentajeSolemne2,"porciento, la nota es:", notaSolemne2)
print("Nota de Tarea que corresponde al", porcentajeTarea,"porciento, la nota es:", notaTarea)
print("Nota de Actividades que corresponde al", porcentajeActividad,"porciento, la nota es:", notaActividad)
print("Nota de EDX que corresponde al", porcentajeEDX,"porciento, la nota es:", notaEDX)

#A continuación se calcula la ponderación para cada nota
nota1 = (notaSolemne1*(porcentajeSolemne1/100))
nota2 = (notaSolemne2*(porcentajeSolemne2/100))
nota3 = (notaTarea*(porcentajeTarea/100))
nota4 = (notaActividad*(porcentajeActividad/100))
nota5= (notaEDX*(porcentajeEDX/100))

#Realizo calculo de promedio sumando todas las notas ponderadas
x = (nota1 + nota2 + nota3 + nota4 + nota5)
promedio = round(x,1)
print("La nota de presentación correponde a:", promedio)

#Entrego información de acuerdo a su promedio
if promedio >= 4.0: 
    print("Felicitaciones! Está eximido")

else: 
    print("Usted esta reprobado")