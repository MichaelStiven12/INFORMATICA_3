#Metodos de cadenas
'''
cadena = "hola"

print(dir(cadena))
print(cadena.upper())
print(cadena.lower())
print(cadena.center(50, "-"))
print(cadena.strip("       hola  "))

cadena1 = "Michael Stiven Valencia Mora"

print(cadena1.count("i"))
print(cadena1.replace("Michael", "Maicol"))
print(cadena1.find("a"))

print(cadena1[4])
print(cadena1[2:7:2])

#Metodos de las listas

lista = [1,2,3,4]
print(dir(lista))

#Metodos de las tuplas

tupla = (10, 20, 30)
print(dir(tupla))

#Metodos de los diccionarios

diccionario = {1: "uno", 2: "dos", 3: "tres"}
print(dir(diccionario))
'''
#==> EJERCICIO 1
"A continuación se encuentra el poema el salmon"

"""
TÍTULO: EL SALMÓN
PÁRRAFO 1: DETRÁS DE UN SALMÓN, NADA UN TIBURÓN, LO CAZA EN ALASKA, CANSADOS LOS DOS. 
PÁRRAFO 2: ASUSTADO GRITA: ¡NOOO! POR FAVOR,MI VIDA ES MUY CORTA, ¡MUESTRA COMPASIÓN!.
PÁRRAFO 3: ABRIENDO SU BOCA, LO DEJA ESCAPAR, Y CORRIENTE ARRIBA, LO HA VISTO NADAR.
"""

"""a) Corrija el poema de tal manera que:
      Los indicadores de título y párrafo desaparezcan
      Corregir el uso de mayúsculas y minúsculas según las reglas gramaticales.
      El titulo esté en formato de título.
      Separar los cuatro versos de cada párrafo en renglones sucesivos
      Generar un espacio de renglon entre titulo-parrafo y párrafo-parrafo
      El título debe estar centrado.   
   b) Contar el número de veces que aparece cada vocal
      contar el numero de lineas del poema.
      Reemplazar las palabras: salmón ==> tiburón
                               tiburón ==> salmón
   c) Verificar si el contenido del poemas es: alfabetico
                                               alfanumerico
                                               decimal
                                               digitos
   d) Utilizar la indexación para extraer los elementos ubicados
      en los índices: 0, 10, 100, último índices
   e) Utilizar slicing para extraer los elementos ubicados en:
      - Indices pares.
      - Indices impares.
      - Cada quinto elemento, empezando desde el 20
      - Cada tercer elemento, pero empezando desde el indice 4 y terminando en el 62
      - Desde la mitad hacia adelante
      - Todos pero al revés
      - Cada segundo elemento, pero al revés"""
