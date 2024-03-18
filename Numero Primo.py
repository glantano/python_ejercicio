#Escribe una función llamada es_primo que retorne True cuando un número es primo y False cuando no lo es.
def es_primo(num):
    if num == 1 :
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True