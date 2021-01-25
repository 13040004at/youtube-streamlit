# -*- coding:utf-8 -*-

# 撮影した画像にスケッチ風のエフェクトがかかり、ディスプレイに撮影した画像を表示させるプログラム

# ライブラリのインポート
import subprocess

# 画像ファイル名
image_file = "/home/pi/effect.jpg"

# 撮影コマンド
command = "raspistill -o " + image_file

# エフェクト方法(今回はスケッチ風に)
command = command + " -ifx sketch"

# コマンド実行
subprocess.call(command, shell=True)

# 画面表示コマンド
command = "gpicview " + image_file

# コマンド実行
subprocess.call(command, shell=True)