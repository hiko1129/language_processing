"""09. Typoglycemia."""
import random
'''スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文
（例えば"I couldn't believe that I could actually understand
 what I was reading : the phenomenal power of the human mind ."）を与え，
 その実行結果を確認せよ.'''
str = "I couldn't believe that I could actually understand" \
      " what I was reading : the phenomenal power of the human mind ."

words_list = str.split(' ')
result = []
for word in words_list:
    if len(word) > 4:
        char_list = list(word)
        temp_list = char_list[1:-1]
        random.shuffle(temp_list)
        shuffled_word = ''.join(temp_list)
        word = char_list[0] + shuffled_word + \
            char_list[-1]
    result.append(word)

print(' '.join(result))
