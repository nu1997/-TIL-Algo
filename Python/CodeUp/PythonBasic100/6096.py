'''
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
'''

board = list(list(map(int, input().split())) for _ in range(19))
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(19):
        # board[i][a-1] = int(not board[i][a-1])
        # board[b-1][i] = int(not board[b-1][i])
        board[a-1][i] = int(not board[a-1][i])
        board[i][b-1] = int(not board[i][b-1])
for i in range(19):
    print(*board[i])