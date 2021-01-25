total = 0

with open('sample11_6_1.txt', 'r') as f:

    for line in f:
        i = int(line)
        total += i


print(total)
