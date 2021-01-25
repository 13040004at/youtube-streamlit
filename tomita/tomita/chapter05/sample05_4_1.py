def func():
    def inner(a):
        print('a:',a)
        print('a ** 2:',a ** 2)
        print('a ** 3:',a ** 3)

    inner(2)
    inner(3)

func()