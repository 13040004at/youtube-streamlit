def speed(t1,x1,t2,x2):
    dt = t2 - t1
    dx = x2 - x1
    if dt == 0 and dx != 0:
        raise ValueError('dt is 0,but dx is not 0')
    return dx / dt

print(speed(1,1,4,10))
print(speed(1,1,1,10))