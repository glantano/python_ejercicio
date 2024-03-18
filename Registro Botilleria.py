
class LIQUIDS:
    def __init__(self, ID , LT , PR , BR):
        self.identifier = ID
        self.liters = LT
        self.price = PR
        self.brand = BR

class WHISKEY(LIQUIDS):
        def __init__(self, ID, LT , PR , BR , OR ):
            super().__init__(ID , LT , PR , BR)
            self.origen = OR

class DRINKS(LIQUIDS):
        def __init__(self, ID, LT , PR , BR , SU ):
            super().__init__(ID , LT , PR , BR)
            self.suguarpercent = SU

class DATA:
    def __init__(self , LI_LIST):
        self.liquids_list = LI_LIST

    def getTotal_drinks(self):  #REVISADO Y PROBADO
        PRICES_TOTAL_DRINKS = []
        for x in range (len(self.liquids_list)):
            if isinstance(self.liquids_list[x],DRINKS):
                PRICES_TOTAL_DRINKS.append(self.liquids_list[x].price)
            
        return print ('------El valor total de las BEBIDAS de la bodega es de :','$',sum(PRICES_TOTAL_DRINKS) ,'pesos------')
  
    def getTotal_whiskey(self): #REVISADO Y PROBADO
        PRICES_TOTAL_WHISKEY = []
        for x in range (len(self.liquids_list)):
            if isinstance(self.liquids_list[x], WHISKEY):
                PRICES_TOTAL_WHISKEY.append(self.liquids_list[x].price)
        return print ('-----El valor total de los WHISKEY de la bodega es de :','$',sum(PRICES_TOTAL_WHISKEY) ,'pesos-----')
        
    def getTotal(self): #REVISADO Y PROBADO
        PRICES_LIST = []
        for i in range (len(self.liquids_list)):
            PRICES_LIST.append(self.liquids_list[i].price)  
        return print ('-----El valor total de los PRODUCTOS de la bodega es de :','$',sum(PRICES_LIST) ,'pesos-----')
        
    def getID(self): #REVISADO Y PROBADO
        ID_LIST = []
        for i in range (len(self.liquids_list)):
            ID_LIST.append(self.liquids_list[i].identifier) 
        
        return print ('-----Actualmente en bodega existen ' , len(ID_LIST) , 'productos-----')
        
    def addProduct(self): #REVISADO Y PROBADO
        A = int(input('Seleccione el producto que desea agregar, 1  = WHISKEY  , 2 == BEBIDA: '))
        
        if A == 1 :
            B =  int(input('Ingrese la ID del producto : '  ))
            C =  float(input('Ingrese la cantidad de litros del producto: '))
            D =  int(input('Ingrese el precio del producto : '))
            E =  input('Ingrese la marca del producto : ')
            F =  input('Ingrese el origen del producto : ')
        
            P = WHISKEY(B,C,D,E,F)
            LI_LIST.append(P)
            print ('¡¡¡   Producto agregado exitosamente al inventario !!!')
            
            SHOW_LIST = []  
            for x in range (len(self.liquids_list)):
                SHOW_LIST.append(self.liquids_list[x].brand)
            print ('-----Los productos que se encuentran actualmente en el inventario son : ' ,SHOW_LIST ,'-----')
            
        
        elif A == 2 :
            B =  int(input('Ingrese la ID del producto : '  ))
            C =  float(input('Ingrese la cantidad de litros del producto: '))
            D =  int(input('Ingrese el precio del producto : '))
            E =  input('Ingrese la marca del producto : ' )
            F =   float(input('Ingrese el porcentaje de azucar : '))
            
            P = DRINKS(B,C,D,E,F)
            LI_LIST.append(P)
            print ('¡¡¡   Producto agregado exitosamente al inventario !!!')
            
            SHOW_LIST = []  
            for x in range (len(self.liquids_list)):
                SHOW_LIST.append(self.liquids_list[x].brand)
            print ('-----Los productos que se encuentran actualmente en el inventario son : ' ,SHOW_LIST , '-----')
        
    def deleteProduct(self): #REVISADO Y PROBADO
        A = int(input('Ingrese la ID del producto que desea eliminar : '))
        
        NEW_LIST = []   
        for x in range(len(self.liquids_list)):
            if A == (self.liquids_list[x].identifier):
                del LI_LIST[x]
                print('-----Producto eliminado del inventario-----')
                for i in range (len(self.liquids_list)):
                    NEW_LIST.append(self.liquids_list[i].brand)
                    
            return print ('-----Los productos que quedan actualmente en el inventario son : ' ,NEW_LIST, '-----')
        
    def dictTest(self): #REVISADO Y PROBADO
        
        PRODUCTS = {}
        for x in range (len(self.liquids_list)):
            PRODUCTS[self.liquids_list[x].identifier] = self.liquids_list[x].brand

        LITROS = {}
        for x in range (len(self.liquids_list)):
            LITROS[self.liquids_list[x].identifier] = self.liquids_list[x].liters
        
        PRECIOS = {}
        for x in range (len(self.liquids_list)):
            PRECIOS[self.liquids_list[x].identifier] = self.liquids_list[x].price

        A = int(input('Inserte la ID del producto que desea buscar : '))    
        TEST = PRODUCTS.get(A)
        print ('-----La ID corresponde al producto : ' , TEST , '-----')
        print ('-----El total de litros de ese producto es de : ' , LITROS.get(A) , '-----')
        print ('-----El precio de ese producto es de : ' , PRECIOS.get(A) , '-----')

    def getdetails(self): 
        for i in range(len(self.liquids_list)):
            print('\n')
            print('-----ID : ', self.liquids_list[i].identifier)
            print('-----Marca : ', self.liquids_list[i].brand)  
 

