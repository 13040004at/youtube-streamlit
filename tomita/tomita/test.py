class Person:
    def __init__(self, name):
        self.__name = name

    def greet(self):
        print('Hello, my name is ' + self.__name)
