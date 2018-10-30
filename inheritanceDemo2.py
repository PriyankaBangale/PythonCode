class Trip:
    '''This class describes a Trip.'''
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday
        

class Cruise(Trip):
    def __init__(self,ship=None,departday=None,arriveday=None):
        self.ship = ship
        Trip.__init__(self, departday=departday, arriveday=arriveday)
        
    def print_schedule(self):
        print("Cruise {} to {}".format(self.departday,self.arriveday))


class Flight(Trip):
    def __init__(self,plane=None,departday=None,arriveday=None):
        self.plane = plane
        self.departday = departday
        self.arriveday = arriveday
        
    def print_arrival(self):
        print("Flight arrives on {}".format(self.arriveday))        

        
if __name__ == '__main__':
    voyage = Cruise(departday = 'Friday', arriveday = 'Monday', ship='Sea Breeze')
    print(voyage.departday)
    print(voyage.arriveday)
    print(voyage.ship)

    voyage.print_schedule()

    print("*"*50)
    
    flthome = Flight(departday = 'Monday', arriveday = 'Monday', plane = 'CRJ')
    print(flthome.departday)
    print(flthome.arriveday)
    print(flthome.plane)
    
    flthome.print_arrival()