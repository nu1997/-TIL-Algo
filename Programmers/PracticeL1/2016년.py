# 월별 일수를 7로 나눈 값, 1월이 기준이므로 1월은 0
months = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

def solution(a, b):
    date = 0
    point = 5 #금요일은 days에서 5번째이므로

    date += sum(months[:a-1])
    date += (b - 1) % 7
    if date > 6:
        date %= 7
    point += date
    
    if point > 6:
        point -= 7
    return days[point]