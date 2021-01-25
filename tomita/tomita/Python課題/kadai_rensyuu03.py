Tl = float(input('身長をm単位で入力してください >'))
Wt = float(input('体重をkg単位で入力してください >'))
a = (Wt / (Tl ** 2))
print('BMI = ',str(a))

if a < 18.5:
    print('やせ')

elif 18.5 <= a and a < 25:
    print('標準')

elif 25 <= a and a <30:
    print('肥満')

else:
    print('高度肥満')