'''
poema = """TÍTULO: EL SALMÓN
PÁRRAFO 1: DETRÁS DE UN SALMÓN, NADA UN TIBURÓN, LO CAZA EN ALASKA, CANSADOS LOS DOS. 
PÁRRAFO 2: ASUSTADO GRITA: ¡NOOO! POR FAVOR, MI VIDA ES MUY CORTA, ¡MUESTRA COMPASIÓN!.
PÁRRAFO 3: ABRIENDO SU BOCA, LO DEJA ESCAPAR, Y CORRIENTE ARRIBA, LO HA VISTO NADAR.
"""

poema = poema.replace("TÍTULO: ", "")
poema = poema.replace("PÁRRAFO 1: ", "")
poema = poema.replace("PÁRRAFO 2: ", "")
poema = poema.replace("PÁRRAFO 3: ", "")

poema = poema.lower()
poema = poema.capitalize()

poema = poema.replace(", ", ",\n")
poema = poema.replace(".", ".\n")
poema = poema.replace("detrás", "Detrás")
poema = poema.replace("asustado", "Asustado")
poema = poema.replace("abriendo", "Abriendo")
poema = poema.replace("El salmón", "El Salmón\n")
poema = poema[0:9].center(50, " ") + "\n" + poema[9:len(poema)]
a = poema.count("a")
e = poema.count("e")
i = poema.count("i")
o = poema.count("o")
u = poema.count("u")
lineas = poema.count("\n")
poema = poema.replace("salmón", "tiburón")
poema = poema.replace("tiburón", "salmón")
print("Poema: " + poema)
print("Cantidad de a: " + str(a))
print("Cantidad de e: " + str(e))
print("Cantidad de i: " + str(i))
print("Cantidad de o: " + str(o))
print("Cantidad de u: " + str(u))
print("Numero de lineas: " + str(lineas))
print("Alfabetico: " + str(poema.isalpha()))
print("Alfanumerico: " + str(poema.isalnum()))
print("Digitos: " + str(poema.isdigit()))
print("Decimal: " + str(poema.isdecimal()))
print("Indice 0: " + poema[0])
print("Indice 10: " + poema[10])
print("Indice 100:" + poema[100])
print("Ultimo indice: " + poema[-1])
print("Indices pares:" + poema[0::2])
print("Indices impares: " + poema[1::2])
print("Desde el 20: " + poema[20::5])
print("Desde el 4: " + poema[4:63:3])
print("Desde la mitad: " + poema[len(poema)//2:])
print("Hacia atras: " + poema[len(poema) - 1:0:-1])
print("Hacia atras de a dos: " + poema[len(poema) - 1:0:-2])

'''
'''
#====================== EJERCICIOS MÉTODOS DE LISTAS ====================

#==> EJERCICIO 1

""" Realice las siguientes operaciones sobre listas:
        * ["A","B","C"] Elimine el último elemento de la lista
                        Luego agregue su nombre al final de la lista                  
        * [100,200,300] Elimine el segundo elemento de la lista,
                        Luego agregue su edad como segundo elemento de la lista
        * [1,2,3,4]     Elimine el último elemento de la lista
                        Luego agrege los valores 100, 200, 300 al final de la lista
                        Elimine el segundo elemento de la lista
                        Luego inserte el valor -1 en la segunda posición de la lista
        * Contruya una sola lista con los elementos resultantes de las 3 listas anteriores."""

#==> EJERCICIO 2
lista1 = ["A", "B", "C"]
lista1.pop(-1)
lista1.append("Michael Stiven Valencia Mora")
print(lista1)

lista2 = [100, 200, 300]
lista2.pop(1)
lista2.insert(1, 22)
print(lista2)

lista3 = [1, 2, 3, 4]
lista3.pop(-1)
for i in [100, 200, 300]:
    lista3.append(i)
lista3.insert(1, -1)
print(lista3)

lista4 =[]
for i in [lista1, lista2, lista3]:
    for j in i:
      lista4.append(j)

print(lista4)

""" Determine si el numero 25 está en la lista edades,
    y si es así cuantas veces aparece.
    edades = [0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] """

edades = [0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(edades.count(25))

#==> EJERCICIO 3
""" Teniendo en cuenta la lista anterior, ordene de forma ascendente,luego descendente a los elementos.
    Pero sin alterar la lista edades original. """

lista5 = edades.copy()
lista5.sort()
lista6 = lista5.copy()
lista6.reverse()
print(lista5)
print(lista6)

#==> EJERCICIO 4
""" Cree una copia de edades y haga lo siguiente:
   * Muestre en pantalla el elemento inicial y el final
   * Remueva aquellos elementos cuyo valor es 0 o 1"""

lista7 = edades.copy()
lista8 = []
for i in lista7:
   if(i == 0 or i == 1):
      pass
   else:
      lista8.append(i)
print(lista8)
 
#==> EJERCICIO 5
"""  Utilice slicing para extraer a partir de la lista edades:
         - Elementos ubicados en indices pares
         - Elementos ubicados en indices impares
         - Todos los elementos, pero al revés de la lista
         - Cada 70avo elemento a partir del 10
         - Cada 100avo elemento, pero al revés de la lista
         - Cada 35avo elemento, a partir de la mitad
  ¿Qué operaciones puedo hacer con listas que no puede hacer con tuplas? """

print(edades[::2])
print(edades[1::2])
print(edades[-1:0:-1])
print(edades[10::70])
print(edades[-1:0:-100])
print(edades[int(len(edades)/2)::35])


diccionario = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco"
}

print(diccionario.keys())
print(diccionario.values())
print(diccionario.get(2))
diccionario.pop(1)
'''

