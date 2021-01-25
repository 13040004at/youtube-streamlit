f = open('sample11_1_1.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(repr(line))
f.close()