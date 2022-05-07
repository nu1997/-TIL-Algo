import sys
sys.stdin = open("ex_001_input.txt")

a = int(input())
print("{0:.2f} inch =>  {1:.2f} cm".format(a, a * 2.54))