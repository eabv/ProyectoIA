'''
INSTRUCCIONES:  
    Activado = 0 ; Desactivado = 1
UBICACIONES:
    Casa 1 = C1, Casa 2 = C2, Casa 3 = C3, Casa 4 = C4,
    Casa 5 = C5, Casa 6 = C6, Casa 7 = C7
'''
import random


class Casas(object):
    """
    Clase objeto representación de Casas
    .......
    Métodos
    -------
    __init__():
        Constructor de la clase de Casas
    """

    def __init__(self):
        """
        Clase Entorno Condominios con el objeto Casas
        .......
        Parámetros
        ----------
        ubicacionestado : 
            Indica las ubicaciones con su estado
        """
        self.ubicacionestado = {'C1': random.randint(0, 1), 'C2': random.randint(0, 1), 'C3': random.randint(0, 1),
                                'C4': random.randint(0, 1), 'C5': random.randint(0, 1), 'C6': random.randint(0, 1),
                                'C7': random.randint(0, 1)}
# Clase Entorno Condominios


class EntornoCondominios(Casas):
    """
    Clase Entorno Condominios con el objeto Casas
    .......
    Métodos
    -------
    __init__():
        Constructor de la clase de Entorno Condominios
    """

    def __init__(self, casa):
        '''
        Método constructor de la clase Entorno Condominios, inicializa sus parámetros

        Parámetros:
        casa : String
            Parámetro de ubicacion y estado
        ubicacion : int
            Número de ubicacion entre 1-6
        costo : int  
            Inicialización del costo
        '''
        print("---------- AIRE ACONDICIONADO INTELIGENTE -----------")
        print("Estado: ")
        # Impresión de la ubicación
        print(casa.ubicacionestado)
        ubicacion = random.randint(0, 6)
        # Inicilización del costo
        costo = 0

