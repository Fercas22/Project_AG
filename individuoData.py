class Individual():
    
    def __init__(self, name, genotipoX, genotipoY, iX, iY, fenotipoX, fenotipoY, aptitud):
        self.name = name
        self.genotipoX = genotipoX
        self.genotipoY = genotipoY
        self.iX = iX
        self.iY = iY
        self.fenotipoX = fenotipoX
        self.fenotipoY = fenotipoY
        self.aptitud = aptitud
        # pass

    def __str__(self):
        return self.name, self.genotipoX, self.genotipoY, self.iX, self.iY, self.fenotipoX, self.fenotipoY, self.aptitud
    


class IndividuoCruza():
    def __init__(self, name, genotipoX, genotipoY):
        self.name = name
        self.genotipoX = genotipoX
        self.genotipoY = genotipoY
    
    def __str__(self):
        return self.name, self.genotipoX, self.genotipoY