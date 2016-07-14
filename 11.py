"""11. タブをスペースに置換."""
import os
'''タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ.'''

with open('./assets/hightemp.txt') as file:
    str = file.read()
print(str.replace('\t', ' '))

#コマンドバージョン
os.system("cat ./assets/hightemp.txt | tr '\t' ' '")
