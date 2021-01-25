# -*- coding:utf-8 -*-

# LEDランプを5回点灯させるプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOピン番号
switch_pin = 18
led_pin = 23

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

led_state = False
old_input_state = True # pulled-up

while True:
    new_input_state = GPIO.input(switch_pin)
    if new_input_state == False and old_input_state == True:
        led_state = not led_state
    old_input_state = new_input_state
    GPIO.output(led_pin, led_state)

