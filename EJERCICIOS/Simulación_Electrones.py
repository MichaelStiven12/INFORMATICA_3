import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from copy import deepcopy
k = 1
r = 1
T = 0.01
q = 1
e_out = 50
e_in = 100

def crear_Estado_Inicial():
    angulo = 6.28/e_out
    x_out = [r*np.cos(ang) for ang in np.arange(0, 6.28, angulo)]
    y_out = [r*np.sin(ang) for ang in np.arange(0, 6.28, angulo)]
    x_in = [np.random.random()*3 - 1.5 for i in range(e_in)]
    y_in = [np.random.random()*3 - 1.5 for i in range(e_in)]
    return x_out,y_out,x_in,y_in

def dibujar_sistema(x_out,y_out,x_in,y_in):
    plt.figure()
    plt.plot(x_out,y_out, "ro")
    plt.plot(x_in, y_in, "bo")
    plt.gca().set_aspect("equal")
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.grid()
    plt.show()

x_out,y_out, x_in,y_in = crear_Estado_Inicial()
dibujar_sistema(x_out,y_out,x_in,y_in)

r=[]
for i in range(len(x_out)):
    r.append([x_out[i], y_out[i]])

for i in range(len(x_in)):
    r.append([x_in[i], y_in[i]])

r_out = r[:e_out]
r_in = r[e_out:]

def distancia(r1, r2):
    return ((r1[0]-r2[0])**2 + (r1[1]-r2[1])**2)**0.5

def calcular_energia_total():
    sumEnergias = 0
    combinaciones = list(combinations(r, 2))
    for r_ in combinaciones:
        r1, r2 = r_[0], r_[1]
        sumEnergias += k*q*q/distancia(r1,r2)
    return sumEnergias

def metropolis():
    posicion = np.random.choice(range(len(r_in)))
    old_r = r_in[posicion]
    old_E = calcular_energia_total()
    new_r = [np.random.random()*3 - 1.5, np.random.random()*3 - 1.5]
    r_in[posicion] = new_r
    r[posicion + len(r_out)] = new_r
    new_E = calcular_energia_total()
    deltaE = new_E - old_E
    if deltaE <= 0:
        pass
    else:
        r_in[posicion] = old_r
        r[posicion + len(r_out)] = old_r
    
def monte_carlo_step():
    for i in range(len(r_in)):
        metropolis()
print(calcular_energia_total())
amount_mcs = 1000
energies = np.zeros(shape = amount_mcs)
for i in range(amount_mcs):
    monte_carlo_step()


newx_in = []
newy_in = []
for punto in r_in:
    newx_in.append(punto[0])
    newy_in.append(punto[1])

dibujar_sistema(x_out, y_out, newx_in, newy_in)
print(calcular_energia_total())