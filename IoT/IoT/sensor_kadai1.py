# -*- coding:utf-8 -*-

# 人体を感知したら、メッセージを表示するプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN04 = 4

# GPIOピン番号
PIN10 = 10

# GPIOピンの初期化
GPIO.cleanup()

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4番を入力として使用
GPIO.setup(PIN04, GPIO.IN)

# GPIOの10番を入力として使用
GPIO.setup(PIN10, GPIO.OUT)

# 1分間1秒ずつチェックしてメッセージを表示
for i in range(1, 61):
    if(GPIO.input(PIN04) == GPIO.HIGH):
        print("人体を感知しました")
        GPIO.output(PIN10, GPIO.HIGH)
        time.sleep(1)



    else:
        print("人体を感知していません")
        # 消灯
        GPIO.output(PIN10, GPIO.LOW)
        time.sleep(1)

    time.sleep(1)