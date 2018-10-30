#Child Class has no Constructor Method

class Trip:
    '''This class describes a Trip.'''
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday

    def print_departure(self):
        print("Trip leaves on {}".format(self.departday))


class Cruise(Trip):
    '''Child Class Cruise inherting its properties from parent class Trip'''
    def print_schedule(self):
        print("Cruise {} to {}".format(self.departday,self.arriveday))


class Flight(Trip):
    '''Child Class Flight inherting its properties from parent class Trip'''
    def print_arrival(self):
        print("Flight arrives on {}".format(self.arriveday))
        
if __name__ == '__main__':
    #Cruise class object
    voyage = Cruise(departday='Friday', arriveday='Monday')
    print(voyage.departday)
    print(voyage.arriveday)
    
    voyage.print_departure()
    voyage.print_schedule()

    print("*"*50)

    flthome = Flight(departday='Monday', arriveday='Monday')
    print(flthome.departday)
    print(flthome.arriveday)
    
    flthome.print_departure()
    flthome.print_arrival()