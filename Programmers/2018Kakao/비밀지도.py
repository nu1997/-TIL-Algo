def solution(n, arr1, arr2):
    answer = []
    # n만큼 arr1과 arr2 꺼내서 바로 이진수로 뽑자
    for i in range(n):
        a = arr1[i]
        b = arr2[i]
        temp1 = str(format(a | b, 'b')).zfill(n)
        # 람다 넣고 map으로 뽑으면 tuple로 뽑힘
        temp2 = map(lambda x: '#' if x == '1' else ' ', temp1)
        temp = ''.join(temp2)
        answer.append(temp)
    return answer