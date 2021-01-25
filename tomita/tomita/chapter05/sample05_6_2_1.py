def func2(l):
    return l[1] + l[2]

def func1(x):
    try:
        func2([x])
    except:
        print('exception occurrred')

func1(1)
print('end')