"""15. 末尾のN行を出力."""
import sys
import os
'''自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．'''

path = './assets/hightemp.txt'
num_of_lines = int(sys.argv[1])
with open(path) as f:
    lines = f.readlines()
lines_maximum = len(lines)
for i in range(lines_maximum - num_of_lines, lines_maximum):
    print(lines[i], end='')

print()
#コマンドバージョン
os.system('tail -n 10 {0}'.format(path))
