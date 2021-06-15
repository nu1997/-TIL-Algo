def solution(numbers):
    answer = []
    for num in numbers:
        if num % 4 == 3:
            temp = 2
            while num:
                if 1 <= format(num ^ (num + temp), 'b').count('1') <= 2:
                    answer.append(num + temp)
                    break
                else:
                    temp *= 2
        else:
            answer.append(num + 1)
    return answer

