def func(*args,**kwargs):
    print('args:',args)
    print('kwargs:',kwargs)

func()
func(a=1,b=2)
func(1,2,a=3,b=4)