import math
import random
from re import I
from tarfile import LENGTH_NAME

from numpy import mat, number
from objeto import *

# intervalo.append(int(input('Ingrese el inicio del intervalo: ')))
# intervalo.append(int(input('Ingrese el final del intervalo: ')))
# resolucion = float(input('Ingrese la resolución: '))
# cambios
def main():
    name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    initialPopulation = 2
    populationLimit = 4
    mutationIndividual = 0
    chromosomeMutation = 0
    resolution = 0.08
    intervalX = [-3, 5]
    intervalY = [5, 8]

    numberValue = []
    bits = []
    arrayX = []
    arrayY = []
    individual = []
    
    # Tamaño y numero de valores del intervalo
    numberValue.append(intervalSizes(intervalX, resolution))
    numberValue.append(intervalSizes(intervalY, resolution))
    # Calcular los bits que se necesitan para los valores del intervalo
    for i in range(0, 2):
        bits.append(numberBits(numberValue[i]))
    # Generar los indivduos de la poblacion con nombre, genotipo e i = valor

    for i in range(0, initialPopulation):
        bandera = False
        print('Vuelta #', i)
        while bandera == False:
            print('Dentro del while en', i)
            print(len(individual))
            arrayX.append(randonBitsX(bits[0][0]))
            arrayY.append(randonBitsY(bits[1][0]))
            fenotipoX = round(intervalX[0] + (arrayX[i][1] * resolution), 4)
            fenotipoY = round(intervalY[0] + (arrayY[i][1] * resolution), 4)
            ind = Individual(name[i], arrayX[i][0], arrayY[i][0], arrayX[i][1], arrayY[i][1], fenotipoX, fenotipoY, 0)
            individual.append(ind)
            for k in individual:
                print('Entramos al for each en i =', i)
                print('Tamaño despues de agregar', len(individual))
                print(k.iX, '<=', numberValue[0], 'and', k.iY, '<=', numberValue[1])
                if k.iX <= numberValue[0] and k.iY <= numberValue[1]:
                    print('Calificas')
                    bandera = True
                else:
                    print('No entramos')
                    individual.pop()
                    arrayX.pop()
                    arrayY.pop()
                    bandera = False
                    break
    
    # - x**3 ln y + 4xy - 2y**2 ln x +1
    a = (-fenotipoX)**3
    # b = math.log(fenotipoY)
    # c = (4 * fenotipoX * fenotipoY)
    # d = -2 (fenotipoY**2)
    # e = math.log(fenotipoX)
    print(numberValue)
    print(individual[0].name, individual[0].genotipoX, individual[0].iX, individual[0].genotipoY, individual[0].iY)
    print(individual[1].name, individual[1].genotipoX, individual[1].iX, individual[1].genotipoY, individual[1].iY)
   
# Arreglo de bits para X y su valor en decimal
def randonBitsX(a):
    contadorBits = ''
    arrayBitsX = []
    decimal = 0
    arrayReturn = []
    for i in range(0, a):
        arrayBitsX.append(random.randint(0, 1))
        contadorBits = contadorBits + str(arrayBitsX[i])
    decimal = binario_to_Decimal(int(contadorBits))
    arrayReturn.append(arrayBitsX)
    arrayReturn.append(decimal)
    return arrayReturn

# Arreglo de bits para Y y su valor en decimal
def randonBitsY(a):
    contadorBits = ''
    arrayBitsY = []
    decimal = 0
    arrayReturn = []
    for i in range(0, a):
        arrayBitsY.append(random.randint(0, 1))
        contadorBits = contadorBits + str(arrayBitsY[i])
    decimal = binario_to_Decimal(int(contadorBits))
    arrayReturn.append(arrayBitsY)
    arrayReturn.append(decimal)
    return arrayReturn

# Binario a Decimal
def binario_to_Decimal(binario):
    decimal = 0
    i = 0
    while (binario > 0):
        digito  = binario%10
        binario = int(binario//10)
        decimal = decimal+digito*(2**i)
        i = i + 1
    return decimal

# Tamaño de intervalo
def intervalSizes(interval, resolution):
    intervalSize = abs(interval[1] - (interval[0]))
    numberValues  = math.ceil((intervalSize / resolution) + 1)
    return numberValues

# Número de bits y su equivalencia
def numberBits(valor):
    # [0] = Bit, [1] = 2^Bit
    bits = [0, 0]
    while bits[1] <= valor:
        bits[0] += 1
        bits[1] = 2**bits[0]
    return bits

main()