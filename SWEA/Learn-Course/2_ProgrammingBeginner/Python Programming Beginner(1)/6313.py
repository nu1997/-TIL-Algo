import sys
sys.stdin = open("ex_060_input.txt")

# Ascii  불러오는 ord 아니면 chr

n = int(input())
word = chr(n)

print(f'ASCII {n} => {word}')