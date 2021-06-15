import sys
sys.stdin = open("ex_063_input.txt")

N = int(input())

result = 1
for n in range(1, N+1):
    result *= n

print(result)