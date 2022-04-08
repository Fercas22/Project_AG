import math
from optparse import BadOptionError
import random
from re import I
from cruza import *
from individuoData import *
from metodosIndividuo import *
from mutacion import *
from grafGeneSinPoda import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

generacionSinPoda = [] # [generacion, objeto<individuo>] = [[1, objeto], [2, objeto]...]
generacionPeor = [] # [generacion, peorIndividuo]
generacionPromedio = [] # [generacion, promedioIndividuo]
generacionMejor = [] # [generacion, mejorIndividuo]
poblacion = [] # [objetos<Individuo>]
mejores = [] # Almacenar a los 5 mejores

def main(initialPopulation, populationLimit, intervalX, intervalY, mutationIndividual, chromosomeMutation, resolution, generacion):
# def main():

    metodos = MetodosIndividuo()
    name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    initialPopulation = 5 #Comentar
    populationLimit = 7 #Comentar
    mutationIndividual = 0.6 #Comentar
    chromosomeMutation = 0.07 #Comentar
    resolution = 0.08 #Comentar
    intervalX = [-3, 5] # Comentar
    intervalY = [5, 8] #Comentar
    generacion = 20

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
        poblacion.append(individual[i])
    
    for i in range(0, generacion):
        # gene = []
        print('Genracion cmp:', i+1)
        gene = cmp(poblacion, mutationIndividual, chromosomeMutation, intervalX[0], intervalY[0], resolution, numberValue, populationLimit)
        # print(gene[i][1])
        generacionSinPoda.append([i + 1, gene[0]])
        generacionPeor.append([i + 1, gene[1]])
        generacionPromedio.append([i + 1, gene[2]])
        generacionMejor.append([i + 1, gene[3]])

    # print(generacionPeor)
    # print(len(generacionSinPoda))
    # print(generacionSinPoda)
    print('GENERACIONES')
    for j in range(len(generacionSinPoda)):
        print('GENERACION:', generacionSinPoda[j][0])
        # print('Peor:', generacionPeor[j][1])
        for k in range(len(generacionSinPoda[j][1])):
            print(generacionSinPoda[j][1][k].name)

    print("Llega a la grafica de genaracion sin poda")
    graficaGeneracionSinPoda(generacionSinPoda, intervalX, intervalY)
    # convertToVideo(pathIn, pathOut, fps, time)
    print("Llega a convertir video")
    convertToVideo()
    grafica(generacion)
    # print(generacionMejor)
    # print(generacionPeor)
    # print(generacionPromedio)

    
def cmp(individual, mutacionInd, cromosomaInd, intervalX, intervalY, resolution, valores, populationLimit):
    cruza = Cruza()
    mutacion = Mutacion()
    individuoIni = individual.copy()
    individuoAux = []
    generacion = []
    apt = []
    aptPo = []
    # print(individual)
    # Añadir la poblacion incial a un auxiliar
    for i in range(len(individuoIni)):
        individuoAux.append(individuoIni[i])
    #  Elaborar cruza y mutacion
    cru = cruza.cruza(individual)
    muta = mutacion.pMutacionIndividuo(cru, mutacionInd, cromosomaInd, intervalX, intervalY, resolution, valores)
    # Añadir los individuos de la mutacion al auxiliar
    for j in range(len(muta)):
        individuoAux.append(muta[j])
    # Individuos sin poda
    # for k in range(len(individuoAux)):
    #     print(individuoAux[k].name)

    for i in range(len(individuoAux)):
        # print(individuoAux[i].name, individuoAux[i].aptitud)
        apt.append(individuoAux[i].aptitud)
    
    # Peor individuo de la generacion
    minValue = min(apt)
    # print(minValue)
    # Poda
    po = poda(individuoAux, populationLimit, apt)
    # Promedio de la generacion
    suma = 0
    for i in range(len(po)):
        # print(po[i].name, po[i].aptitud)
        aptPo.append(po[i].aptitud)
        suma = suma + po[i].aptitud
    promedio = suma / len(po)
    # Mejor individuo de la generacion
    maxValue = max(aptPo)
    # generacion = [sinPoda, peor, promedio, mejor]
    generacion.append(individuoAux)
    generacion.append(minValue)
    generacion.append(promedio)
    generacion.append(maxValue)

    for i in range(len(poblacion)):
        poblacion.pop()

    for j in range(len(po)):
        poblacion.append(po[j])
    # print(generacion)
    mejores.clear()
    mejores5 = mejor(po)

    return generacion

def poda(individuo, populationLimit, apt):
    ind = individuo.copy()
    apt = apt.copy()
    
    while len(ind) > populationLimit:
        # print(len(ind), '>', populationLimit)
        minValue = min(apt)
        # print(maxValue)
        for i in range(len(ind)):
            # print(ind[i].aptitud, '=', maxValue)
            if ind[i].aptitud == minValue:
                ind.pop(i)
                break
        for j in range(len(apt)):
            if apt[j] == minValue:
                apt.pop(j)
                break 
    return ind

def mejor(pobla):
    ind = pobla.copy()
    apt = []
    
    for i in range(len(ind)):
        # print(individuoAux[i].name, individuoAux[i].aptitud)
        apt.append(ind[i].aptitud)

    while len(ind) > 5:
        # print(len(ind), '>', populationLimit)
        minValue = min(apt)
        # print(maxValue)
        for i in range(len(ind)):
            # print(ind[i].aptitud, '=', maxValue)
            if ind[i].aptitud == minValue:
                ind.pop(i)
                break
        for j in range(len(apt)):
            if apt[j] == minValue:
                apt.pop(j)
                break 
    return ind

def grafica(generacion):
    print('Entramos a grafica')
    print(generacionMejor)
    print(generacionPeor)
    print(generacionPromedio)
    promedio = []
    peorAptitud = []
    mejorAptitud = []
    # print(len(generacion))
    
    tam = []
    for j in range(0, generacion):
        tam.append(j)
    print(len(tam))
    # print(generacionPromedio[1][1])
    for i in range(len(generacionMejor)):
        promedio.append(int(generacionPromedio[i][1]))
        peorAptitud.append(generacionPeor[i][1])
        mejorAptitud.append(generacionMejor[i][1])

    figure = plt.figure(figsize=(5,5))
    ax = plt.subplot(1,1,1)
    ax.plot( tam, promedio, label='Promedio',marker='.')  # Plot some data on the (implicit) axes.
    ax.plot( tam, peorAptitud, label='Peor',marker='.')  # etc.
    ax.plot( tam, mejorAptitud, label='Mejor',marker='.')

    blue_line = mlines.Line2D([], [], color='blue', markersize=10, label='Promedio')
    red = mlines.Line2D([], [], color='orange', markersize=10, label='Peor')
    yel = mlines.Line2D([], [], color='green', markersize=10, label='Mejor')
    ax.legend(handles=[blue_line,red,yel])

    plt.show()  


# main()