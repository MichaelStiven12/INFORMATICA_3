"""
Este archivo es el archivo principal que integra todos los archivos
Aqui se encuentra  la funcion simulacion()
la cual integra todas las funciones para operarlas
esta funcion recibe un voltaje
y retorna la corriente producida por la celda (j_cell)
"""

from PropiedadesMaterialN import *
from PropiedadesMaterialP import *
from Funciones import *
from ConstantesFisicas import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def simulation(voltage):        #this function return j_cell of the solar cell
    # Built-in potential --------------------------------------------------------------
    V_bi = Vbi(Eg_n, Eg_p, chi_n, chi_p, N_d, N_a, Nc_n, Nc_p, Nv_n, Nv_p, ni_n, ni_p)

    # Depletion region ----------------------------------------------------------------
    x_n = region(N_a, N_d, eps_n, eps_p, N_d, N_a, V_bi, voltage )
    x_p = region(N_d, N_a, eps_n, eps_p, N_d, N_a, V_bi, voltage )

    if x_n > w_n:  # Condition in case the depletion region exceeds the width of the material
        x_n = w_n
        x_p = w_n * (N_d / N_a)

    # Photocurrent --------------------------------------------------------------------
    dj_p    =  dJp(s_p, L_p, D_p, w_n, x_n, alpha_1, Ref, Trans)
    dj_n    =  dJn(s_n, L_n, D_n, w_p, x_p, alpha_2, w_n, alpha_1, Ref, Trans)  
    dj_scr  =  dJscr(x_n, x_p, w_n, alpha_1, alpha_2 , Ref, Trans)
    j_ph    =  Jph(dj_n, dj_p, dj_scr)
    # Saturation current density J0 ---------------------------------------------------
    j0_p    =  J0pn(D_p, p_0, L_p, s_p, w_n, x_n)
    j0_n    =  J0pn(D_n, n_0, L_n, s_n, w_p, x_p)
    j_0     =  J0(j0_n, j0_p)
    # Saturation current density J00 --------------------------------------------------
    j_00    =  J00(x_n, x_p, ni_n, ni_p, L_p, L_n, D_p, D_n)
    # Dark current density ------------------------------------------------------------
    j_dark  =  Jdark(j_0, j_00, voltage)
    # Cell current density ------------------------------------------------------------
    j_cell  =  j_ph - j_dark
    return j_cell

# ========================Mi primera celda simulada========================
#voltage = 0.5  #Voltios
#j_celda = simulation(voltage)   #densidad de corriente que produce celda
#pot_celda = voltage * j_celda   #densidad de potencia electrica producida por la celda

# =======================Simulacion variando el voltaje====================

voltage = np.arange(0, 1, 0.01)
jcell = np.zeros(shape = 100)

for valor in range(len(voltage)):
    jcell[valor] = simulation(voltage[valor])

potencia = jcell*voltage

maxima_p = max(potencia)
v_mpp = voltage[list(potencia).index(maxima_p)]
j_mpp = jcell[list(voltage).index(v_mpp)]
p_mpp = j_mpp*v_mpp

corte = np.where(np.diff(np.sign(jcell)))[0]
v_0c = voltage[corte][0]
j_sc = jcell[0]
ff = p_mpp/(j_sc*v_0c)
n = p_mpp/P_inc
print(j_sc)
print("Potencia maxima de la celda: ", p_mpp)
print("Factor de llenado de la celda", ff)
print("Eficiencia de la celda:", n)

plt.figure()
plt.plot(voltage, jcell, color = "blue")
plt.title("Gráfica caracteristica de la celda solar")
plt.ylabel("J [A/cm^2]")
plt.xlabel("V [Voltios]")
plt.legend(["Densidad de corriente"], loc = "upper left")
plt.xlim(0, 0.7)
plt.ylim(0, 0.05)
plt.yticks([0.00, 0.01, 0.02, 0.03, j_mpp, j_sc, 0.05], ["0.00", "0.01", "0.02", "0.03", "j_mpp", "j_sc", "0.05"])
plt.xticks([0.0, 0.1, 0.2, 0.3, v_mpp, 0.5, 0.536, 0.6, 0.7],["0.0", "0.1", "0.2", "0.3", "v_mpp", "0.5", "v_0c", "0.6", "0.7"])
plt.plot([0, v_mpp], [j_mpp, j_mpp], color = "black", linestyle = "dashed")
plt.plot([v_mpp, v_mpp], [0, j_mpp], color = "black", linestyle = "dashed")
plt.plot([v_mpp], [j_mpp], color = "black", marker = "o")
otro_y = plt.twinx()
otro_y.plot(voltage, potencia, color = "red")
otro_y.set_ylabel("P [W/cm^2]")
otro_y.set_xlim(0, 0.7)
otro_y.set_ylim(0, 0.02)
otro_y.set_yticks([0.0000, 0.0025, 0.0050, 0.0075, 0.0100, 0.0125, 0.0150, maxima_p, 0.0175, 0.0200], ["0.0000", "0.0025", "0.0050", "0.0075", "0.0100", "0.0125", "0.0150", "P_max", "0.0175", "0.0200"])
otro_y.plot([v_mpp, 0.7], [maxima_p, maxima_p], color = "black", linestyle = "dashed")
otro_y.plot([v_mpp], [maxima_p], color = "black", marker = "o")
otro_y.legend(["Potencia"])
plt.show()
