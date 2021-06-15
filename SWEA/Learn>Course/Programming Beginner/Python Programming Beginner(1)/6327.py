import sys
sys.stdin = open("ex_077_input.txt")

def calc_square(n):
    return n ** 2

num_list = list(map(int, input().split(',')))

for i in num_list:
    print(f'square({i}) => {calc_square(i)}')
