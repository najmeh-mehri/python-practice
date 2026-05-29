'''
Remove duplicates in a row and spaces from input string.
'''
word = input()
n=""
punc=' '
for i in range(len(word)):
    if word[i] != word[i-1]:
        n = n + word[i]
for i in n:
    if i not in punc:
        print(i,end='')