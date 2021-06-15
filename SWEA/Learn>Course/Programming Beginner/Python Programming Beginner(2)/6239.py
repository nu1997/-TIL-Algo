import sys
sys.stdin = open("ex_042_input.txt")

word_list = list(map(str, input().split()))
print(' '.join(word_list[::-1]))