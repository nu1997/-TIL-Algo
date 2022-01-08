def solution(numbers):
    reference = list(range(10))
    for number in numbers:
        reference.remove(number)
    answer = sum(reference)
    return answer