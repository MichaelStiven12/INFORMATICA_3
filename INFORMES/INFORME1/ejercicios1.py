nombre_completo = "Michael Stiven Valencia Mora"

#Ejercicio 1

def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False

def sumadeDigitos(numero):
    cadena = str(numero)
    suma = []
    for letra in cadena:
        suma.append(int(letra))
    return sum(suma)

def tieneVocales(mensaje):
    for caracter in mensaje:
        if caracter in ["a","e","i","o","u"]:
            return True
        else:
            pass
    return False
        
def esPrimo(numero):
    divisores = []
    for i in range(1,numero + 1):
        if numero%i == 0:
            divisores.append(i)
    if len(divisores) == 2:
        return True
    else:
        return False

funciones = [esMayorDeEdad, sumadeDigitos, tieneVocales, esPrimo]


#Ejercicio 2

uso = {
        "Mariana": [["Si", "No", "Si", "No", "No"], ["No", "No", "Si", "No", "No"]],        
        "Sofia": [["Si", "No", "No", "Si", "Si"], ["Si", "No", "No", "Si", "No"]],        
        "Camila": [["Si", "No", "Si", "No", "Si"], ["No", "No", "No", "No", "No"]],        
        "Maria": [["Si", "Si", "Si", "No", "No"], ["No", "No", "Si", "No", "No"]],        
        "Juan": [["Si", "Si", "Si", "Si", "No"], ["Si", "No", "Si", "No", "No"]],        
        "Angie": [["Si", "No", "Si", "No", "No"], ["Si", "No", "Si", "No", "No"]],        
        "Esteban": [["Si", "No", "No", "Si", "Si"], ["No", "No", "No", "Si", "No"]],        
        "Jose": [["Si", "No", "Si", "Si", "No"], ["Si", "No", "Si", "Si", "No"]],        
        "Gisell": [["Si", "Si", "No", "Si", "No"], ["Si", "No", "Si", "No", "No"]],        
        "Cristian": [["Si", "Si", "Si", "No", "No"], ["Si", "Si", "Si", "No", "No"]]        
}
diccionarioPagos = {
                    "Mariana": 0,
                    "Sofia": 0,
                    "Camila": 0,
                    "Maria": 0,
                    "Juan": 0,
                    "Angie": 0,
                    "Esteban": 0,
                    "Jose": 0,
                    "Gisell": 0,
                    "Cristian": 0
}

fue = []
for j in range(0,2):
    for i in range(0,5):
        fue.append([])
        for estudiante in uso.keys():
            if uso[estudiante][j][i] == "Si":
                fue[len(fue) - 1].append("Si")
            else:
                fue[len(fue) - 1].append("No")

for elemento in fue:
    for i in range(0,10):
        if elemento[i] == "Si":
            diccionarioPagos[list(uso.keys())[i]] += 15000/elemento.count("Si")
        if elemento.count("Si") == 0:
                diccionarioPagos[list(uso.keys())[i]] += 1000

for estudiante in diccionarioPagos.keys():
    diccionarioPagos[estudiante] = round(diccionarioPagos[estudiante],2)

#Ejercicio 3

precios = {          
            "Pantalon": [38000, 0.03],
            "Zapatos": [55500, 0.05],
            "Tenis": [71000, 0.04],  
            "Camisa": [29500, 0.02],
            "Corbata": [25000, 0.07],
            "Blusas": [80500, 0.05],
            "Vestidos": [95000, 0.02]
}

