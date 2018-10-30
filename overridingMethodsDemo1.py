class Trip:
    '''This class describes a Trip.'''
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday

    def print_departure(self):
        print("Trip Leaves on {}".format(self.departday))
        

class Cruise(Trip):
    def print_departure(self):
        print("Cruise {} to {}".format(self.departday, self.arriveday))


if __name__ == '__main__':
    print(Trip.__doc__)
    vacation = Trip(departday='Sunday', arriveday='Monday')
    vacation.print_departure()
    print("*"*50)

    day1 = Cruise(departday='Monday', arriveday='Monday')
    day1.print_departure()
    print("*"*50)
    
    day2 = Cruise(departday='Tuesday', arriveday='Tuesday')
    day2.print_departure()
    print("*"*50)
    
    plans = [vacation, day1, day2]
    for plan in plans:
        plan.print_departure()