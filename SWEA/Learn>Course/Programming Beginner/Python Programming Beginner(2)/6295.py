import sys
sys.stdin = open("ex_067_input.txt")

a, b = map(int, input().split(', '))
two_dimension = [[i * v for i in range(b)]for v in range(a)]
print(two_dimension)