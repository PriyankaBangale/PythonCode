class Cruise:
    '''This class describes a cruise.'''
    def __init__(self, ship=None, balance=0.0, cabin=0):
        '''Constructor Method'''
        self.ship = ship
        self.balance = balance
        self.cabin = cabin

    def dine(self, amount):
        self.balance += amount
        return self.balance

if __name__ == '__main__':
    #Creating an instance of class Cruise
    myVacation = Cruise(ship='Voyager',cabin=101)
    yourVacation = Cruise(ship='Sundowner',balance=157.50, cabin=511)

    #Calling Object Methods
    print(myVacation.dine(125.0))
    print(yourVacation.dine(215.50))