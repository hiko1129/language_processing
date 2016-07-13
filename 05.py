"""05. n-gram."""
'''与えられたシーケンス（文字列やリストなど）から
n-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から
単語bi-gram，文字bi-gramを得よ．'''
str = 'I am an NLPer'


def n_gram(input, n):
    """n-gram."""
    last = len(input) - (n - 1)
    result = []
    for i in range(0, last):
        result.append(input[i:i+n])
    return result

print(n_gram(str, 2))
print(n_gram(str.split(' '), 2))
