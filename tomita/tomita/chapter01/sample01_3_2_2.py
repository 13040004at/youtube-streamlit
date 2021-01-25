import random

# おみくじの候補をリクエストで定義
FORTUNE_CANDIDATES = ['大吉','中吉','小吉','吉','末吉','凶','大凶']

# 乱数の最大値を設定
fortune_max = len(FORTUNE_CANDIDATES) - 1

# 0～設定された最大値までの乱数を取得
fortune = random.randint(0,fortune_max)

# 乱数の番号のリスト項目を表示
print(FORTUNE_CANDIDATES[fortune])
