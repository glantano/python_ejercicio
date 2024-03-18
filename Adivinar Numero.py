#Adivinar un numero al azar entre el 1 y el 20.
from random import randint

numero_adivinar = randint(1,20)
intentos = 0
adivinado = False

while (intentos<5):
    numero = int(input("Ingrese numero entre 1 a 20: "))
    intentos = intentos + 1
    if numero == numero_adivinar:
        print ("Adivinaste, mi número era",numero_adivinar)
        adivinado = True
        break
    elif numero > numero_adivinar:
        print ("Mi número es menor")
    elif numero < numero_adivinar:
        print ("Mi número es mayor")

if not adivinado:
    print("No adivinaste, mi numero era", numero_adivinar)

