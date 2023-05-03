import matplotlib.pyplot as plt
import pandas
import numpy as np

columnas = ["Nombre","Cargo","Salario", "Años_experiencia"]
indices = ["0001","0002","0003","0004","0005","0006","0007","0008","0009","0010","0011","0012","0013"]
datos =  [["Cristian Pachon"     ,"Ingeniero"      ,3200000, 8],
          ["Daniela Pineda"      ,"Programador"    ,4300000, 9],
          ["Esteban Murcia"      ,"Programador"    ,4600000, 10],
          ["Jose Guzman"         ,"Ingeniero"      ,3900000, 8],
          ["Camilo Rodriguez"    ,"Ensamblador"    ,1200000, 2],
          ["Mariana Londoño"     ,"Ensamblador"    ,1100000, 1],
          ["Estefania Muños"     ,"Ensamblador"    ,1700000, 5],
          ["Cristian Rodriguez"  ,"Ingeniero"      ,3100000, 8],
          ["Natalia Alzate"      ,"Ensamblador"    ,2200000, 6],
          ["Juan Sanabria"       ,"Diseñador"      ,5100000, 11],
          ["Juanita Calderon"    ,"Ensamblador"    ,1300000, 4],
          ["Laura Quintero"      ,"Administrador"  ,2500000, 7],
          ["Viviana Quesada"     ,"Guardia"        ,1500000, 3]]


dataFrameEmpresa = pandas.DataFrame(index=indices,
                                    columns=columnas,
                                    data=datos
                                    )

print(dataFrameEmpresa)

'''
Graficar la dispersion  => Años experiencia vs Salario
Graficar el histograma => Salario
Graficar el histograma => Años experiencia
Graficar el diagrama de barras => cargo vs Salario promedio'''

plt.figure()
plt.plot(dataFrameEmpresa["Años_experiencia"].values, dataFrameEmpresa["Salario"].values, "or", label = "Dispersión")
plt.grid()
plt.title(r"$Años\ de\ experiencia\ vs\ Salario$")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario")
plt.legend()
plt.show()

plt.figure()
plt.hist(dataFrameEmpresa["Salario"].values, bins = 5, density = True)
plt.title(r"$Histograma\ de\ salarios$")
plt.xlabel("Salario")
plt.ylabel("Frecuencia")
plt.show()

plt.figure()
plt.hist(dataFrameEmpresa["Años_experiencia"].values, bins = 5, color = "#a65",density = True)
plt.title(r"$Histograma\ de\ años\ de\ experiencia$")
plt.xlabel("Años de experiencia")
plt.ylabel("Frecuencia")
plt.show()

plt.figure()
plt.bar(dataFrameEmpresa[["Cargo", "Salario"]].groupby(["Cargo"]).mean().index, dataFrameEmpresa[["Cargo", "Salario"]].groupby(["Cargo"]).mean()["Salario"], color = "#d54", edgecolor = "#0f3")
plt.show()
