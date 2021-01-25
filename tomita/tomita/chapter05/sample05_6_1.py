def func2(l):
    return l[1] + l[2]

def func1(x,y):
    func2([x,y])

func1(1,2)
print('end')