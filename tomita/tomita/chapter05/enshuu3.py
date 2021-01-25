def power(a):
    def inner(x):
        return x ** a
    return inner

power3 = power(3)
power4 = power(4)

print(power3(2))
print(power4(3))