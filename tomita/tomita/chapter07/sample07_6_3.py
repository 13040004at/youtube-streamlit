from chapter07.sample07_6_2 import Car

class Truck(Car):
    def __init__(self,seats,max_speed,capacity):
        super().__init__(seats,max_speed)
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    def spec(self):
        print('Seats: ' + str(self.seats) + ' , Max speed: ' + str(self.max_speed) + ' , Capacity: ' + str(self.capacity))

truck = Truck(4,100,500)
truck.spec()