def get_minmax(num):
    max_num = num[0]
    min_num = num[0]
    for n in range(1, N):
        if num[n] > max_num:
            max_num = num[n]
        elif num[n] < min_num:
            min_num = num[n]
    result = max_num - min_num
    return result

# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
T = int(input())

for t in range(1, T+1):
    # 각 케이스의 첫 줄에 양수의 개수 N이 주어진다.(5 ≤ N ≤ 1000 )
    N = int(input())
    # 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
    num = list(map(int, input().split()))

    print("#{0} {1}".format(t, get_minmax(num)))