LIQUID_1 = WHISKEY(1234 , 1 , 25000 , 'JACK DANIELS' , 'EEUU')
LIQUID_2 = WHISKEY(5678 , 0.7 , 15990 , 'BOURBON N7' , 'ESCOCIA')
LIQUID_3 = DRINKS(4321 , 2 , 2300 , 'COCA COLA' , 15)
LIQUID_4 = DRINKS(8765 , 1.5 , 1350 , 'PEPSI' , 12)

LI_LIST = [LIQUID_1,LIQUID_2,LIQUID_3,LIQUID_4]
DATA_CALCS = DATA(LI_LIST)

while  True :



    print ('****************************************************')
    print ('              BOTILLERIA DE GIOVANNI                ')
    print ('****************************************************')
    
    print ('\n')
    print ('1. OBTENER EL VALOR TOTAL DE BEBIDAS EN INVENTARIO')
    print ('2. OBTENER EL VALOR DE WHISKEY EN EL INVENTARIO')
    print ('3. OBTENER EL VALOR TOTAL DE PRODUCTOS EN EL INVENTARIO')
    print ('4. OBTENER TOTAL DE PRODUCTOS EN EL INVENTARIO ')
    print ('5. AGREGAR UN NUEVO PRODUCTO AL INVENTARIO')
    print ('6. ELIMINAR UN PRODUCTO DEL INVENTARIO')
    print ('7. OBTENER DETALLES DE PRODUCTOS EN EL INVENTARIO')
    print ('8. BUSCAR PRODUCTOS EN EL INVENTARIO POR ID')
    print ('9. SALIR')
    print ('\n')

    OPTION_1 = int(input('SELECCIONE UNA OPCION : '))
    print ('\n')
    
    if OPTION_1 == 1 :
        DATA_CALCS.getTotal_drinks()
        print('\n')
        
    elif OPTION_1 == 2 :
        DATA_CALCS.getTotal_whiskey()
        print('\n')
        
    elif OPTION_1 == 3 : 
        DATA_CALCS.getTotal()
        print('\n')
        
    elif OPTION_1 == 4 : 
        DATA_CALCS.getID()
        print('\n')
        
    elif OPTION_1 == 5 : 
        DATA_CALCS.addProduct()
        print('\n')
        
    elif OPTION_1 == 6 :
        DATA_CALCS.deleteProduct()
        print('\n')
    
    elif OPTION_1 == 7 :
        DATA_CALCS.getdetails()
        print('\n')
        
    elif OPTION_1 == 8 : 
        DATA_CALCS.dictTest()
        print('\n')
        
    elif OPTION_1 == 9:
        break
        
