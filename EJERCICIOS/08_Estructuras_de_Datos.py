import numpy as np
import pandas as pd

#Ejercicio 1 ===============>
"""
Crear un solo arreglo numpy con la siguiente informacion 
de los estudiantes que usan el servicio de taxi
                            IDA                             
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES     
JUAN          Si        Si        Si      Si      No        
CAMILA        Si        No        Si      No      Si        
JOSE          Si        No        Si      Si      No        
MARIA         Si        Si        Si      No      No        
ESTEBAN       Si        No        No      Si      Si        
ANGIE         Si        No        Si      No      No        
"""

juan = ["Si", "Si", "Si", "Si", "No"]
camila = ["Si", "No", "Si", "No", "Si"]
jose = ["Si", "No", "Si", "Si", "No"]
maria = ["Si", "Si", "Si", "No", "No"]
esteban = ["Si", "No", "No", "Si", "Si"]
angie = ["Si", "No", "Si", "No", "No"]

arreglo = np.array([juan, camila, jose, maria, esteban, angie])
print(arreglo)
#Ejercicio 2 ===============>

"""
Crear una serie con informacion del rendimiento de los empleados en una empresa =>
--------------  Emplea_1  Emplea_2  Emplea_3  Emplea_4  Emplea_5  Emplea_6  Emplea_7  Emplea_8  Emplea_9  Emplea_10  Emplea_11  Emplea_12  Emplea_13  Emplea_14  Emplea_15  Emplea_16  Emplea_17  Emplea_18  Emplea_19  Emplea_20  Emplea_21  Emplea_22  Emplea_23  Emplea_24  Emplea_25  Emplea_26  Emplea_27 
Rendimiento --    "C"       "B"      "B"        "B"        "C"      "B"      "A"        "C"       "B"        "A"        "C"       "B"        "B"        "B"         "B"        "A"       "B"        "A"         "A"        "C"       "B"        "B"        "B"         "B"         "C"       "A"       "C"   """

empleados = ["Emplea_1", "Emplea_2", "Emplea_3", "Emplea_4", "Emplea_5", "Emplea_6", "Emplea_7", "Emplea_8", "Emplea_9", "Emplea_10",  "Emplea_11",  "Emplea_12",  "Emplea_13",  "Emplea_14",  "Emplea_15",  "Emplea_16",  "Emplea_17",  "Emplea_18",  "Emplea_19",  "Emplea_20",  "Emplea_21",  "Emplea_22",  "Emplea_23",  "Emplea_24",  "Emplea_25",  "Emplea_26",  "Emplea_27"]
rendimiento = ["C", "B", "B", "B", "C", "B", "A", "C", "B", "A", "C", "B", "B", "B", "B", "A", "B", "A", "A", "C", "B", "B", "B", "B", "C", "A", "C"]
serie = pd.Series(rendimiento, empleados)
print(serie)
#Ejercicio 3 ===============>
"""
Crear un data frame con los empleados de una empresa:
Cod   Nombre               Cargo          Salario   
0001   Cristian Pachon     Ingeniero      $ 3.200.000
0002   Daniela Pineda      Programador    $ 4.300.000
0003   Esteban Murcia      Programador    $ 4.600.000
0004   Jose Guzman         Ingeniero      $ 3.900.000
0005   Camilo Rodriguez    Ensamblador    $ 1.200.000
0006   Mariana Londoño     Ensamblador    $ 1.100.000
0007   Estefania Muños     Ensamblador    $ 1.700.000
0008   Cristian Rodriguez  Ingeniero      $ 3.100.000
0009   Natalia Alzate      Ensamblador    $ 2.200.000
0010   Juan Sanabria       Diseñador      $ 5.100.000
0011   Juanita Calderon    Ensamblador    $ 1.300.000
0012   Laura Quintero      Administrador  $ 2.500.000
0013   Viviana Quesada     Guardia        $ 1.500.000
"""

filas = ["0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009", "0010", "0011", "0012", "0013"]
columnas = ["Nombre", "Cargo", "Salario"]
datos = [["Cristian Pachon",  "Ingeniero", 3200000],
         ["Daniela Pineda",  "Programador", 4300000],
         ["Esteban Murcia",  "Programador", 4600000],
         ["Jose Guzman",  "Ingeniero", 3900000],
         ["Camilo Rodriguez",  "Ensamblador", 1200000],
         ["Mariana Londoño",  "Ensamblador", 1100000],
         ["Estefania Muños",  "Ensamblador", 1700000],
         ["Cristian Rodriguez",  "Ingeniero", 3100000],
         ["Natalia Alzate",  "Ensamblador", 2200000],
         ["Juan Sanabria",  "Diseñador", 5100000],
         ["Juanita Calderon",  "Ensamblador", 1300000],
         ["Laura Quintero",  "Administrador", 2500000],
         ["Viviana Quesada",  "Guardia", 1500000]]

dataframe = pd.DataFrame(datos, filas, columnas)
print(dataframe)
print(dataframe["Salario"].mean())


#Ejercicio: Revisar que metodos y atributos tienen los arreglos, las series y los dataframes.