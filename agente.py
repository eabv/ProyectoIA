import random
class Casas(object):
    '''
    Clase Casas
    '''
    def __init__(self):
        self.ubicacionestado =  {'C1': random.randint(0,1), 'C2': random.randint(0,1), 'C3': random.randint(0,1), 
                                'C4': random.randint(0,1), 'C5': random.randint(0,1), 'C6': random.randint(0,1),
                                'C7': random.randint(0,1)}
class EntornoCondominios(Casas):
  def __init__(self, casa):
    print("---------- AIRE ACONDICIONADO INTELIGENTE -----------")
    print("Estado: ")
    print(casa.ubicacionestado)
    ubicacion = random.randint(0,6)
    costo=0

####################################################################################################
    if ubicacion == 0:
            
            if casa.ubicacionestado['C1'] == 1:
                print("Se detecta movimiento en la cas 1 ")
                casa.ubicacionestado['C1'] == 0
                costo = costo + 1
                print("Se activa el aire acondicionado en la casa 1, el agente pasa a la casa 2")
                print("costo:", costo, "\n")  

                if casa.ubicacionestado['C2'] == 1:
                    print("Se detecta movimiento en la casa 2")
                    casa.ubicacionestado['C2'] == 0
                    costo = costo + 1                      
                    print("Se activa el aire acondicionado en la casa 2, el agente pasa a la casa 3")
                    print("costo:", costo, "\n")    

                else:
                   print("El agente no detecta movimiento en la casa 2, el agente pasa a la casa 3\n")

                if casa.ubicacionestado['C3'] == 1:
                         print("Se detecta movimiento en la cas 3")
                         casa.ubicacionestado['C3'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 3, el agente pasa a la casa 4")
                         print("costo:", costo, "\n")   
                         
                else:
                     print("El agente no detecta movimiento en la casa 3, el agente pasa a la casa 4\n")
                                
                if casa.ubicacionestado['C4'] == 1:
                         print("Se detecta movimiento en la cas 4 ")
                         casa.ubicacionestado['C4'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 4, el agente pasa a la casa 5")
                         print("costo:", costo, "\n")  
                else:
                     print("El agente no detecta movimiento en la casa 4, el agente pasa a la casa 5\n")     
                
                if casa.ubicacionestado['C5'] == 1:
                         print("Se detecta movimiento en la cas 5 ")
                         casa.ubicacionestado['C5'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                         print("costo:", costo, "\n")  
                else:
                     print("El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")
                    
                if casa.ubicacionestado['C6'] == 1:
                         print("Se detecta movimiento en la casa 6 ")
                         casa.ubicacionestado['C6'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 6, el agente pasa a la casa 7")
                         print("costo:", costo, "\n")  
                else:
                     print("El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")
                
                if casa.ubicacionestado['C7'] == 1:
                         print("Se detecta movimiento en la casa 7")
                         casa.ubicacionestado['C7'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 7")
                         print("Total de costo:", costo)  
                else:
                     print("El agente no detecta movimiento en la casa 7\n")
                     print("Total de costo:", costo)              

