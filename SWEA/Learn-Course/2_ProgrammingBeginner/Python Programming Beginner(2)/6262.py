import sys
sys.stdin = open("ex_096_input.txt")

ex_input = input()
ex_list = sorted(list(set(ex_input)))
L = len(ex_list)
cnt = [0] * L

for i in ex_input:
    for j in range(L):
        if i == ex_list[j]:
            cnt[j] += 1

for i in range(L):
    print(f'{ex_input[i]},{cnt[i]}')