ventas = {
            "001": [40, 20, 22, 30, 2, 20, 3],   
            "002": [13, 31, 14, 32, 15, 20, 11],   
            "010": [12, 24, 32, 40, 9, 50, 13],   
            "020": [22, 42, 12, 33, 24, 32, 23],   
            "021": [19, 51, 21, 25, 10, 14, 2],   
            "022": [35, 22, 31, 51, 21, 15, 11],   
            "023": [39, 21, 36, 22, 32, 32, 15],   
            "024": [43, 22, 33, 41, 21, 31, 36],   
            "025": [33, 33, 31, 20, 42, 42, 35],   
            "031": [37, 22, 47, 5, 28, 31, 32],   
            "032": [41, 24, 38, 33, 21, 31, 16],   
            "033": [39, 21, 18, 32, 37, 22, 12],   
            "041": [33, 33, 31, 21, 21, 39, 25],   
            "042": [15, 25, 39, 20, 48, 30, 32],   
            "043": [37, 27, 32, 29, 28, 35, 16],   
            "121": [39, 24, 12, 31, 21, 32, 13],   
            "122": [13, 31, 31, 50, 22, 30, 21],   
            "123": [31, 23, 35, 35, 39, 19, 19],   
            "351": [35, 26, 36, 39, 27, 32, 16],   
            "352": [25, 25, 31, 21, 21, 37, 15],   
            "353": [37, 23, 34, 35, 32, 20, 49],   
            "368": [25, 31, 14, 29, 39, 37, 16],   
            "369": [37, 26, 31, 31, 27, 32, 41],   
            "461": [21, 40, 42, 23, 11, 15, 19],   
            "466": [31, 27, 31, 39, 21, 32, 25],   
            "469": [35, 38, 32, 19, 29, 50, 16]
} 

salarios = []
salarios_netos = []
for empleado in ventas.keys():
    salarios.append([])
    for i in range(0, len(list(precios.keys()))):    
        salarios[len(salarios) - 1].append(ventas[empleado][i]*precios[list(precios.keys())[i]][0]*precios[list(precios.keys())[i]][1])

for salario in salarios:
    salarios_netos.append(sum(salario) + 1200000)


salarios_ord = salarios_netos.copy()
salarios_ord.sort()
codigo1 = list(ventas.keys())[salarios_netos.index(salarios_ord[-1])]
codigo2 = list(ventas.keys())[salarios_netos.index(salarios_ord[-2])]
codigo3 = list(ventas.keys())[salarios_netos.index(salarios_ord[-3])]

codigosAltosSalarios = [codigo1, codigo2, codigo3]


#Ejercicio 4

puntos = [[5, 2, 3], [4, 1, 3], [2.5, 1, 0], [0.5, 0.5, 2], [1, 2, 1], [6, 2, 1], [3, 2, 0.5], [2, 6, 1], [0, 0, 0], [2, 0, 0.5],
          [2, 2, 3], [2, 3, 4], [1, 1, 3], [4, 4, 4], [5, 5, 1], [1, 0.5, 1], [3, 4, 5], [3, 1, 2], [3, 9, 1], [0.5, 0.5, 6]]
distancias = []
puntos1 = []
for i in range(0, len(puntos)):
    for j in range(i + 1, len(puntos)):
        distancias.append(((puntos[i][0] - puntos[j][0])**2 + (puntos[i][1] - puntos[j][1])**2 + (puntos[i][2] - puntos[j][2])**2)**0.5)
        puntos1.append([i + 1, j + 1])

punto_cercano = min(distancias)

parCercano = f"P{puntos1[distancias.index(punto_cercano)][0]}-P{puntos1[distancias.index(punto_cercano)][1]}"


#Ejercicio 5

registros = ["P009-21Unidades", "B005-19Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades", "A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades" ]

def ventasEmpresa(registros):
    precios = {
            "A001": 31000,
            "A011": 25000,
            "A032": 43000,
            "A125": 55000,
            "B001": 10000,
            "B005": 20000,
            "P009": 30000,
            "P019": 49000,
            "R001": 60000,
            "W307": 90000,
            "Z052": 35000,
            "Z025": 27000,
            "Z278": 65000
    }
    dinero_total = 0
    for venta in registros:
        dinero_total += precios[venta[0:4]]*int(venta[5:7])
    return dinero_total