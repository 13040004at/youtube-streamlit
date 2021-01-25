# coding: utf-8

# 乱数機能の利用
import random

# 0～2の乱数を発生させる
# 発生した乱数を変数fortuneに代入する
fortune = random.randint(0,4)

# 変数の値(発生した乱数)に応じて大吉、中吉、小吉を表示
if fortune == 0:
    print('大吉')
elif fortune == 1:
    print('中吉')
elif fortune == 2:
    print('小吉')
elif fortune == 3:
    print('凶')
elif fortune == 4:
    print('大凶')
