"""14. 先頭からN行を出力."""
import os
import sys
'''自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．'''

path = './assets/hightemp.txt'
num_of_lines = int(sys.argv[1])
with open(path) as f:
    for i in range(num_of_lines):
        print(f.readline(), end='')

print()
#コマンドバージョン
os.system('head -n 10 {0}'.format(path))
