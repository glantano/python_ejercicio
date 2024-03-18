#calcula el digito verificador 

INPUT_1 = input("Ingrese el numero que desea calcular: ")
INPUT_2 = list(INPUT_1)
SERIE_1 = [2,3,4,5,6,7]
for i in range(len(INPUT_2)):
    INPUT_2[i] = int(INPUT_2[i])
 
OPERATION_LIST  = list(reversed(INPUT_2))
if len(OPERATION_LIST) == 8:
    OP_1 = OPERATION_LIST [0] * SERIE_1 [0]
    OP_2 = OPERATION_LIST [1] * SERIE_1 [1] 
    OP_3 = OPERATION_LIST [2] * SERIE_1 [2]    
    OP_4 = OPERATION_LIST [3] * SERIE_1 [3]
    OP_5 = OPERATION_LIST [4] * SERIE_1 [4]  
    OP_6 = OPERATION_LIST [5] * SERIE_1 [5] 
    OP_7 = OPERATION_LIST [6] * SERIE_1 [0]    
    OP_8 = OPERATION_LIST [7] * SERIE_1 [1]   
    ADITTION = OP_1 + OP_2 + OP_3 + OP_4 + OP_5 + OP_6 + OP_7 + OP_8
    REST_MODULE_11 = ADITTION % 11
    REST_11 = 11 - REST_MODULE_11
    if REST_11 == 11:
        print ("dv = 0")
    elif REST_11 == 10:
        print ("dv = K")
    else :
        print ("dv = " , REST_11)
if len(OPERATION_LIST) == 7:
    OP_1 = OPERATION_LIST [0] * SERIE_1 [0]    
    OP_2 = OPERATION_LIST [1] * SERIE_1 [1]   
    OP_3 = OPERATION_LIST [2] * SERIE_1 [2]      
    OP_4 = OPERATION_LIST [3] * SERIE_1 [3]
    OP_5 = OPERATION_LIST [4] * SERIE_1 [4]
    OP_6 = OPERATION_LIST [5] * SERIE_1 [5]
    OP_7 = OPERATION_LIST [6] * SERIE_1 [0]  
    ADITTION = OP_1 + OP_2 + OP_3 + OP_4 + OP_5 + OP_6 + OP_7 
    REST_MODULE_11 = ADITTION % 11
    REST_11 = 11 - REST_MODULE_11
    
    if REST_11 == 11:
        print ("dv = 0")
    elif REST_11 == 10:
        print ("dv = K")
    else :
        print ("dv = " , REST_11)
