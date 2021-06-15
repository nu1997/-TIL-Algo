import sys
sys.stdin = open("ex_070_input.txt")

word_list = list(map(str, input().split()))
new_list = sorted(list(set(word_list)))
print(','.join(new_list))
