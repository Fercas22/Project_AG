import random
from individuoData import *
from metodosIndividuo import *

class Mutacion():
    
    def pMutacionIndividuo(self, cru, mutacionInd, cromosomaInd, intervalX, intervalY, resolution, valores):
        individualNew = []
        for i in range(len(cru)):
            proMutacion = round(random.uniform(0,1),4)
            # print(proMutacion, '<=', mutacionInd)
            # print(cru[i].genotipoX, cru[i].name)
            # Validar que la probabilidad del individuo sea apta para mutar
            if (proMutacion <= mutacionInd):
                # print(cru[i].name, cru[i].genotipoX, cru[i].genotipoY)
                self.mutacionX(cru[i].genotipoX, cromosomaInd)
                self.mutacionY(cru[i].genotipoY, cromosomaInd)
                # print(cru[i].name, cru[i].genotipoX, cru[i].genotipoY)
            # print(cru[i].name, cru[i].genotipoX, cru[i].genotipoY)
            # Generar los decimales para los nuevos individuos
            deciX = self.decimalX(cru[i].genotipoX)
            deciY = self.decimalY(cru[i].genotipoY)
            # print(cru[i].name, deciX, deciY)
            # print('Nombre:', cru[i].name, 'deciX:', deciX, '<=', valores[0], 'deciY', deciY, '<=', valores[1])
            # Validar que los decimales dados sean mayores a los intervalos proporcionados
            if deciX <= valores[0] and deciY <= valores[1]:
                fenoX = round(intervalX + (deciX * resolution), 4)
                fenoY = round(intervalY + (deciY * resolution), 4)
                # print(cru[i].name, deciX, deciY, fenoX, fenoY)
                # Validar que los fenotipos sean mayor a 0 para que no sean indefinidos
                if fenoX > 0 and fenoY > 0:
                    # - x**3 ln y + 4xy - 2y**2 ln x +1
                    aptitud = (-(fenoX**3)) * (math.log(fenoY)) + (4 * fenoX * fenoY) - (2*(fenoY**2)) * math.log(fenoX) + 1
                    ind = Individual(cru[i].name, cru[i].genotipoX, cru[i].genotipoY, deciX, deciY, fenoX, fenoY, aptitud)
                    individualNew.append(ind)
                    # print('id =', individualNew[i].name, 'X =', individualNew[i].genotipoX, 'iX =', individualNew[i].iX, 'fenotipoX =', individualNew[i].fenotipoX, 'Y =', individualNew[i].genotipoY, 'iY =', individualNew[i].iY, 'fenotipoY =', individualNew[i].fenotipoY, 'Aptitud =', individualNew[i].aptitud)
            # print(cru[i].name, deciX, deciY)
        return individualNew
 
    def mutacionX(self, x, cromosomaInd):
        metodos = MetodosIndividuo()
        for i in range(len(x)):
            proCromosoma = round(random.uniform(0,1),4)
            # print(proCromosoma ,'<=', cromosomaInd)
            if (proCromosoma <= cromosomaInd):
                if (x[i] == 0):
                    # print(i, 'X')
                    x[i] = 1
                elif (x[i] == 1):
                    # print(i, 'X')
                    x[i] = 0

    def mutacionY(self, y, cromosomaInd):
        metodos = MetodosIndividuo()
        for i in range(len(y)):
            proCromosoma = round(random.uniform(0,1),4)
            # print(proCromosoma ,'<=', cromosomaInd)
            if (proCromosoma <= cromosomaInd):
                if (y[i] == 0):
                    # print(i, 'Y')
                    y[i] = 1
                elif (y[i] == 1):
                    # print(i, 'Y')
                    y[i] = 0
        
    def decimalX(self, x):
        metodo = MetodosIndividuo()
        bits = ''
        decimal = 0
        for i in range(0, len(x)):
            bits = bits + str(x[i])
        decimal = metodo.binario_to_Decimal(int(bits))
        # print('Contador =', contadorBits)
        return decimal
    
    def decimalY(self, y):
        metodo = MetodosIndividuo()
        bits = ''
        decimal = 0
        for i in range(0, len(y)):
            bits = bits + str(y[i])
        decimal = metodo.binario_to_Decimal(int(bits))
        # print('Contador =', contadorBits)
        return decimal