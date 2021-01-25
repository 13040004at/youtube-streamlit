from chapter07.sample07_6_2 import Car

class Truck(Car):
    def __init__(self,seats,max_speed,capacity):
        super().__init__(seats,max_speed)
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    def __eq__(self,other):
        if not isinstance(other,Car):
            return False
        return self.seats == other.seats and self.max_speed == other.max_speed


car = Car(4,100)
truck = Truck(4,100,500)
print(car == truck)