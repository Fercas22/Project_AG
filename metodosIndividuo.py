import math
import random

class MetodosIndividuo():

    # Arreglo de bits para X y Y con su valor en decimal
    def randonBits(self, a):
        contadorBits = ''
        arrayBits = []
        decimal = 0
        arrayReturn = []
        for i in range(0, a):
            arrayBits.append(random.randint(0, 1))
            contadorBits = contadorBits + str(arrayBits[i])
        decimal = self.binario_to_Decimal(int(contadorBits))
        # print('Contador =', contadorBits)
        arrayReturn.append(arrayBits)
        arrayReturn.append(decimal)
        return arrayReturn

    # Binario a Decimal
    def binario_to_Decimal(self, binario):
        decimal = 0
        i = 0
        while (binario > 0):
            digito  = binario%10
            binario = int(binario//10)
            decimal = decimal+digito*(2**i)
            i = i + 1
        return decimal

    # Tamaño de intervalo
    def intervalSizes(self, interval, resolution):
        intervalSize = abs(interval[1] - (interval[0]))
        numberValues  = math.ceil((intervalSize / resolution) + 1)
        return numberValues

    # Número de bits y su equivalencia
    def numberBits(self, valor):
        # [0] = Bit, [1] = 2^Bit
        bits = [0, 0]
        while bits[1] <= valor:
            bits[0] += 1
            bits[1] = 2**bits[0]
        return bits