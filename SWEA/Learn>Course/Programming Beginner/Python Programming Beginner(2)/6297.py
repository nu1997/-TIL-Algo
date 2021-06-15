import sys
sys.stdin = open("ex_075_input.txt")

num_list = list(map(int, input().split(', ')))

odd_list = [str(i) for i in num_list if i % 2 != 0]
print(', '.join(odd_list))