a = 0

while True:
    try:
        s = input('Please input number:')
        num = int(s)
        b = a + num
        print(str(a)  + '+' + str(num) + '=>' + str(b))
        a = b

    except ValueError as ex:
        print('Not a number is inputted. Program exit.')
        break