class Car:
    def __init__(self,seats,max_speed):
        self.__seats = seats
        self.__max_speed = max_speed

    @property
    def seats(self):
        return self.__seats

    @property
    def max_speed(self):
        return self.__max_speed

    def spec(self):
        print('Seats: ' + str(self.seats) + ', Max speed: ' + str(self.max_speed))

car = Car(4,100)
#print(car.seats)
#print(car.max_speed)

