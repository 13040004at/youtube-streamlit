def func(a,b):
    if a > b:
        return a - b
    else:
        return b - a

result = []
for a in range(0,3):
    for b in range(0,3):
        result.append(func(a,b))