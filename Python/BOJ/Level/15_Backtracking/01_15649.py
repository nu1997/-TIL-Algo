
N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

array = []

def dfs():
    if len(array) == m: # 길이가 M이 됐다면
        for i in array: # array 원소들 출력
            print(i, end = ' ')
        print()
        return # 호출 됐던 위치로 돌아가기
    
    for i in range(1, n + 1): # 자연수 1~N까지 
        if i not in array: # i가 array 안에 없다면
            array.append(i) # i를 array에 삽입
            dfs()           # 재귀함수
            array.pop()     # array의 오른쪽 원소 삭제

dfs()