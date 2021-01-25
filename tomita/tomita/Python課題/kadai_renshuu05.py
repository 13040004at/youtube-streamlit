a = int(input('255以下の10進数を入力してください'))

if  a > 255:
    print('255より大きい数字を入力しています。')

else:

    l1 = [128, 64, 32, 16, 8, 4, 2, 1]



    for i in l1:
        b = a // i
        print(b, end='')


        c = a - (b * i)
        a = c





