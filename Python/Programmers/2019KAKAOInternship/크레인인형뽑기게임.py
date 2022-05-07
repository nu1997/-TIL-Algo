def solution(board, moves):
    answer = 0
    n_board = list(map(list, zip(*board)))
    N = len(n_board)
    stack = []
    for move in moves:
        for i in range(N):
            x = n_board[move-1][i]
            if x != 0:
                stack.append(x)
                n_board[move-1][i] = 0
                if len(stack) > 1 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer