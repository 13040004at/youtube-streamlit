# -*- coding:utf-8 -*-

# 撮影した画像にスケッチ風のエフェクトがかかり、ディスプレイに撮影した画像を表示させるプログラム

# ライブラリのインポート
import subprocess

# 画像ファイル名
image_file = "/home/pi/shutter.jpg"

# 音声ファイル名
wavfile = "/home/pi/shutter.wav"

# 撮影コマンド
command = "raspistill -o " + image_file

# コマンド実行
subprocess.call(command, shell=True)

# aplayコマンド
aplay_command = "aplay" + wavfile

# aplayコマンドの実行
subprocess.call(aplay_command, shell=True)


# 画面表示コマンド
command = "gpicview " + image_file

# コマンド実行
subprocess.call(command, shell=True)