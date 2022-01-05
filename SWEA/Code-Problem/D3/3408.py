# def allsum(n):
#     allsum = 0
#     for i in range(n+1):
#         allsum += i
#     return allsum
#
# def oddsum(n):
#     oddsum = 0
#     for i in range(n):
#         oddsum += (i * 2 + 1)
#     return oddsum
#
# def evensum(n):
#     evensum = 0
#     for i in range(n+1):
#         evensum += (i*2)
#     return evensum

# for문 하지말고 등차수열 공식 적용

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S1 = N * (N + 1) // 2
    S2 = N ** 2
    S3 = N * (N + 1)
    # print('#%d %d %d %d' % (tc, allsum(N), oddsum(N), evensum(N)))
    print('#%d %d %d %d' % (tc, S1, S2, S3))