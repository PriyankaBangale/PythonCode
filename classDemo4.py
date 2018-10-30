class Cruise:
    '''This class describes a cruise.'''
    def __init__(self, ship=None, balance=0.0, cabin=0):
        '''Constructor Method'''
        self.ship = ship
        self.balance = balance
        self.cabin = cabin
        
    #Class Variable
    discountcabins = (101,102,105,106,109,110)

    def discount(self):
        if self.cabin in Cruise.discountcabins:
            self.balance -= 50.0
        
if __name__ == '__main__':
    #Creating an object1
    myVacation = Cruise(ship='Voyager',cabin=101)

    print(myVacation.ship)
    print(myVacation.balance)
    print(myVacation.cabin)
    
    #Accessing the Class Variable
    print(Cruise.discountcabins)

    #Creating an object2
    yourVacation = Cruise(ship='Sundowner',balance=157.50, cabin=511)

    #Calling object's method
    myVacation.discount()
    yourVacation.discount()

    print(myVacation.balance)
    print(yourVacation.balance)