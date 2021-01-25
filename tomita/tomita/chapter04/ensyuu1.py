prob = 35
money = 6000

if prob >= 80:
    print('天気が悪いので今日は家で過ごしましょう')

elif prob >= 40 and money >= 5000:
    print('雨が降りそうなので今日は映画を見に行きましょう')

elif prob < 40 and money >= 5000:
    print('天気がいいので今日は遠出しましょう')

elif prob < 40 and money < 5000:
    print('今日は近場で遊びましょう')