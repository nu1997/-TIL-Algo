import sys
sys.stdin = open("ex_068_input.txt")

word_list = list(map(str, input().split(', ')))
sorted_list = sorted(word_list)

print(', '.join(sorted_list))