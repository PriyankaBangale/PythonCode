class Cruise:
    '''This class describes a cruise.'''
    def __init__(self, ship=None, balance=0.0, cabin=0):
        print("Constructor Method")
        self.ship = ship
        self.balance = balance
        self.cabin = cabin


if __name__ == '__main__':
    cruiseObj = Cruise()
    print(cruiseObj.ship)
    print(cruiseObj.balance)
    print(cruiseObj.cabin)

    #Encapsulation
    
    myVacation = Cruise(ship='Voyager',cabin=101)
    print(myVacation.ship)
    print(myVacation.balance)
    print(myVacation.cabin)

    yourVacation = Cruise(ship='Sundowner',balance=157.50, cabin=511)
    print(yourVacation.ship)
    print(yourVacation.balance)
    print(yourVacation.cabin)

    #Modifying Instance Attributes
    yourVacation.balance = 400.0
    yourVacation.cabin = 104

    print(yourVacation.balance)
    print(yourVacation.cabin)