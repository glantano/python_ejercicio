class personas :
    def __init__(self,nombre,apellido,identificacion,estadocivil,nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.estadocivil = estadocivil
        self.nacimiento = nacimiento

class estudiantes (personas):
    def __init__(self,nombre,apellido,identificacion,estadocivil,nacimiento,curso):
        super().__init__(nombre,apellido,identificacion,estadocivil,nacimiento)
        self.curso = curso

class profesor (personas):
    def __init__(self,nombre,apellido,identificacion,estadocivil,nacimiento,departamento,tipocontrato):
        super().__init__(nombre,apellido,identificacion,estadocivil,nacimiento)
        self.departamento = departamento
        self.contrato = tipocontrato

class personal (personas):
    def __init__(self,nombre,apellido,identificacion,estadocivil,nacimiento,anoincorporacion,pisoasignado,seccion):
        super().__init__(nombre,apellido,identificacion,estadocivil,nacimiento)
        self.anoincorporacion = anoincorporacion
        self.pisoasignado = pisoasignado
        self.seccion = seccion

class resultado(estudiantes,profesor,personal):
    def __init__(self,estudiantes,profesores,personal):
        self.estudiantes = estudiantes
        self.profesores = profesores
        self.personal = personal
    
    def cambiocivilestudiantes(self):
        print ('\n')
        for i in range (len(self.estudiantes)):
            print ("El estudiante", self.estudiantes[i].nombre,"su estado civil es:", self.estudiantes[i].estadocivil)
            cambio = input("Ingrese el nuevo estado civil: ")
            self.estudiantes[i].estadocivil = cambio
            print ('\n')
    
    def cambiocivilprofesor(self):
        print ('\n')
        for i in range (len(self.profesores)):
            print ("El profesor", self.profesores[i].nombre,"su estado civil es:", self.profesores[i].estadocivil)
            cambio = input("Ingrese el nuevo estado civil: ")
            self.profesores[i].estadocivil = cambio
            print ('\n')
    
    def cambiocivilpersonal(self):
        print ('\n')
        for i in range (len(self.personal)):
            print ("El personal", self.personal[i].nombre,"su estado civil es:", self.personal[i].estadocivil)
            cambio = input("Ingrese el nuevo estado civil: ")
            self.personal[i].estadocivil = cambio
            print ('\n')
    
    def cambiopiso(self):
        print ('\n')
        for i in range (len(self.personal)):
            print ("El personal", self.personal[i].nombre,"su piso asignado es:", self.personal[i].pisoasignado)
            cambio = input("Ingrese el nuevo piso: ")
            self.personal[i].pisoasignado = cambio
            print ('\n')
        
    def cambiocurso(self):
        print ('\n')
        for i in range (len(self.estudiantes)):
            print ("El estudiante", self.estudiantes[i].nombre,"su curso es:", self.estudiantes[i].curso)
            cambio = input("Ingrese el nuevo curso: ")
            self.estudiantes[i].curso = cambio
            print ('\n')
    
    def cambiodepartamento(self):
        print ('\n')
        for i in range (len(self.profesores)):
            print ("El profesor", self.profesores[i].nombre,"su departamento es:", self.profesores[i].departamento)
            cambio = input("Ingrese el nuevo departamento: ")
            self.profesores[i].departamento = cambio
            print ('\n')
    
    def calculoedadestudiantes(self):
        print ('\n')
        for i in range (len(self.estudiantes)):
            edad = 2020 - self.estudiantes[i].nacimiento
            print ("El estudiante", self.estudiantes[i].nombre,"tiene", edad, "años")
            print ('\n')
    
    def calculoedadprofesores(self):
        print ('\n')
        for i in range (len(self.profesores)):
            edad = 2020 - self.profesores[i].nacimiento
            print ("El profesor", self.profesores[i].nombre,"tiene", edad, "años")
            print ('\n')

    def calculoedadpersonal(self):
        print ('\n')
        for i in range (len(self.personal)):
            edad = 2020 - self.personal[i].nacimiento
            print ("El personal", self.personal[i].nombre,"tiene", edad, "años")
            print ('\n')
    
    def imprimir (self):
        print ('\n')
        for i in range (len(self.estudiantes)):
            print ("El estudiante", self.estudiantes[i].nombre,self.estudiantes[i].apellido,"cuya identificacion es", self.estudiantes[i].identificacion,"su estado civil es:", self.estudiantes[i].estadocivil,"su año de nacimiento es:", self.estudiantes[i].nacimiento,"su curso es:", self.estudiantes[i].curso)
            print ('\n')
        for i in range (len(self.profesores)):
            print ("El profesor", self.profesores[i].nombre,self.profesores[i].apellido,"cuya identificacion es", self.profesores[i].identificacion,"su estado civil es:", self.profesores[i].estadocivil,"su año de nacimiento es:", self.profesores[i].nacimiento,"su departamento es:", self.profesores[i].departamento,"su tipo de contrato es:", self.profesores[i].contrato)
            print ('\n')
        for i in range (len(self.personal)):
            print ("El personal", self.personal[i].nombre,self.personal[i].apellido,"cuya identificacion es", self.personal[i].identificacion,"su estado civil es:", self.personal[i].estadocivil,"su año de nacimiento es:", self.personal[i].nacimiento,"su año de incorporacion es:", self.personal[i].anoincorporacion,"su piso asignado es:", self.personal[i].pisoasignado,"su seccion es:", self.personal[i].seccion)
            print ('\n')

estudiante_1 = estudiantes("Juan", "Perez", "12345", "Soltero", 1995, "Matematica")
estudiante_2 = estudiantes("Pedro", "Gomez", "23456", "Casado", 1997, "Fisica")
estudiante_3 = estudiantes("Maria", "Lopez", "34567", "Soltera", 1995, "Quimica")

profesor_1 = profesor("Gabriel", "Gonzalez", "45678", "Soltero", 1995, "Matematica", "Jornada Completa")
profesor_2 = profesor("Roberto", "Garcia", "56789", "Casado", 1970, "Fisica", "Jornada Anexo")
profesor_3 = profesor("Cristian", "Vera", "67890", "Viudo", 1980, "Quimica", "Jornada Adjunta")

personal_1 = personal("Alexander", "Muñoz", "78901", "Soltero", 1967, 2000 , "1", "Biblioteca")
personal_2 = personal("Miguel", "Tapia", "89012", "Casado", 1956, 1990 , "2", "Cafeteria")
personal_3 = personal("Kevin", "Perez", "90123", "Viudo", 1965, 1997 , "3", "Decanato")

resultados = resultado ([estudiante_1, estudiante_2, estudiante_3], [profesor_1, profesor_2, profesor_3], [personal_1, personal_2, personal_3])

while True:
    print ('\n')
    print ('1. Cambio estado civil de una persona')
    print ('2. Reasignacion de piso de personal')
    print ('3. Cambio curso de estudiantes')
    print ('4. Cambio de departamento de profesores')
    print ('5. Calculo edad actual de una persona')
    print ('6. Imprimir datos')
    print ('7. Salir')
    print ('\n')

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print ('\n')
        print ("1. Cambio estado civil de un estudiante")
        print ("2. Cambio estado civil de un profesor")
        print ("3. Cambio estado civil de un personal")
        print ('\n')
        opcion2 = input("Ingrese una opcion: ")
        if opcion2 == "1":
            resultados.cambiocivilestudiantes()
        elif opcion2 == "2":
            resultados.cambiocivilprofesor()
        elif opcion2 == "3":
            resultados.calculoedadpersonal()
        else:
            print ("Opcion invalida")
    
    elif opcion == "2":
        resultados.cambiopiso()
        
    elif opcion == "3":
        resultados.cambiocurso()    
    
    elif opcion == "4":
        resultados.cambiodepartamento()
    
    elif opcion == "5":
        print ('\n')
        print ("1. Calcular edad de un estudiante")
        print ("2. Calcular edad de un profesor")
        print ("3. Calcular edad de un personal")
        print ('\n')
        opcion3 = input("Ingrese una opcion: ")
        if opcion3 == "1":
            resultados.calculoedadestudiantes()
        elif opcion3 == "2":
            resultados.calculoedadprofesores()
        elif opcion3 == "3":
            resultados.calculoedadpersonal()
        else:
            print ("Opcion invalida")
    
    elif opcion == "6":
        resultados.imprimir()

    elif opcion == "7":
        break