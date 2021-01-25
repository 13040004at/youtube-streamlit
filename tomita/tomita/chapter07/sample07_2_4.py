import math

class Circle:
    def __init__(self , radius):
        self.radius = radius

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2