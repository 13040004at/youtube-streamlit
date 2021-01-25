def deco(func):
    def wrapper(*args,**kwargs):
        print('*args:',args)
        print('**kwargs:',kwargs)
        result = func(*args,**kwargs)
        print('result:',result)
        return result
    return wrapper

@deco
def add(a,b):
    return a + b

add(10,20)
add(b=30,a=40)