"""04. 元素記号."""
from collections import OrderedDict
'''"Hi He Lied Because Boron Could Not Oxidize Fluorine.
 New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．'''
str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.' \
      ' New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
index_list = [0, 4, 5, 6, 7, 8, 15, 15, 18]
words_list = str.split(' ')

dictionary = OrderedDict()
for i, word in enumerate(words_list):
    real_index = i + 1
    if i in index_list:
        dictionary[word[0]] = real_index
    else:
        dictionary[word[0:2]] = real_index
print(dictionary)
