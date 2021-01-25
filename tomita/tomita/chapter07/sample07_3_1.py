class Sample:
    count = 0

    def __init__(self):
        self.__class__.count += 1

    @classmethod
    def info(cls):
        print('There are ' + str(cls.count) + ' instances')

s1 = Sample()
s2 = Sample()
Sample.info()

s3 = Sample()
Sample.info()