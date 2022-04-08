from operator import le
import matplotlib.pyplot as plt
import os
import cv2
import datetime as date





def graficaGeneracionSinPoda(generaSinPoda, rangoX, rangoY):
    
    generacion_sinPoda = generaSinPoda.copy()
    x = []
    y = []
    print(f'RANGOX {rangoX} RANGOY {rangoY}')
    # plt.axis([rangoX[0], rangoY[1], rangoY[0], rangoY[1]])
    

    for i in range(len(generacion_sinPoda)):
        for j in range(len(generacion_sinPoda[i][1])):
            # print(f'i-->{i}  j-->{j}')
            # print(f'GENERACION -->{i+1} FENOTIPOX {generacion_sinPoda[i][1][j].fenotipoX} FENOTIPOY {generacion_sinPoda[i][1][j].fenotipoY}')
            # plt.scatter(generacion_sinPoda[i][1][j].fenotipoX, generacion_sinPoda[i][1][j].fenotipoY)
            x.append(generacion_sinPoda[i][1][j].fenotipoX)
            y.append(generacion_sinPoda[i][1][j].fenotipoY)
            plt.scatter(x,y)
        print(f'FENOTIPO EN X --> {x}')
        print(f'FENOTIPO EN Y --> {y}')
        plt.xlabel(str(len(x)))
        plt.ylabel(str(len(y)))
        # plt.axis([min(x),max(x)+1, min(y), max(y)+1])
        
        # print(f'{[min(x),max(x), min(y), max(y)]}')
        # print(f'{[min(x),max(x)+1, min(y), max(y)+1]}')
        plt.xlim(0, 15)
        plt.ylim(0, 15)
        # plt.xlim(rangoX[0], rangoY[1])
        # plt.ylim(rangoY[0], rangoY[1])
        # print(f'{rangoX[i]} --> {rangoY[i]}')
        plt.title(f'Generación {i+1}')
        # print(os.getcwd())
        if i+1 < 10:
            plt.savefig(f'./img/img0{i+1}')
        else:
            plt.savefig(f'./img/img{i+1}')
        # tiempo = str(date.datetime.now()).replace(':','_')
        # tiempo = tiempo.replace('-','_')
        # tiempo = tiempo.replace(' ','__')
        # print("NOMBRE DE LA IMAGEN: " +str(i)+'_'+tiempo[:19])
        # plt.savefig('./img/'+str(i)+'_'+tiempo[:19])
        # plt.show()
        x.clear()
        y.clear()
    # print(f'FENOTIPO X --> {x} TAMAÑO --> {len(x)} MINX --> {min(x)} MAX_X --> {max(x)}')
    # print(f'FENOTIPO Y --> {y} TAMAÑO --> {len(x)} MIN_Y --> {min(y)} MAX_Y --> {max(y)}')

    # miny = min(y)
    # plt.xlabel(miny)

    # minx = min(x)
    # maxx = max(x)
    # miny = min(y)
    # maxy = max(y)

    # plt.xlim(minx, maxx)
    # plt.ylim(miny, maxy)
    # plt.axis([miny,maxy, minx, maxx])
    # for i in range(len(generacion_sinPoda)):
    #     plt.scatter(x, y)
    #     plt.show()

def convertToVideo():
    path = os.getcwd()+'/img/'
    archivos = sorted(os.listdir(path))
    img_array = []
    print(archivos)
    # # #Leer imagenes
    for i in range(0,len(archivos)):
        nombreArchivo = archivos[i]
        print(nombreArchivo)
        dirArchivo = path+str(nombreArchivo)
        print(dirArchivo)
        img = cv2.imread(dirArchivo)
        img_array.append(img)
        # cv2.imshow('img_'+str(i+1),img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    # alto, ancho = img.shape[:2]
    # print(f'SHAPE --> {img.shape}')
    print("CREAR VIDEO -->")
    print(f"ESTO ES EL ARRAY {img_array}")
    alto = img.shape[0]
    ancho = img.shape[1]
    video = cv2.VideoWriter('./video/videoEvolucion.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, (ancho, alto))

    for i in range(0, len(archivos)):
        video.write(img_array[i])
        # print(img_array[i])
    
    video.release()
    #Borrar las imagenes
    # for i in range(0,len(archivos)):
    #     nombreArchivo = archivos[i]
    #     print(nombreArchivo)
    #     dirArchivo = path+str(nombreArchivo)
    #     print(dirArchivo)
    #     os.remove(dirArchivo)
    
        

