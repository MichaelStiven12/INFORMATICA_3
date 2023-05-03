import numpy
from collections import defaultdict
from matplotlib import pyplot
import itertools

length = 10
j = 1.0
kB = 1.0

#Contenedores
sites = list() #Contenedor de posiciones
spins = dict() #Contenedor de spins
nbhs = defaultdict(list) #Contenedor de vecinos

#Creación de la muestra
for x, y in itertools.product(range(length), range(length)): #Consultar que hace el metodo product.
    sites.append((x,y))


#Creación del estado aleatorio
def random_configuration():
    for spin in sites:
        spins[spin] = numpy.random.choice([-1, 1])

random_configuration()

#Visualizar los spins
def plot_spins():
    pyplot.figure()
    colors = {1: "red", -1: "blue"}
    for site, spin in spins.items():
        x, y = site
        pyplot.quiver(x, y, 0, spin, pivot="middle", color=colors[spin])
    pyplot.xticks(range(-1,length+1))
    pyplot.yticks(range(-1,length+1))
    pyplot.gca().set_aspect("equal")
    pyplot.savefig("EJERCICIOS/Estado_Inicial.png")
    pyplot.show()

#Asignación de primeros vecinos

for site in spins.keys():
    x, y = site
    if x + 1 < length: #Vecinos por derecha
        nbhs[site].append(((x + 1) % length, y))
    if x - 1 >= 0: #Vecinos por izquierda
        nbhs[site].append(((x - 1) % length, y))
    if y + 1 < length: #Vecino por arriba
        nbhs[site].append((x, (y + 1) % length))
    if y - 1 >= 0: #Vecino por abajo
        nbhs[site].append((x, (y - 1) % length))

#Energías

def energy_site(site):
    energy = 0.0
    for nbh in nbhs[site]:
        energy += spins[site] * spins[nbh]
    return -j * energy

def total_energy():
    energy = 0.0
    for site in sites:
        energy += energy_site(site)
    return 0.5 * energy

def magnetization():
    mag = 0.0
    for spin in spins.values():
        mag += spin
    return mag


#Implementación del algoritmo Metrópolis para el sistema Ising-2D.

def metropolis(site, T):
    oldSpin = spins[site]
    oldEnergy = energy_site(site)
    spins[site] *= -1
    newEnergy = energy_site(site)
    deltaE = newEnergy - oldEnergy
    if deltaE <= 0:
        pass #El cambio fue aceptado
    else:
        if numpy.random.uniform(0, 1) <= numpy.exp(-deltaE/(kB*T)):
            pass
        else:
            spins[site] *= -1

#Montecarlo
def monte_carlo_step(T):
    for i in range(len(sites)):
        int_rand_site = numpy.random.randint(0, len(sites))
        rand_site = sites[int_rand_site]
        metropolis(rand_site, T)

#Simulación
amount_mcs = 50
T_high = 5.0
T_low = 0.1
step = -0.1


#Ciclo de temperatura
temps = numpy.arange(T_high, T_low, step)
energies = numpy.zeros(shape=(len(temps), amount_mcs))
magnetizations = numpy.zeros(shape=(len(temps), amount_mcs))
random_configuration()
for ind_T, T in enumerate(temps):
    for i in range(amount_mcs):
        monte_carlo_step(T)
        energies[ind_T, i] = total_energy()
        magnetizations[ind_T, i] = magnetization()

print(energies)
#Visualizar los spines
plot_spins()

tau = amount_mcs // 2
energy_mean = numpy.mean(energies[:, tau:], axis=1)
magnetization_mean = abs(numpy.mean(magnetizations[:, tau:], axis=1))

pyplot.figure()
pyplot.plot(temps, energy_mean, label="Energy")
pyplot.legend()
pyplot.xlabel(r"$T$")
pyplot.ylabel(r"$\left<E\right>$")
pyplot.grid()
pyplot.show()

pyplot.figure()
pyplot.plot(temps, magnetization_mean, label="Magnetization")
pyplot.legend()
pyplot.xlabel(r"$T$")
pyplot.ylabel(r"$\left<M\right>$")
pyplot.grid()
pyplot.show()


#Revisar la simulación
#Dibujar el sistema final
#Graficar la energía y la magnetización en función de la temperatura