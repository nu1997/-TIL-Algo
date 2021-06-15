import sys
sys.stdin = open("ex_002_input.txt")

a = int(input())
print("{0:.2f} kg =>  {1:.2f} lb".format(a, a * 2.2046))