class Duck:
    def cry(self):
        return 'quack'

class Cat:
    def cry(self):
        return 'quack'

def duck_check(something):
    if something.cry() == 'quack':
        print('something is duck')

duck_check(Duck())
duck_check(Cat())
