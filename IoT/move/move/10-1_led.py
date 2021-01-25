# -*- coding:utf-8 -*-

# LEDランプを5回点灯させるプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN = 18

# GPIOピンの初期化
#GPIO.cleanup()

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4番を出力として使用
GPIO.setup(PIN, GPIO.OUT)

# LEDランプ5回点灯
#for i in range(5):

while(True):
    # 点灯
    GPIO.output(PIN,True)
    time.sleep(1)

    # 消灯
    GPIO.output(PIN,False)
    time.sleep(1)

