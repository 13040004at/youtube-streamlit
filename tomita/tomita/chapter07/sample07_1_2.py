class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello, my name is ' + self.name)

    def __eq__(self,other):
        if not isinstance(other,Person):
            return False
        return self.name == other.name and self.age == other.age


