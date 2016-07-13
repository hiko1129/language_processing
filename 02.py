"""02. 「パトカー」＋「タクシー」＝「パタトクカシーー」."""
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ.
str1 = 'パトカー'
str2 = 'タクシー'
answer = ''
for char1, char2 in zip(str1, str2):
    answer += char1 + char2
print(answer)
