def adder(a):
    return lambda x: x + a

a = adder(3)
b = adder(5)

print(a(10))
print(b(10))