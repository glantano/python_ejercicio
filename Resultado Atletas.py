#Se define la clase "Atleta" con sus respectivos atributos
class Atleta :
    def __init__(self,nombre,rut,ciudadania,registro):
        self.nombre = nombre
        self.rut = rut
        self.ciudadania = ciudadania
        self.registro = registro

#Se define la clase "Puntaje" con el atributo "Atleta" donde almacena una lista con todos los Atletas
class Puntaje:
    def __init__(self,atletas):
        self.atletas = atletas
    
    #Se trabaja a traves de funciones y For In en los siguientes Metodos:
    def maximo(self):
        for i in range (len(self.atletas)):
            maximo = max(self.atletas[i].registro)
            print ("El máximo de", self.atletas[i].nombre, "es de:", maximo)
        print ("--------------------------------------------")

    def promedio(self):
        for i in range (len(self.atletas)):
            promedio = round((sum(self.atletas[i].registro)/len(self.atletas[i].registro)),1)
            print ("El promedio de", self.atletas[i].nombre, "es de:", promedio)
        print ("--------------------------------------------")

    def mediana(self):
        for i in range (len(self.atletas)):
            mediana = sorted(self.atletas[i].registro)[len(self.atletas[i].registro)//2]
            print ("La mediana de", self.atletas[i].nombre, "es de:", mediana)
        print ("--------------------------------------------")

    def mejor (self):
        mejor = []
        for i in range (len(self.atletas)):
            mejor.append(max(self.atletas[i].registro))
            mejor_atleta = self.atletas[mejor.index(max(mejor))].nombre
        print ("El mejor salto es de", mejor_atleta , "con una distancia de:", max(mejor))
        print ("--------------------------------------------")

    def confiable(self):
        confiable = 0
        for i in range (len(self.atletas)):
            promedio = sum(self.atletas[i].registro)/len(self.atletas[i].registro)
            mediana = sorted(self.atletas[i].registro)[len(self.atletas[i].registro)//2]
            if promedio  + mediana > confiable:
                confiable = promedio + mediana
                atleta = self.atletas[i]
        print ("El atleta", atleta.nombre, "es el más confiable")
        print("Tiene la mayor distancia promedio y mediana con una suma de :", round(confiable,1))

#Informacion de los atletas y su Clase
atleta1 = Atleta("Juan","1234567","Concepcion",[3.4,3.7,3.6])
atleta2 = Atleta("Javier","65675","Santiago",[2.9,3.7,2.6])
atleta3 = Atleta("Marcos","86594","Valparaiso",[2.3,3.9,3.6])
atleta4 = Atleta("Luis","6894945","Valdivia",[3.1,3.2,3.2])

#Lista que almacena información de todos los atletas
resultados = Puntaje([atleta1,atleta2,atleta3,atleta4])

#Se imprime los resultados
resultados.maximo()
resultados.promedio()
resultados.mediana()
resultados.mejor()
resultados.confiable()