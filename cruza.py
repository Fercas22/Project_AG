import random
from individuoData import IndividuoCruza

class Cruza():

    def cruza(self, individual):
        individuosC = [] # Individuos cruza
        pares = []
        poblation = individual.copy()

        while len(poblation) > 0:
            aleatorio = random.randint(0, len(poblation)-1)
            pareja1 = poblation.pop(aleatorio)
            # print(f'pareja1 --> {pareja1.name}')
            if len(poblation) > 0:
                aleatorio2 = random.randint(0, len(poblation)-1)
                pareja2 = poblation.pop(aleatorio2)
                # print(f'Pareja2 --> {pareja2.name}')
                pares.append([pareja1, pareja2])
                # print(f'PARES --> {pares}')
            else:
                pares.append([pareja1])
                # print(f'Pareja de 1 --> {pares}')       
        # print(f'{pares}')

        for i in range(len(pares)):
            puntoX =  random.randint(0, len(pares[i][0].genotipoX)-1)
            puntoY =  random.randint(0, len(pares[i][0].genotipoY)-1)     
            # print(f'puntoX --> {puntoX}  PuntoY --> {puntoY}')

            # ACCEDIENDO AL GENOTIPO DE DE LOS INDIVIDUOS
            if len(pares[i]) > 1:
                # print(f'Que es esto? {pares[i][0].name}--> {len(pares[i])}')
                p1x = pares[i][0].genotipoX
                p1y = pares[i][0].genotipoY
                p2x = pares[i][1].genotipoX
                p2y = pares[i][1].genotipoY
                name1 = ''
                name2 = ''
                name1 += pares[i][0].name
                name2 += pares[i][1].name
                # print(f'Name1 --> {name1} Name2 -->{name2}')
                # print(f'P1X --> {p1x} P2X --> {p2x}')
                hijo1BitsX = []
                hijo1BitsY = []

                for punto_X in range(len(p1x)):
                    # print(punto_X)
                    # print(f'PUNTOX {p1}')
                    if punto_X >= puntoX:
                        hijo1BitsX.append(p2x[punto_X])
                        # print(f'Hijox2 --> {p2x[punto_X]}')
                    else:
                        hijo1BitsX.append(p1x[punto_X])
                        # print(f'Hijo1 --> {p1x[punto_X]}')
                # print(f'P1Y --> {p1y} P2Y --> {p2y}')  

                for punto_Y in range(len(p1y)):
                    if punto_Y >= puntoY:
                        hijo1BitsY.append(p2y[punto_Y])
                        # print(f'P2y HIJOS BITS Y --> {p2y[punto_Y]}')
                    else:
                        hijo1BitsY.append(p1y[punto_Y])
                        # print(f'P1Y HIJOS BITS Y --> {p1y[punto_Y]}')
                # print(f'Esto es hijosX --> {hijo1BitsX}')
                # print(f'Esto es hijosY --> {hijo1BitsY}')
                ind = IndividuoCruza(name2+name1, hijo1BitsX, hijo1BitsY)
                individuosC.append(ind)
                # print(individuosC)
                hijo2BitsX = []
                hijo2BitsY = []

                for x in range(len(p1x)):
                    if x >= puntoX:
                        hijo2BitsX.append(p1x[x])
                        # print(f'Hijo 2X Px1--> {p1x[x]}')
                    else:
                        hijo2BitsX.append(p2x[x])
                        # print(f'Px1 Hijos X p2 --> {p2x[x]}')

                for y in range(len(p1y)):
                    if y >= puntoY:
                        hijo2BitsY.append(p1y[y])
                        # print(f'{p1y[y]}')
                    else:
                        hijo2BitsY.append(p2y[y])
                        # print(f'{p2y[y]}')

                ind = IndividuoCruza(name1+name2, hijo2BitsX, hijo2BitsY)
                individuosC.append(ind)
                # print(f'px1 {p1x}')
                # print(f'py1 {p1y}')
                # print(f'px2 {p2x}')
                # print(f'py2 {p2y}')
                # print(f'Name -->{name1+name2} Esto es hijosX1 --> {hijo1BitsX}')
                # print(f'Name --> {name1+name2} Esto es hijosY1 --> {hijo1BitsY}')
                # print(f' Name --> {name2+name1} Esto es hijosX2 --> {hijo2BitsX}')
                # print(f' Name --> {name2+name1}Esto es hijosY2 --> {hijo2BitsY}')
            else:
                name1 = ''
                name1 += pares[i][0].name + pares[i][0].name
                # print(f'NAME_1 --> {name1}')
                ind = IndividuoCruza(name1, pares[i][0].genotipoX, pares[i][0].genotipoY)
                individuosC.append(ind)

        #Individuos
        # for i in range(len(individuosC)):
        #     print('NAME --> ', individuosC[i].name,' GENOTIPOX --> ', individuosC[i].genotipoX, 'GENOTIPOY --> ',individuosC[i].genotipoY)
        # print(individuosC)

        #Retornar la lista de nuevos individuos generados de la cruza
        return individuosC