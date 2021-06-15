import sys
sys.stdin = open("ex_078_input.txt")

def longword(words):
    long_word = ''
    for word in words:
        if len(word) > len(long_word):
            long_word = word
    return long_word

words = input().split(', d')

print(longword(words))