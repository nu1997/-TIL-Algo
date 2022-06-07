# 그룹 단어 체커

N = int(input())
cnt = 0
for _ in range(N):
    S = input()
    flag = 1
    for i in range(len(S)-1):
        if S[i] in S[i+1:] and S[i+1] != S[i]:
            flag = 0
            break
    if flag == 1:
        cnt += 1
print(cnt)