####################################################################################################
        # Condicional para el estado activo
        if ubicacion == 0:
            # Si en la casa C1 detecta movimiento cuando C1 == 1
            if casa.ubicacionestado['C1'] == 1:
                # Imprime el estado al que se cambia y el incremento del costo
                print("Se detecta movimiento en la cas 1 ")
                casa.ubicacionestado['C1'] == 0
                costo = costo + 1
                # Activa el aire acondicionado y pasa a la siguiente ubicación
                print(
                    "Se activa el aire acondicionado en la casa 1, el agente pasa a la casa 2")
                print("costo:", costo, "\n")

                # Si en la casa C2 detecta movimiento cuando C2 == 1
                if casa.ubicacionestado['C2'] == 1:
                    # Imprime el estado al que se cambia y el incremento del costo
                    print("Se detecta movimiento en la casa 2")
                    casa.ubicacionestado['C2'] == 0
                    costo = costo + 1
                    # Activa el aire acondicionado y pasa a la siguiente ubicación
                    print(
                        "Se activa el aire acondicionado en la casa 2, el agente pasa a la casa 3")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 2, el agente pasa a la casa 3\n")

                if casa.ubicacionestado['C3'] == 1:
                    print("Se detecta movimiento en la cas 3")
                    casa.ubicacionestado['C3'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 3, el agente pasa a la casa 4")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 3, el agente pasa a la casa 4\n")

                if casa.ubicacionestado['C4'] == 1:
                    print("Se detecta movimiento en la cas 4 ")
                    casa.ubicacionestado['C4'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 4, el agente pasa a la casa 5")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 4, el agente pasa a la casa 5\n")

                if casa.ubicacionestado['C5'] == 1:
                    print("Se detecta movimiento en la cas 5 ")
                    casa.ubicacionestado['C5'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")

                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6 ")
                    casa.ubicacionestado['C6'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 6, el agente pasa a la casa 7")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")

                if casa.ubicacionestado['C7'] == 1:
                    print("Se detecta movimiento en la casa 7")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 7")
                    print("Total de costo:", costo)
                else:
                    print("El agente no detecta movimiento en la casa 7\n")
                    print("Total de costo:", costo)
            else:
                print(
                    "El agente no detecta movimiento en la casa 1, el agente pasa a la casa 2\n")

                if casa.ubicacionestado['C2'] == 1:
                    print("Se detecta movimiento en la casa 2")
                    casa.ubicacionestado['C2'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 2, el agente pasa a la casa 3")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 2, el agente pasa a la casa 3\n")

                if casa.ubicacionestado['C3'] == 1:
                    print("Se detecta movimiento en la casa 3")
                    casa.ubicacionestado['C3'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 3, el agente pasa a la casa 4")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 3, el agente pasa a la casa 4\n")

                if casa.ubicacionestado['C4'] == 1:
                    print("Se detecta movimiento en la casa 4")
                    casa.ubicacionestado['C4'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 4, el agente pasa a la casa 5")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 4, el agente pasa a la casa 5\n")

                if casa.ubicacionestado['C5'] == 1:
                    print("Se detecta movimiento en la casa 5")
                    casa.ubicacionestado['C5'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")

                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6")
                    casa.ubicacionestado['C6'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 6, el agente pasa a la casa 7")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")

                if casa.ubicacionestado['C7'] == 1:
                    print("Se detecta movimiento en la casa 7")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 7")
                    print("Total de costo:", costo, "\n")

                else:
                    print("El agente no detecta movimiento en la casa 7\n")
                    print("Total de costo:", costo)

######################################################################################################################
        #Ubicación de la casa 1 si detecta movimiento activa el aire acondicionado 
        elif ubicacion == 1:

            if casa.ubicacionestado['C2'] == 1:
                print("Se detecta movimiento en la casa 2")
                casa.ubicacionestado['C2'] == 0
                costo = costo + 1
                print(
                    "Se activa el aire acondicionado en la casa 2, el agente pasa a la casa 3")
                print("costo:", costo, "\n")

                if casa.ubicacionestado['C3'] == 1:
                    print("Se detecta movimiento en la casa 3")
                    casa.ubicacionestado['C3'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 3, el agente pasa a la casa 4")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 3, el agente pasa a la casa 4\n")

                if casa.ubicacionestado['C4'] == 1:
                    print("Se detecta movimiento en la casa 4")
                    casa.ubicacionestado['C4'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 4, el agente pasa a la casa 5")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 4, el agente pasa a la casa 5\n")
                if casa.ubicacionestado['C5'] == 1:
                    print("Se detecta movimiento en la casa 5 ")
                    casa.ubicacionestado['C5'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")
                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6 ")
                    casa.ubicacionestado['C6'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 6, el agente pasa a la cas 7")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")

                if casa.ubicacionestado['C7'] == 1:
                    print("Se detecta movimiento en la cas 7 ")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 7, el agente pasa a la cas 1")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 7, el agente pasa a la casa 1\n")

                if casa.ubicacionestado['C1'] == 1:
                    print("Se detecta movimiento en la casa 1")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 1")
                    print("Total de costo:", costo)
                else:
                    print("El agente no detecta movimiento en la casa 1\n")
                    print("Total de costo:", costo)
            else:

                print(
                    "El agente no detecta movimiento en la casa 2, el agente pasa a la casa 3\n")

                if casa.ubicacionestado['C3'] == 1:
                    print("Se detecta movimiento en la casa 3")
                    casa.ubicacionestado['C3'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 3, el agente pasa a la casa 4")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 3, el agente pasa a la casa 4\n")

                if casa.ubicacionestado['C4'] == 1:
                    print("Se detecta movimiento en la casa 4")
                    casa.ubicacionestado['C4'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 4, el agente pasa a la casa 5")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 4, el agente pasa a la casa 5\n")

                if casa.ubicacionestado['C5'] == 1:
                    print("Se detecta movimiento en la casa 5")
                    casa.ubicacionestado['C5'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")

                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6")
                    casa.ubicacionestado['C6'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 6, el agente pasa a la casa 7")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")

                if casa.ubicacionestado['C7'] == 1:
                    print("Se detecta movimiento en la casa 7")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 7, el agente pasa a la casa 1")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 7, el agente pasa a la casa 1\n")

                if casa.ubicacionestado['C1'] == 1:
                    print("Se detecta movimiento en la casa 1")
                    casa.ubicacionestado['C1'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 1")
                    print("Total de costo:", costo, "\n")

                else:
                    print("El agente no detecta movimiento en la casa 1\n")
                    print("Total de costo:", costo)

#########################################################################################################
        #El agente verifica si en la casa 2 se detecta movimiento realiza el activado del aire
        elif ubicacion == 2:

            if casa.ubicacionestado['C3'] == 1:
                print("Se detecta movimiento en la casa 3")
                casa.ubicacionestado['C3'] == 0
                costo = costo + 1
                print(
                    "Se activa el aire acondicionado en la casa 3, el agente pasa a la casa 4")
                print("costo:", costo, "\n")

                if casa.ubicacionestado['C4'] == 1:
                    print("Se detecta movimiento en la casa 4")
                    casa.ubicacionestado['C4'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 4, el agente pasa a la casa 5")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 4, el agente pasa a la casa 5\n")

                if casa.ubicacionestado['C5'] == 1:
                    print("Se detecta movimiento en la casa 5")
                    casa.ubicacionestado['C5'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")

                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6 ")
                    casa.ubicacionestado['C6'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 6, el agente pasa a la casa 7")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")

                if casa.ubicacionestado['C7'] == 1:
                    print("Se detecta movimiento en la casa 7")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 7, el agente pasa a la cas 1")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 7, el agente pasa a la casa 1\n")

                if casa.ubicacionestado['C1'] == 1:
                    print("Se detecta movimiento en la cas 1")
                    casa.ubicacionestado['C1'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 1, el agente pasa a la cas 2")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 1, el agente pasa a la casa 2\n")

                if casa.ubicacionestado['C2'] == 1:
                    print("Se detecta movimiento en la casa 2")
                    casa.ubicacionestado['C2'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 2")
                    print("Total de costo:", costo)
                else:
                    print("El agente no detecta movimiento en la casa 2\n")
                    print("Total de costo:", costo)

            # Si la casa 3 no detecta movimiento, el agente se mueve hacia la casa 4 y despues a la casa 5
            else:
                print(
                    "El agente no detecta movimiento en la casa 3, el agente pasa a la casa 4\n")

                if casa.ubicacionestado['C4'] == 1:
                    print("Se detecta movimiento en la casa 4")
                    casa.ubicacionestado['C4'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 4, el agente pasa a la casa 5")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 4, el agente pasa a la casa 5\n")

                if casa.ubicacionestado['C5'] == 1:
                    print("Se detecta movimiento en la casa 5")
                    casa.ubicacionestado['C5'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")

                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6")
                    casa.ubicacionestado['C6'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 6, el agente pasa a la casa 7")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")

                if casa.ubicacionestado['C7'] == 1:
                    print("Se detecta movimiento en la casa 7")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 7, el agente pasa a la casa 1")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 7, el agente pasa a la casa 1\n")

                if casa.ubicacionestado['C1'] == 1:
                    print("Se detecta movimiento en la casa 1")
                    casa.ubicacionestado['C1'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 1, el agente pasa a la casa 2")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 1, el agente pasa a la casa 2\n")

                if casa.ubicacionestado['C2'] == 1:
                    print("Se detecta movimiento en la casa 2")
                    casa.ubicacionestado['C2'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 2")
                    print("Total de costo:", costo, "\n")

                else:
                    print("El agente no detecta movimiento en la casa 2\n")
                    print("Total de costo:", costo)
        #En la ubicacion de la casa 3 detecta movimiento 

        elif ubicacion == 3:
            if casa.ubicacionestado['C4'] == 1:
                print("Se detecta movimiento en la casa 4")
                casa.ubicacionestado['C4'] == 0
                costo = costo + 1
                print(
                    "Se activa el aire acondicionado en la casa 4, el agente pasa a la casa 5")
                print("costo:", costo, "\n")

                if casa.ubicacionestado['C5'] == 1:
                    print("Se detecta movimiento en la casa 5")
                    casa.ubicacionestado['C5'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")

                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6")
                    casa.ubicacionestado['C6'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 6, el agente pasa a la casa 7")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")

                if casa.ubicacionestado['C7'] == 1:
                    print("Se detecta movimiento en la casa 7")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 7, el agente pasa a la casa 1")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 7, el agente pasa a la casa 1\n")

                if casa.ubicacionestado['C1'] == 1:
                    print("Se detecta movimiento en la casa 1")
                    casa.ubicacionestado['C1'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 1, el agente pasa a la cas 2")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 1, el agente pasa a la casa 2\n")

                if casa.ubicacionestado['C2'] == 1:
                    print("Se detecta movimiento en la casa 2")
                    casa.ubicacionestado['C2'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 2, el agente pasa a la casa 3")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 2, el agente pasa a la casa 3\n")

                if casa.ubicacionestado['C3'] == 1:
                    print("Se detecta movimiento en la casa 3")
                    casa.ubicacionestado['C3'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 3")
                    print("Total de costo:", costo)
                else:
                    print("El agente no detecta movimiento en la casa 3\n")
                    print("Total de costo:", costo)
            # Si la casa 4 No detecta movimiento sigue a la siguiente casa
            else:
                print(
                    "El agente no detecta movimiento en la casa 4, el agente pasa a la casa 5\n")

                if casa.ubicacionestado['C5'] == 1:
                    print("Se detecta movimiento en la casa 5")
                    casa.ubicacionestado['C5'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")

                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6")
                    casa.ubicacionestado['C6'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 6, el agente pasa a la casa 7")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 6, el agente pasa a la casa 7\n")

                if casa.ubicacionestado['C7'] == 1:
                    print("Se detecta movimiento en la casa 7")
                    casa.ubicacionestado['C7'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 7, el agente pasa a la casa 1")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 7, el agente pasa a la casa 1\n")

                if casa.ubicacionestado['C1'] == 1:
                    print("Se detecta movimiento en la casa 1")
                    casa.ubicacionestado['C1'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 1, el agente pasa a la casa 2")
                    print("costo:", costo, "\n")

                else:
                    print(
                        "El agente no detecta movimiento en la casa 1, el agente pasa a la casa 2\n")

                if casa.ubicacionestado['C2'] == 1:
                    print("Se detecta movimiento en la casa 2")
                    casa.ubicacionestado['C2'] == 0
                    costo = costo + 1
                    print(
                        "Se activa el aire acondicionado en la casa 2, el agente pasa a la casa 3")
                    print("costo:", costo, "\n")
                else:
                    print(
                        "El agente no detecta movimiento en la casa 2, el agente pasa a la casa 3\n")

                if casa.ubicacionestado['C3'] == 1:
                    print("Se detecta movimiento en la casa 3")
                    casa.ubicacionestado['C3'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 3")
                    print("Total de costo:", costo, "\n")

                else:
                    print("El agente no detecta movimiento en la casa 3\n")
                    print("Total de costo:", costo)
######################################################################################################################

#El agente comienza por la casa 5
        elif ubicacion == 4:
            
            if casa.ubicacionestado['C5'] == 1:
                print("Se detecta movimiento en la casa 5")
                casa.ubicacionestado['C5'] == 0
                costo = costo + 1
                print("Se activa el aire acondicionado en la casa 5, el agente pasa a la casa 6")
                print("costo:", costo, "\n") 

                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6")
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
                         print("Se activa el aire acondicionado en la casa 7, el agente pasa a la casa 1")
                         print("costo:", costo, "\n")   
                         
                else:
                     print("El agente no detecta movimiento en la casa 7, el agente pasa a la casa 1\n")
                                
                
                if casa.ubicacionestado['C1'] == 1:
                         print("Se detecta movimiento en la casa 1")
                         casa.ubicacionestado['C1'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 1, el agente pasa a la casa 2")
                         print("costo:", costo, "\n")  
                else:
                     print("El agente no detecta movimiento en la casa 1, el agente pasa a la casa 2\n")     
                
                if casa.ubicacionestado['C2'] == 1:
                         print("Se detecta movimiento en la casa 2")
                         casa.ubicacionestado['C2'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 2, el agente pasa a la cas 3")
                         print("costo:", costo, "\n")  
                else:
                     print("El agente no detecta movimiento en la casa 2, el agente pasa a la casa 3\n")
                    
                if casa.ubicacionestado['C3'] == 1:
                         print("Se detecta movimiento en la casa 3")
                         casa.ubicacionestado['C3'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 3, el agente pasa a la casa 4")
                         print("costo:", costo, "\n")  
                else:
                     print("El agente no detecta movimiento en la casa 3, el agente pasa a la casa 4\n")
                
                if casa.ubicacionestado['C4'] == 1:
                         print("Se detecta movimiento en la casa 4")
                         casa.ubicacionestado['C4'] == 0
                         costo = costo + 1
                         print("Se activa el aire acondicionado en la casa 4")
                         print("Total de costo:", costo)  
                else:
                     print("El agente no detecta movimiento en la casa 4\n")
                     print("Total de costo:", costo)
            # Si la casa 5 no se detecta nigun movimiento, sigue su recorrido
            else:               
                print("El agente no detecta movimiento en la casa 5, el agente pasa a la casa 6\n")
               
                if casa.ubicacionestado['C6'] == 1:
                    print("Se detecta movimiento en la casa 6")
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
                     print("Se activa el aire acondicionado en la casa 7, el agente pasa a la casa 1")
                     print("costo:", costo, "\n")  

                else:
                      print("El agente no detecta movimiento en la casa 7, el agente pasa a la casa 1\n")
                    
                if casa.ubicacionestado['C1'] == 1:
                    print("Se detecta movimiento en la casa 1")
                    casa.ubicacionestado['C1'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 1, el agente pasa a la casa 2")
                    print("costo:", costo, "\n")  
                else: 
                    print("El agente no detecta movimiento en la casa 1, el agente pasa a la casa 2\n")

                if casa.ubicacionestado['C2'] == 1:
                     print("Se detecta movimiento en la casa 2")
                     casa.ubicacionestado['C2'] == 0
                     costo = costo + 1
                     print("Se activa el aire acondicionado en la casa 2, el agente pasa a la casa 3")
                     print("costo:", costo, "\n")  

                else:
                      print("El agente no detecta movimiento en la casa 2, el agente pasa a la casa 3\n")
                
                if casa.ubicacionestado['C3'] == 1:
                    print("Se detecta movimiento en la casa 3")
                    casa.ubicacionestado['C3'] == 0
                    costo = costo + 1
                    print("Se activa el aire acondicionado en la casa 3, el agente pasa a la casa 4")
                    print("costo:", costo, "\n")  
                else: 
                    print("El agente no detecta movimiento en la casa 3, el agente pasa a la casa 4\n")

                if casa.ubicacionestado['C4'] == 1:
                     print("Se detecta movimiento en la casa 4")
                     casa.ubicacionestado['C4'] == 0
                     costo = costo + 1
                     print("Se activa el aire acondicionado en la casa 4")
                     print("Total de costo:", costo, "\n")  

                else:
                      print("El agente no detecta movimiento en la casa 4\n")
                      print("Total de costo:", costo)


entorno = Casas()
condominios = EntornoCondominios(entorno)