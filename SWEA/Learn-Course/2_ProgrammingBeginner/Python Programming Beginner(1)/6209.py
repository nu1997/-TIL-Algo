import sys
sys.stdin = open("ex_004_input.txt")

a = int(input())
print("{0:.2f} ℉ =>  {1:.2f} ℃".format(a, (a-32)/1.8)