"""06. 集合."""
'''"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．'''
str1 = 'paraparaparadise'
str2 = 'paragraph'
search_word = 'se'


def n_gram(input, n):
    """n-gram."""
    last = len(input) - (n - 1)
    result = []
    for i in range(0, last):
        result.append(input[i:i+n])
    return result

X = set(n_gram(str1, 2))
Y = set(n_gram(str2, 2))

print(X.union(Y))  #和集合
print(X.intersection(Y))  #積集合
print(X.difference(Y))  #差集合
print(search_word in X)  # seが含まれているか否か
print(search_word in Y)
