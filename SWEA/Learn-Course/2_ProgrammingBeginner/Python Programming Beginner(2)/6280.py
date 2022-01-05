import sys
sys.stdin = open("ex_028_input.txt")

N = int(input())
div_list = [i for i in range(1, N+1) if N % i == 0]

print(div_list)