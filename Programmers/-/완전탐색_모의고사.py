def solution(answers):
    result = [0, 0, 0]
    # 12345 / 21232425 21232425 21232425 21232425 21232425 / 33112 24455 
    player_1 = [1, 2, 3, 4, 5]
    player_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    player_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == player_1[i % 5]:
            result[0] += 1

        if answers[i] == player_2[i % 40]:
            result[1] += 1

        if answers[i] == player_3[i % 10]:
            result[2] += 1
    answer = []
    for j in range(3):
        if result[j] == max(result):
            answer += [j+1]
    return answer