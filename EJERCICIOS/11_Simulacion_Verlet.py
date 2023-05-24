import numpy as np
import matplotlib.pyplot as plt

G = 1
m = 1
'''x_0 = 3.565*10**8
y_0 = 0
vx_0 = 0
vy_0 = 1.035*10**3'''
delta_t = 0.01
pasos = 500

def aceleracion(x, y, eje):
    if eje == "x":
        return -G*m*x/(x**2 + y**2)**1.5
    elif eje == "y":
        return -G*m*y/(x**2 + y**2)**1.5

def paso_euler(r_0, v_0, a_0, delta_t):
    return r_0 + v_0*delta_t + (a_0*delta_t**2)/2

def paso_verlet(r_1, r_0, a_1, delta_t):
    return 2*r_1 - r_0 + (a_1*delta_t**2)

#Condiciones iniciales
x_0, y_0 = 0, 1
vx_0, vy_0 = 0.8, 0
ax_0 = aceleracion(x_0, y_0, "x")
ay_0 = aceleracion(x_0, y_0, "y")

#Paso euler

x_1 = paso_euler(x_0, vx_0, ax_0, delta_t)
y_1 = paso_euler(y_0, vy_0, ay_0, delta_t)
ax_1 = aceleracion(x_1, y_1, "x")
ay_1 = aceleracion(x_1, y_1, "y")

#Paso verlet

x_lista = [x_0, x_1]
y_lista = [y_0, y_1]
t_lista = [0, delta_t]

for i in range(pasos):
    x_2 = paso_verlet(x_1, x_0, ax_1, delta_t)
    y_2 = paso_verlet(y_1, y_0, ay_1, delta_t)  
    x_lista.append(x_2)
    y_lista.append(y_2)
    x_0, x_1 = x_1, x_2
    y_0, y_1 = y_1, y_2
    ax_1 = aceleracion(x_1, y_1, "x")
    ay_1 = aceleracion(x_1, y_1, "y")

plt.figure()
plt.plot(x_lista, y_lista, "--k")
plt.scatter(0, 0, s = 300, c = "g")
plt.show()

