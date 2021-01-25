class Sample:
    def __init__(self, name):
        self.name = name

    def __call__(self, num):
        print('Sample.__call__: ' + self.name + ': ' + str(num))

def normal_func(num):
    print('normal_func: ' + str(num))

def output(func):
    func(123)

sample1 = Sample('sample1')
sample2 = Sample('sample2')

output(normal_func)
output(sample1)
output(sample2)