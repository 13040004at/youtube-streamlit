# -*- coding:utf-8 -*-

# メール送信プログラム

# ライブラリのインポート
import subprocess
import pexpect
import smtplib
from email import encoders
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
#body = body + "http://"  + HOST + "/~students/" + students_dir + "/" + server_filename

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