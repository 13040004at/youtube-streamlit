class Person:
    def __init__(self,name):
        print('Person.__init__')
        self.name = name

class Employee(Person):
    def __init__(self,name,number):
        print('Employee.__init__')
        super().__init__(name)
        self.number = number
