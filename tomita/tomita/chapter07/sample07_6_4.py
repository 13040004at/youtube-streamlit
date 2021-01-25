class Car:
    def __init__(self,seats,max_speed):
        self.seats = seats
        self.max_speed = max_speed

    def spec(self):
        print('Seats: ' + str(self.seats) + ', Max speed: ' + str(self.max_speed))

    def __eq__(self,other):
        if not isinstance(other,Car):
            return False
        return self.seats == other.seats and self.max_speed == other.max_speed

car1 = Car(4,100)
car2 = Car(4,100)
print(car1 == car2)

