def func(a=0,**kwargs):
    print('a:',a)
    print('kwargs:',kwargs)

func()
func(a=1,b=2)
func(a=1,b=2,c=3,d=4)