import sys
sys.stdin = open("ex_064_input.txt")

N = int(input())

square_dict = {}
for n in range(1, N+1):
    square_dict[n] = n ** 2

print(square_dict)