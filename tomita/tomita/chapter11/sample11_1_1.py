f = open('sample11_1_1.txt', 'a')
f.write('Hello\n')
print('Goodbye', file=f)
f.close()