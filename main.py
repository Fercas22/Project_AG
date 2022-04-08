import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

import AG as ag
qtCreatorFile = "view/mainView.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Title
        self.setWindowTitle('.:: ALGORITMOS GENETICOS ::.')
        # self.setFixedSize(800, 600)

        #Validar tipos de datos
        self.initialPopulation.setValidator(QtGui.QIntValidator()) # int poblacion Inicial
        self.populationLimit.setValidator(QtGui.QIntValidator()) # int poblacion maxima
        self.intervalMinX.setValidator(QtGui.QIntValidator()) # int intervalo min X
        self.intervalMaxX.setValidator(QtGui.QIntValidator()) # int intervalo max X
        self.intervalMinY.setValidator(QtGui.QIntValidator()) # int intervalo min Y
        self.intervalMaxY.setValidator(QtGui.QIntValidator()) # int intervalo max Y
        self.mutationIndividual.setValidator(QtGui.QDoubleValidator()) # double mutacion Indiviuo
        self.chromosomeMutation.setValidator(QtGui.QDoubleValidator()) #double mutacion Gen
        self.resolution.setValidator(QtGui.QDoubleValidator()) # double resolucion
        self.generation.setValidator(QtGui.QIntValidator()) #int generacion
        #

        #Buttons
        self.startButton.clicked.connect(self.getValues)
        self.exitButton.clicked.connect(self.exit)
    
    def getValues(self):
        self.initialPopulation.setText('034')
        initialPopulation = self.initialPopulation.text()
        populationLimit = self.populationLimit.text()

        intervalMinX = self.intervalMinX.text()
        intervalMaxX = self.intervalMaxX.text()

        intervalMinY = self.intervalMinY.text()
        intervalMaxY = self.intervalMaxY.text()

        mutationIndividual = self.mutationIndividual.text()
        chromosomeMutation = self.chromosomeMutation.text()

        resolution = self.resolution.text()
        generation = self.generation.text()



        if initialPopulation and populationLimit and intervalMinX and intervalMaxX and intervalMinY and intervalMaxY and mutationIndividual and chromosomeMutation and resolution and generation:
            self.initialPopulation.setStyleSheet(None)#
            self.populationLimit.setStyleSheet(None)#
            self.intervalMinX.setStyleSheet(None)
            self.intervalMaxX.setStyleSheet(None)
            self.intervalMinY.setStyleSheet(None)
            self.intervalMaxY.setStyleSheet(None)
            self.mutationIndividual.setStyleSheet(None)
            self.chromosomeMutation.setStyleSheet(None)
            self.resolution.setStyleSheet(None)
            self.generation.setStyleSheet(None)


            print('VALIDACIONES')
            initialPopulation = int(initialPopulation)
            populationLimit = int(populationLimit)

            intervalMinX = int(intervalMinX) #MinX
            intervalMaxX = int(intervalMaxX) #MaxX

            intervalX = [intervalMinX, intervalMaxX]  # agregar en arreglo, Min y Max de X
            
            intervalMinY = int(intervalMinY) #MinY
            intervalMaxY = int(intervalMaxY) #MaxY

            intervalY = [intervalMinY, intervalMaxY] # agregar en arreglo, Min y Max de Y

            mutationIndividual = float(mutationIndividual)
            chromosomeMutation = float(chromosomeMutation)
            resolution = float(resolution)
            generation = int(generation)

            #LLamada de la funcion main del archivo AG.py
            ag.main(initialPopulation, populationLimit, intervalX, intervalY, mutationIndividual, chromosomeMutation, resolution, generation)

        else:
            print('Vacio')
            if not initialPopulation:
                self.initialPopulation.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.initialPopulation.setStyleSheet(None)
            
            if not populationLimit:
                self.populationLimit.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.populationLimit.setStyleSheet(None)
            
            if not intervalMinX:
                self.intervalMinX.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.intervalMinX.setStyleSheet(None)
            
            if not intervalMaxX:
                self.intervalMaxX.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.intervalMaxX.setStyleSheet(None)
            
            if not intervalMinY:
                self.intervalMinY.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.intervalMinY.setStyleSheet(None)
            
            if not intervalMaxY:
                self.intervalMaxY.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.intervalMaxY.setStyleSheet(None)
            
            if not mutationIndividual:
                self.mutationIndividual.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.mutationIndividual.setStyleSheet(None)
            
            if not chromosomeMutation:
                self.chromosomeMutation.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.chromosomeMutation.setStyleSheet(None)
            
            if not resolution:
                self.resolution.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.resolution.setStyleSheet(None)
            
            if not generation:
                self.generation.setStyleSheet('border: 3px solid yellow; background-color: #ffffff;')
            else:
                self.generation.setStyleSheet(None)

            QMessageBox.warning(None, 'Vacia', '¡¡Campo vacio, ingrese el valor al campo(s) vacio(s)!!')
        

       
    
    def exit(self):
        # self.close()
        salir = QMessageBox.question(self, 'Salir','¿Esta seguro que desea salir?',QMessageBox.Yes, QMessageBox.No)

        if salir == QMessageBox.Yes:
            self.close()
    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())