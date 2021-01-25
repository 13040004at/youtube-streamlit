x= ['一万円札','五千円札', '千円札', '五百円玉', '百円玉', '五十円玉', '十円玉', '五円玉', '一円玉']
y =[10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

a = int(input('金額を入力してください: '))
print('金額: ', str(a),'円')

for i, j in zip(x, y):
    if a > j:
        maisu = a // j
        print(i,'= ',str(maisu),'枚')
        amari = a - (maisu * j)
        a = amari

    elif a == 0:
        break

