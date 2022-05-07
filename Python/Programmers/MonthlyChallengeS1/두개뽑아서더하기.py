def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                x = numbers[i] + numbers[j]
                if x not in answer:
                    answer.append(x)
    return sorted(answer)