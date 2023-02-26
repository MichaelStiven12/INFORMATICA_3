'''1) Imprimir en la terminal dos enteros, dos flotantes, dos strings, dos booleanos, dos listas, dos tuplas, un diccionario y un conjunt,
todo en una misma linea'''

e1 = 3
e2 = 4
f1 = 5.3
f2 = 56.4
s1 = "Michael"
s2 = "Valencia"
b1 = True
b2 = False
l1 = [1,2,3]
l2 = ["a", "b", "c"]
t1 = (1,2,3)
t2 = ("a", "b", "c")
d = {"nombre": "Michael", "apellido": "Valencia"}
c = {"A", "B", "C"}

print(e1, e2)
print(f1, f2)
print(s1, s2)
print(b1, b2)
print(l1, l2)
print(t1, t2)
print(d)
print(c)


"2) Resolver con los operadores que considere conveniente"

""" Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
Realice un codigo que determine la distancia entre ambos puntos """

p1 = [5, 4, 5]
p2 = [0, 10, 9]
d = []
for i in range(0,3):
    d.append(p2[i] - p1[i])
print((d[0]**2 + d[1]**2 + d[2]**2)**0.5)


""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """

notas = [3.5, 5.0, 4.0]
notaNecesaria = round((3 - (notas[0]*0.15 + notas[1]*0.25 + notas[2]*0.2))/0.4,2)
print(notaNecesaria)

""" Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran? """

for i in range(1,101):
    a1 = (3*(i + 10)**2)/2
    a2 = (5*(i)**2)/2
    print(a1, a2)
    if(a2 >= a1):
        print("El segundo auto rebaso al primero en ", i, " segundos")
        break

""" Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
prestará solo de ida.
Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        No        Si    No
CAMILA        Si        Si        No        No    No
JOSE          Si        No        Si        No    No
MARIA         Si        Si        Si        No    No      
¿Cuanto debe pagar cada estudiante? """

diccionario = {"JUAN": [True, True, False, True, False], 
               "CAMILA": [True, True, False, False, False], 
               "JOSE": [True, False, True, False, False], 
               "MARIA": [True, True, True, False, False]}


for valor in diccionario.values():
    costo = 0
    for i  in range(5):
        if valor[i] == True:
            costo += 15000
        if (diccionario["JUAN"][i] == False) and (diccionario["CAMILA"][i] == False) and (diccionario["JOSE"][i] == False) and (diccionario["MARIA"][i] == False):
            costo += 10000
    print(list(diccionario.keys())[list(diccionario.values()).index(valor)] + " debe pagar: " + str(costo))

