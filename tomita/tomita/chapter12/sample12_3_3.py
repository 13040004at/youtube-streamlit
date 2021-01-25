import datetime
import locale

locale.setlocale(locale.LC_ALL, '')
datein = input('入力してください：')

try:
    dt = datetime.datetime.strptime(datein, '%Y/%m/%d')
    TwoWeekAfter = dt + datetime.timedelta(weeks=2)
    print(TwoWeekAfter.strftime('入力された日付の2週間後は %Y/%m/%d です'))

except ValueError as ex:
    print('入力された月日が正しくありません')