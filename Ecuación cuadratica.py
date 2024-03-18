#clase realizada el dia 19-07-2021

a = int(input("Ingrese 'a': "))
b = int(input("Ingrese 'b': "))
c = int(input("Ingrese 'c': "))

discriminante =  ((b**2) - (2*a*c))

if discriminante >= 0: 
    resultado1 = (- b - discriminante**(1/2))/2*a
    resultado2 = (- b + discriminante**(1/2))/2*a
    print (f"Los resultado de la ecuacion cuadratica es {resultado1} y {resultado2}")

else:
    print("El resultado no existe")