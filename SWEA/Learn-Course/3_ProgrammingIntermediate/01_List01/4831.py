def min_charge(charge_list):
    for cl in range(len(charge_list) - 1):
        if charge_list[cl + 1] - charge_list[cl] > K:
            return 0

    station_list = [0] * (N + 1)
    for i in range(len(charge_list)):
        station_list[charge_list[i]] += 1
    bus = 0
    charge = 0
    while bus < (N - K):
        for i in range(bus + K, bus, -1):
            if station_list[i] == 1:
                charge += 1
                bus = i
                break
    return charge


T = int(input())

for t in range(1, T + 1):
    # K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N = 정류장 수
    # M = 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    charge_list = list(map(int, input().split()))
    print('#%d %d' % (t, min_charge(charge_list)))

# done.