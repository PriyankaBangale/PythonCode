class Trip:
    '''This class describes a Trip.'''
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday

    def print_trip(self):
        print("Schedule is {} {}".format(self.departday, self.arriveday))
        

class Cruise(Trip):
    def __init__(self, ship=None, departday=None, arriveday=None):
        self.ship = ship
        self.departday = departday
        self.arriveday = arriveday
        
    def print_trip(self):
        #Call parent class method using super()
        super(Cruise, self).print_trip()
        print("Ship is {}".format(self.ship))

class Flight(Trip):
    def __init__(self, plane=None, departday=None, arriveday=None):
        self.plane = plane
        self.departday = departday
        self.arriveday = arriveday

    def print_trip(self):
        super(Flight, self).print_trip()
        print("Plane is {}".format(self.plane))

        
if __name__ == '__main__':
    travels = [Cruise(departday='Friday', arriveday='Saturday', ship='Moonbeam'),
               Flight(departday='Wednesday', arriveday='Friday', plane='CRJ')]

    for travel in travels:
        travel.print_trip()
        print("*"*50)
