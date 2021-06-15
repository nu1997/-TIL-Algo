import sys
sys.stdin = open("ex_065_input.txt")

N = input()
N_list = [i for i in map(int, N.split(', '))]
N_tuple = tuple(N_list)
print(N_list)
print(N_tuple)