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

# GPIOピンの初期化
GPIO.cleanup()

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの14番を入力として使用
GPIO.setup(PIN, GPIO.IN)

# センサーが感知されるまで1秒ずつチェック(無限ループ)
while True:
    if (GPIO.input(PIN) == GPIO.HIGH):
        print("センサーが人間を感知しました")
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

# 受講生ディレクトリ
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
MESSAGE = "防犯システムが作動しました。写真URL: http://" + HOST + "/~students/" + students_dir + "/" + server_filename

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
mail_to = "at460904@i.softbank.jp"

# メール送信元
mail_from = "students@wincloud.site"

# 件名
subject = "防犯システムが作動しました"

# 本文
body = "下記URLから写真を確認してください。\n"
body = body + "http://" + HOST + "/~students/" + students_dir + "/" + server_filename

# テキストのみのメール作成
msg = MIMEText(body, "plain")

# メールヘッダーに設定
msg["From"] = mail_from
msg["To"] = mail_to
msg["Date"] = formatdate()
msg["Subject"] = subject

# smtpサーバーから送信
smtp_obj = smtplib.SMTP(SMTP_SERVER, PORT_NUMBER)
smtp_obj.ehlo()
smtp_obj.login("students", "wnstudents")
smtp_obj.sendmail(mail_from, mail_to, msg.as_string())
smtp_obj.close()

