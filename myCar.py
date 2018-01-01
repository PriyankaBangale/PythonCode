class Car(object):
    no_of_tyres = 5
    steeringType = 'Manual'

    @staticmethod
    def myCarGearType(type):
        print 'Gear type of the car is', type

    def moveCar(self, direction):
        self.direction = direction
        print 'Car is moving towards {} direction'.format(direction)

audi = Car() # Audi is an object of Car class
merc = Car() # Merc

audi.moveCar('right')
merc.moveCar(direction='left')

Car.myCarGearType('Manual')
audi.myCarGearType(audi.steeringType)
merc.myCarGearType(merc.steeringType)
