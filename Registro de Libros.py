#ingresa 5 libros con tus evaluaciones y te dará un promedio.

class Libro :
    def __init__ (self, titulo, autor, paginas, pais, calificacion):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pais = pais
        self.calificacion = calificacion

class Calificacion:
    def __init__ (self, libro):
        self.libro = libro

    def promedio(self):
        suma = 0
        i = 0
        while i < len(self.libro): 
            suma = suma + self.libro[i].calificacion
            i = i + 1
        promedio = round((suma /4),1)
        print("El promedio de evaluación de los libro es:", promedio)

    def mejor_libro(self): 
        mejor = []
        for i in range (len(self.libro)):
            mejor.append(self.libro[i].calificacion)
            mejor_libro = self.libro[mejor.index(max(mejor))].titulo
        print("El mejor libro es", mejor_libro,"con una calificación de:", max(mejor))

    def ingreso_libro (self):
        i = 1
        while i < 5:
            print('\n')
            print ("Datos del libro", i)
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            paginas = int(input("Ingrese el número de páginas del libro: "))
            pais = input("Ingrese el país de publicación del libro: ")
            calificacion = int(input("Ingrese la calificación del libro: "))
            self.libro.append(Libro(titulo, autor, paginas, pais, calificacion))
            i = i + 1

    def mostrar_libro (self):
        for i in range (len(self.libro)):
            print('\n')
            print("Titulo:", self.libro[i].titulo)
            print("Autor:", self.libro[i].autor)
            print("Número de páginas:", self.libro[i].paginas)
            print("País de publicación:", self.libro[i].pais)
            print("Calificación:", self.libro[i].calificacion)
            

datos = Calificacion([])
datos.ingreso_libro()
datos.mostrar_libro()
datos.promedio()
datos.mejor_libro()





