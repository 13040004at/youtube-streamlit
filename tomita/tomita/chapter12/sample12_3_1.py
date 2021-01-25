import os
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')

today = datetime.datetime.today()
filename = today.strftime('%Y%m%d')

if os.path.exists(filename) :
        print('ディレクトリはすでに存在します')

else:
        print(filename)

