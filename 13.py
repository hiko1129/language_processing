"""13. col1.txtとcol2.txtをマージ."""
import os
'''12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．'''

directory_path = './assets/'
file1 = directory_path + 'col1.txt'
file2 = directory_path + 'col2.txt'
new_file = directory_path + 'col1+col2.txt'

with open(file1) as f1, open(file2) as f2:
    file1_lines, file2_lines = f1.readlines(), f2.readlines()

with open(new_file, 'w') as n_f:
    for line1, line2 in zip(file1_lines, file2_lines):
        n_f.write("\t".join([line1.rstrip(), line2]))

#コマンドバージョン
os.system('paste -d"\t" {0} {1}'.format(file1, file2))
