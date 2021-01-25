class Person:
    def __init__(self, name):
        self.__name = name

    def greet(self):
        print('Hello, my name is ' + self.__name)

    @property
    def name(self):
        print('name getter')
        return self.__name

    @name.setter
    def name(self, name):
        print('name setter')
        if name == '':
            raise ValueError('name is empty')
        self.__name = name