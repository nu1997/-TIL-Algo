# 5986. 새샘이와 세 소수

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 7 <= N <= 999
    for i in range(2, N):
        prime = []
        for j in range(1 ,i):
            if i % j == 0:
                prime.append(j)
        if prime = [1, j]:


