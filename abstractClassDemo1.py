from abc import ABCMeta, abstractmethod

class Trip(metaclass=ABCMeta):
    @abstractmethod
    def show_msg(self):
        pass

class Cruise(Trip):
   #def show_msg(self):
        print('Abstract Method')

if __name__ == '__main__':
    night_trip = Cruise()
    night_trip.show_msg()
