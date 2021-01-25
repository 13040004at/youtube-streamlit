class Car:
    def __init__(self,seats,max_speed):
        self.seats = seats
        self.max_speed = max_speed

    def spec(self):
        print('Seats: ' + str(self.seats) + ', Max speed: ' + str(self.max_speed))

#car = Car(4,100)
#car.spec()
