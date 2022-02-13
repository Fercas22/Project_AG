import math
import random
from individuoData import *

from metodosIndividuo import *
from mutacion import *

import cruza


def main():
    mutacion = Mutacion()
    metodos = MetodosIndividuo()
    name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    initialPopulation = 5
    populationLimit = 4
    mutationIndividual = 0.6
    chromosomeMutation = 0.07
    resolution = 0.08
    intervalX = [-3, 5]
    intervalY = [5, 8]

    numberValue = []
    bits = []
    arrayX = []
    arrayY = []
    individual = []
    
    # Tamaño y numero de valores del intervalo
    numberValue.append(metodos.intervalSizes(intervalX, resolution))
    numberValue.append(metodos.intervalSizes(intervalY, resolution))

    # Calcular los bits que se necesitan para los valores del intervalo
    for i in range(0, 2):
        bits.append(metodos.numberBits(numberValue[i]))

    # Generar los indivduos de la poblacion inicial con sus datos
    for i in range(0, initialPopulation):
        bandera = False
        while bandera == False:
            arrayX.append(metodos.randonBits(bits[0][0]))
            arrayY.append(metodos.randonBits(bits[1][0]))
            fenotipoX = round(intervalX[0] + (arrayX[i][1] * resolution), 4)
            fenotipoY = round(intervalY[0] + (arrayY[i][1] * resolution), 4)
            if fenotipoX > 0 and fenotipoY > 0:
                # - x**3 ln y + 4xy - 2y**2 ln x +1
                aptitud = (-(fenotipoX**3)) * (math.log(fenotipoY)) + (4 * fenotipoX * fenotipoY) - (2*(fenotipoY**2)) * math.log(fenotipoX) + 1
                ind = Individual(name[i], arrayX[i][0], arrayY[i][0], arrayX[i][1], arrayY[i][1], fenotipoX, fenotipoY, aptitud)
                individual.append(ind)
                for k in individual:
                    # print(k.iX, '<=', numberValue[0], 'and', k.iY, '<=', numberValue[1])
                    if k.iX <= numberValue[0] and k.iY <= numberValue[1]:
                        bandera = True
                    else:
                        individual.pop()
                        arrayX.pop()
                        arrayY.pop()
                        bandera = False
                        break
            else:
                arrayX.pop()
                arrayY.pop()
                bandera = False

    # print('id =', individual[0].name, 'X =', individual[0].genotipoX, 'iX =', individual[0].iX, 'fenotipoX =', individual[0].fenotipoX, 'Y =', individual[0].genotipoY, 'iY =', individual[0].iY, 'fenotipo =', individual[0].fenotipoY, 'Aptitud =', individual[0].aptitud)
    # print('id =', individual[1].name, 'X =', individual[1].genotipoX, 'iX =', individual[1].iX, 'fenotipoX =', individual[1].fenotipoX, 'Y =', individual[1].genotipoY, 'iY =', individual[1].iY, 'fenotipo =', individual[1].fenotipoY, 'Aptitud =', individual[1].aptitud)
    for i in range(len(individual)):
        print(individual[i].name)

    # print(cruza.cruza(individual))
    # print(cruza.cruza(individual))
    cruza.cruza(individual)


main()