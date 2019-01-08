#!/usr/bin/python3.6

import sys
import random
import os
from datetime import datetime

#引数に読み込むファイルを指定してオープン
f = open(sys.argv[1], "r",encoding="utf-8")

#while実行前に定義、この時点でファイルの1行目を読み込み
line = f.readline()

#whileで読み込んだ行を格納するリストを準備
lines=[]

#引数ファイルを１行ずつ読み込んでリストに格納
while line:
    lines.append(line)
    line = f.readline()

#ファイルクローズ
f.close()

#おみくじの結果を格納したリストからランダムで１行をチョイス
kekka = random.choice(lines)

#ランダムでチョイスした１行（文字列）をカンマ区切りでリストに変換
kekkaList = kekka.split(',')

#出力するファイル名に付与する日付を取得
hizuke = datetime.now().strftime("%Y-%m-%d")

#出力ファイル名を指定
wfilename = "omikuji_{0}.txt".format(hizuke)

#出力ファイルと同じ名前のファイルが存在する場合はエラーを出力
#if os.path.isfile(wfilename):
#    sys.stderr.write('エラー:ファイルが既に存在しています。\n')

#出力ファイル名でファイルオープンし結果を書き込み
f = open(wfilename,'w')
f.write("===============================\n")
for i in kekkaList:
    f.write(i)
    f.write("\n")
f.write(hizuke)
f.write("\n")
f.write("===============================\n")
f.close()

print("おみくじの結果を{0}に書込みました！".format(wfilename))
