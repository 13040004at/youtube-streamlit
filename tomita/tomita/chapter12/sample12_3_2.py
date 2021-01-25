import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

datein = input('入力してください：')

try:
    dt = datetime.datetime.strptime(datein, '%Y/%m/%d')
    print(dt.strftime('入力された日は%Aです'))
except ValueError as ex:
    print('入力された月日が正しくありません')