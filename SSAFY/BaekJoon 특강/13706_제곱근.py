N = int(input())
for i in range(1, N//2):
    if N % i == 0:
        if i * i == N:
            print(i)