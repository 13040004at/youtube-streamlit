# -*- coding:utf-8 -*-

# 音声出力後、LEDランプを5回点灯させるプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time
import subprocess

# 音声ファイル名
wavfile = "/home/pi/first.wav"

# aplayコマンド
aplay_command = "aplay " + wavfile

# aplayコマンドの実行
subprocess.call(aplay_command, shell=True)

# GPIOピン番号
PIN = 4

# GPIOピンの初期化
GPIO.cleanup()

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4番を出力として使用
GPIO.setup(PIN, GPIO.OUT)

# LEDランプ5回点灯
for i in range(10):
    # 点灯
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(3.0)

    # 消灯
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(1.0)
print(time.ctime())