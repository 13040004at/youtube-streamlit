# -*- coding:utf-8 -*-

# ライブラリのインポート
from tkinter import *
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN = 18

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)
# GPIOの18番を出力として使用
GPIO.setup(PIN, GPIO.OUT)

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.check_var = BooleanVar()
        check = Checkbutton(frame, text='PIN 18',
                            command = self.update,
                            variable=self.check_var, onvalue=True, offvalue=False)
        check.grid(row=1)

    def update(self):
        GPIO.output(PIN, self.check_var.get())


root = Tk()
root.wm_title('On / Off Switch')
app = App(root)
root.geometry("200×50+0+0")
root.mainloop()