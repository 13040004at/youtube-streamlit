# -*- coding:utf-8 -*-

# 防犯システムプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time
import subprocess
import pexpect
import smtplib
from email import encoders
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# GPIOピン番号
PIN = 14
PIN2 = 4

# GPIOピンの初期化
GPIO.cleanup()

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの14番を入力として使用
GPIO.setup(PIN, GPIO.IN)

# GPIOの4番を出力として使用
GPIO.setup(PIN2, GPIO.OUT)


# センサーが感知されるまで1秒ずつチェック(無限ループ）
while True:
    if (GPIO.input(PIN) == GPIO.HIGH):
        print("センサーが人間を感知しました")
        # 点灯
        GPIO.output(PIN2, GPIO.HIGH)
        time.sleep(1)
        break

    print("センサー感知中")
    time.sleep(1)

# 写真を撮影する
image_file = "/home/pi/capture.jpg"

# 撮影コマンド
image_command = "raspistill -t 1000 -q 10 -o " + image_file

# コマンド実行
subprocess.call(image_command, shell=True)

# アラーム音ファイル
wavfile = "/home/pi/alert.wav"

# aplayコマンド
command = "aplay " + wavfile

# コマンド実行
subprocess.call(command, shell=True)

# 音声ファイル名
wavfile = "/home/pi/security.wav"

# aplayコマンド
command = "aplay " + wavfile

# コマンド実行
subprocess.call(command, shell=True)

# サーバー設定
ID = 'students'
PASSWORD = 'winstudents'
HOST = 'www.wincloud.site'
DIR = 'public_html'

# 受講生ディレクトリ(ご自身の受講番号に変更してください)
students_dir = 'KRAa055PY14/images'

# ローカルのファイル名
local_filename = 'capture.jpg'

# ファイル名
server_filename = 'capture.jpg'

# scpコマンド
scp_command = 'scp ' + local_filename
scp_command = scp_command + ' ' + ID + '@' + HOST + ':' + DIR + '/' + students_dir + '/' + server_filename

# コマンド実行
command = pexpect.spawn(scp_command)
command.expect('(?i)password')
command.sendline(PASSWORD)
command.expect(pexpect.EOF)

# LineNotifyトークン
ACCESS_TOKEN = "GFpPVFIUJLKZVoUv7JEdxaZIogAdn5KJtPk2LYrFHKW"

# メッセージ
MESSAGE = "防犯システムが作動しました。写真URL：http://" + HOST + "/~students/" + students_dir + "/" + server_filename

# 通知コマンド
command = "curl"
command = command + " -X POST"
command = command + " -H 'Authorization: Bearer " + ACCESS_TOKEN + "'"
command = command + " -F 'message=" + MESSAGE + "'"
command = command + " https://notify-api.line.me/api/notify"

# コマンド実行
subprocess.call(command, shell=True)

# SMTPサーバー設定
SMTP_SERVER = "www.wincloud.site"
PORT_NUMBER = 587

# メール送信先
mail_to="at460904@i.softbank.jp"

# メール送信元
mail_from = "students@wincloud.site"

# 件名
subject = "防犯システムが作動しました"

# 本文
body = "下記のURLから写真を確認してください。\n"
body = body + "http://"  + HOST + "/~students/" + students_dir + "/" + server_filename

# テキストのみのメール作成
msg = MIMEText(body, "plain")

# メールヘッダーに設定
msg["From"] = mail_from
msg["To"] = mail_to
msg["Date"] = formatdate()
msg["Subject"] = subject

# smptサーバーから送信 
smtp_obj = smtplib.SMTP(SMTP_SERVER, PORT_NUMBER)
smtp_obj.ehlo()
smtp_obj.login("students", "winstudents")
smtp_obj.sendmail(mail_from, mail_to, msg.as_string())
smtp_obj.close()


# _____ _____ _____ __ __ _____ _____
# |     |   __|     |  |  |     |     |
# |  |  |__   |  |  |_   _|  |  |  |  |
# |_____|_____|_____| |_| |_____|_____|
#
# Project Tutorial Url:http://osoyoo.com/?p=1031
#
import smbus
import time

# Define some device parameters
I2C_ADDR = 0x3f  # I2C device address, if any error, change this address to 0x27
LCD_WIDTH = 16  # Maximum characters per line

# Define some device constants
LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94  # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4  # LCD RAM address for the 4th line

LCD_BACKLIGHT = 0x08  # On
# LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100  # Enable bit

# Timing constants
E_PULSE = 0.001
E_DELAY = 0.001

# Open I2C interface
# bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1


def lcd_init():
    # Initialise display
    lcd_byte(0x33, LCD_CMD)  # 110011 Initialise
    lcd_byte(0x32, LCD_CMD)  # 110010 Initialise
    lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28, LCD_CMD)  # 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
    time.sleep(E_DELAY)


def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = the data
    # mode = 1 for data
    #        0 for command

    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    # High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)


def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)


def lcd_string(message, line):
    # Send string to display

    message = message.ljust(LCD_WIDTH, " ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)


def main():
    # Main program block

    # Initialise display
    lcd_init()

    while True:
        # Send some test
        lcd_string("alert!          ", LCD_LINE_1)
        

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)
        
# 消灯
GPIO.output(PIN2, GPIO.LOW)
time.sleep(1)

