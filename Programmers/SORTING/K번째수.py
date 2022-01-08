def solution(array, commands):
    answer = []
    # i번째부터 j번째까지 자르고(포함) 정렬한 뒤 k번째 숫자 -> python으로는 꽤 쉽군.
    for command in commands:
        new_array = sorted(array[command[0]-1:command[1]])
        answer.append(new_array[command[2]-1])
    return answer