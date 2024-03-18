#se crea la clase Banco para almacenar el nombre y saldo de las cuentas
class Banco(): 
    #se define funcion para la creacion de los atributos de la clase
    def __init__(self,nombre,saldo):
        self.nombre = nombre
        self.saldo = saldo
    #se define funcion para cuando se realice el deposito
    def depositar(self, deposito):
        self.deposito = deposito
        self.saldo = self.saldo + self.deposito
        print("Tiene un saldo de", self.saldo)
    #se define funcion para cuando se realice el retiro
    def retirar (self, retiro):
        self.retiro = retiro
        self.saldo = self.saldo - self.retiro
        #en caso que el saldo quede en negativo envia mensaje de saldo insuficiente
        if self.saldo > 0:
            print("Tiene un saldo de", self.saldo)
        else: 
            print("No tiene saldo suficiente")

#se define atributos para la clase de Bancos
cuenta1 = Banco("Pedro", 5000)
cuenta2 = Banco("Juan", 1000)

#realiza un menu para las operaciones de deposito y retiro de las cuentas
retorno = "S"
while retorno =="S": 
    print ("CUENTA BANCARIA ")
    print("1-Realizar depósito")
    print("2-Realizar un retiro")

    #se solicita al usuario ingresar una operacion
    operacion = input("Ingrese operacion a solicitar: ")

    #se define las actividades de cada operacion segun lo solicitado por el usuario
    if operacion == "1": 
        valor = int(input("Escriba un monto de deposito: "))
        cuenta1.depositar(valor)
    elif operacion == "2": 
        valor = int(input("Escriba la cantidad a retirar: "))
        cuenta1.retirar(valor)
    else: 
        print("Ingrese una operación valida")

    #Se pregunta si desea otra operacion o se termina el programa
    otra_transaccion = input("¿Desea realizar otra transacción? (S/N): ")
    retorno = otra_transaccion.upper()
    