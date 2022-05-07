# 2948. 문자열 교집합

T = int(input())
for tc in range(1, T+1):
    L1, L2 = map(int, input().split())
    A = input().split()
    B = input().split()
    ans = len(set(A) & set(B))
    print('#%d %d' % (tc, ans))