#EJEMPLO: Crear una funcion que determine si un numero es par o impar.

def esUnNumeroPar(numero):
    if(numero%2 == 0):
        return "El numero es par"
    else:
        return "El numero es impar"   


lista = [[1,2,3],
         [1,2,3],
         [1,2,3],
         [10,20,30]]



#Crear una funcion que reciba como parametro de entrada una lista de listas (numeros) y retorne una lista con la suma de las filas.

def sumaFilas(lista):
    listaSuma = []
    for elemento in lista:
        listaSuma.append(sum(elemento))
    return listaSuma

print(sumaFilas(lista))
#Crear una funcion que reciba como parametro de entrada una lista de listas (numeros) y retorne una lista con la suma de las columnas.

def sumaColumnas(lista):
    listaSumaCol = []
    sumaCol = []
    for i in range(0,len(lista[0])):
       listaSumaCol.append([])
       for elemento in lista:
            listaSumaCol[len(listaSumaCol) - 1].append(elemento[i])
    for elemento in listaSumaCol:
        sumaCol.append(sum(elemento))
    return sumaCol

print(sumaColumnas(lista))