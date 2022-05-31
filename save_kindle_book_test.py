import pyautogui
import time
import os
import datetime

page = int(input("おおよその本ページ数を入力して下さい："))
print(str(page) + "で設定しました。")
direction = str(input("本のページ移動する時の向きを英語で入力して下さい(入力例 right or left):"))
print(direction + "で設定しました")

# スクショ間隔(秒)
span = 1
# 出力フォルダ頭文字
h_foldername = "output"
# 出力ファイル頭文字
h_filename = "picture"


# ５秒の間に、スクショしたいkindleの画面に移動
time.sleep(5)

# 出力フォルダ作成(フォルダ名：頭文字_年月日時分秒)
folder_name = h_foldername + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
os.mkdir(folder_name)

# スクショ処理
for p in range(page):
    # 出力ファイル名(頭文字_連番.png)
    out_filename = h_filename + "_" + str(p+1).zfill(4) + '.png'
    # 画面全体のスクリーンショット
    s = pyautogui.screenshot()
    # 出力パス： 出力フォルダ名 / 出力ファイル名
    s.save(folder_name + "/" + out_filename)
    # 次のページ
    #pyautogui.keyDown('left')
    pyautogui.keyDown(direction)
    # 画面の動作待ち
    time.sleep(span)
