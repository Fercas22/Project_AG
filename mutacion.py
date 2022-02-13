import random
from unicodedata import decimal
from numpy import round_
from metodosIndividuo import *

class Mutacion():
    
    def pMutacionIndividuo(self, listaIndividuo, mutacionInd, cromosomaInd):
        for i in range(len(listaIndividuo)):
            proMutacion = round(random.uniform(0,1),4)
            # print(proMutacion, '<=', mutacionInd)
            # print(listaIndividuo[i].genotipoX, listaIndividuo[i].name)
            if (proMutacion <= mutacionInd):
                # print(listaIndividuo[i].genotipoX)
                self.mutacionX(listaIndividuo[i].genotipoX, cromosomaInd)
                # print(listaIndividuo[i].genotipoX)
                
    def mutacionX(self, x, cromosomaInd):
        metodos = MetodosIndividuo()
        bits = ''
        decimal = 0
        for i in range(len(x)):
            proCromosoma = round(random.uniform(0,1),4)
            # print(proCromosoma ,'<=', cromosomaInd)
            if (proCromosoma <= cromosomaInd):
                if (x[i] == 0):
                    # print(i)
                    x[i] = 1
                elif (x[i] == 1):
                    # print(i)
                    x[i] = 0
            bits = bits + str(x[i])
        decimal = metodos.binario_to_Decimal(int(bits))