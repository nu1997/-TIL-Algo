
N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

'''
from itertools import combinations

lst = combinations([x for x in range(1, N+1)], M)
for el in lst:
    print(el)
'''