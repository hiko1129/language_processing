"""12. 1列目をcol1.txtに，2列目をcol2.txtに保存."""
import os
'''各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．'''

temp_path = './assets/hightemp.txt'

with open(temp_path) as file:
    lines = file.readlines()


def write_txt(input_col, filename):
    """テキストファイルに書き込む."""
    with open("./assets/{0}".format(filename), 'w') as file:
        file.writelines(input_col)

prefectures, cities = [], []
for line in lines:
    temperature_data = line.split()
    prefectures.append(temperature_data[0] + "\n")
    cities.append(temperature_data[1] + "\n")

write_txt(prefectures, 'col1.txt')
write_txt(cities, 'col2.txt')

#コマンドバージョン
os.system("cut -f1,2 {0}".format(temp_path))
