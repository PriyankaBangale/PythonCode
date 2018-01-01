class Car(object):

    def __init__(self, no_of_tyres, steeringType):
        self.no_of_tyres = no_of_tyres
        self.steeringType = steeringType

    def __del__(self):
        print 'Car object is destoyed'

    def __engineType(self): # Private methods
        print 'Fiat XL minature'

    def moveCar(self, direction):
        self.__engineType()

audi = Car(5, 'Manual')  # Audi is an object of Car class
merc = Car(no_of_tyres=6, steeringType='Automatic') # Merc

print audi.no_of_tyres
print merc.moveCar(direction='left')