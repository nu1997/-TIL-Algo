import sys
sys.stdin = open("ex_051_input.txt")

N = input()

digit_sum = 0
for n in N:
    digit_sum += int(n)

print(digit_sum)