#EJERCICIOS DE DICCIONARIOS   

#==> EJERCICIO 1
""" Cree el siguiente diccionario =>
    Calificaciones = {"Juan": 5.0, "David": 2.4, "Maria": 2.9, "Esteban": 2.2, "Daniela": 2.0, "Mario": 3.1, "Juanita": 2.1, "José": 3.0, "Sebastian": 2.3, "Cristian": 2.0, "Alberto": 3.9, "Angélica": 4.2, "Angel": 2.0, "Marly": 2.5, "Mariana": 4.5, "Josefina": 2.7}
     
       a) Extraiga los keys y values del diccionario, almacenelos en las variables claves, valores, respectivamente
       b) Corrija en el diccionario las calificaciones de Marly (4.3), Angel (3.1) y Juanita (3.5)
       c) Elimine a les estudiantes Josefina y Juan.
       d) Cree una copia y llamela reprobados, elimine todos aquellos con calificación mayor o igual a 3
       e) Muestre en pantalla la mejor calificación, para ello utilice indexing
       f) Muestre en pantalla la peor calificación, para ello utilice indexing 
       g) Utilice indexing para agregar dos nuevos estudiantes: Marco(3.0) Alejandra(5.0)"""

calificaciones = {"Juan": 5.0, "David": 2.4, "Maria": 2.9, "Esteban": 2.2, "Daniela": 2.0, "Mario": 3.1, "Juanita": 2.1, "José": 3.0, "Sebastian": 2.3, "Cristian": 2.0, "Alberto": 3.9, "Angélica": 4.2, "Angel": 2.0, "Marly": 2.5, "Mariana": 4.5, "Josefina": 2.7}

claves = calificaciones.keys()
valores  = calificaciones.values()

calificaciones["Marly"] = 4.3
calificaciones["Angel"] = 3.1
calificaciones["Juanita"] = 3.5

calificaciones.pop("Josefina")
calificaciones.pop("Juan")

reprobados = calificaciones.copy()

for i in claves:
   if reprobados[i] >= 3:
      reprobados.pop(i)

maxima = max(valores)
print("La nota maxima es: " + str(list(valores)[list(valores).index(maxima)]))

minima = min(valores)
print("La nota minima es: " + str(list(valores)[list(valores).index(minima)]))

calificaciones["Marco"] = 3.0
calificaciones["Alejandra"] = 5.0

print(calificaciones)
print(reprobados)
print(maxima)
print(minima)

#==> EJERCICIO 2
""" Utilizando diccionarios cree una base de datos de empleados de una empresa,
la base de datos se debe llamar empleadosMabe. Debe contener la siguiente información
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
A partir de la base de datos, busque una manera de:
    a) Encontrar la persona con mayor salario
    b) Encontrar la persona con menor salario
    c) Calcular el gasto total de la empresa por motivo salarios
    d) Calcular el promedio de lo que ganan los programadores
    e) Calcular el promedio de lo que ganan los ensambladores"""


empleadosMabe = {
                  "0001": ["Cristian Pachon",  "Ingeniero", 3200000],
                  "0002": ["Daniela Pineda",  "Programador", 4300000],
                  "0003": ["Esteban Murcia",  "Programador", 4600000],
                  "0004": ["Jose Guzman",  "Ingeniero", 3900000],
                  "0005": ["Camilo Rodriguez",  "Ensamblador", 1200000],
                  "0006": ["Mariana Londoño",  "Ensamblador", 1100000],
                  "0007": ["Estefania Muños",  "Ensamblador", 1700000],
                  "0008": ["Cristian Rodriguez",  "Ingeniero", 3100000],
                  "0009": ["Natalia Alzate",  "Ensamblador", 2200000],
                  "0010": ["Juan Sanabria",  "Diseñador", 5100000],
                  "0011": ["Juanita Calderon",  "Ensamblador", 1300000],
                  "0012": ["Laura Quintero",  "Administrador", 2500000],               
                  "0013": ["Viviana Quesada",  "Guardia", 1500000]                
}

datos = empleadosMabe.values()
salarios = []

for i in datos:
   salarios.append(i[2])

salario_maximo = max(salarios)


