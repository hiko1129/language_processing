"""08. 暗号文."""
'''与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．'''

str = 'Change before you have to.'


def cipher(input_text):
    """与えられた文字列の暗号化・復号化を行う."""
    result = ''
    for word in input_text:
        result += chr(219 - ord(word)) if word.islower() else word
    return result

cryptogram = cipher(str)
print(cryptogram)
print(cipher(cryptogram))
