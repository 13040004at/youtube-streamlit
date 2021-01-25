def mul(x,*args):
    a = x
    for b in args:
        a = x * b
        x = a
    return a

print(mul(1,2))
print(mul(2,4,6))
print(mul(3,5,7,11))

