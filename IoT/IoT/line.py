# -*- coding:utf-8 -*-

# LINE Notifyの通知コマンドを実行

# ライブラリのインポート
import subprocess

# トークン
ACCESS_TOKEN = "GFpPVFIUJLKZVoUv7JEdxaZIogAdn5KJtPk2LYrFHKW"

# メッセージ
MESSAGE = "こんにちは"

# 通知コマンド
command = "curl"
command = command + " -X POST"
command = command + " -H 'Authorization: Bearer " + ACCESS_TOKEN + "'"
command = command + " -F 'message=" + MESSAGE + "'"
command = command + " https://notify-api.line.me/api/notify"

#　コマンド実行
subprocess.call(command, shell=True)

