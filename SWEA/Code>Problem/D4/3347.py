# 올림픽 종목 투표

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    An = list(map(int, input().split()))
    Bm = list(map(int, input().split()))
    vote = [0] * N
    for j in range(M):
        # 비용 Bm[j] > An[i]인 i를 고르기. 가장 작은 i.
        for i in range(N):
            if Bm[j] >= An[i]:
                vote[i] += 1
                # print(i)
                break
    ans = vote.index(max(vote))
    print('#%d %d' % (tc, ans+1))