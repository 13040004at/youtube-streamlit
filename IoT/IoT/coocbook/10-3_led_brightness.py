# -*- coding:utf-8 -*-

# LEDランプを5回点灯させるプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN = 18

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4番を出力として使用
GPIO.setup(PIN, GPIO.OUT)

pwm_led = GPIO.PWM(PIN, 500)
pwm_led.start(100)


try:
    while(True):
        duty_s = input("Enter Brightness(0 to 100):")
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
finally:
        print("Cleaning Up!")
        GPIO.cleanup()



