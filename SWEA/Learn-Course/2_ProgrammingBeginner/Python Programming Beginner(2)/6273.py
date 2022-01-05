# 입력없음

def calc_sum(scores):
    total = sum(scores)
    return total

def calc_avg(scores):
    result = sum(scores) / len(scores)
    return result


A = 90, 80
B = 85, 75
C = 90, 100

student_list = [A, B, C]
count = 1
for student in student_list:
    print(f'{count}번 학생의 총점은 {calc_sum(student)}점이고, 평균은 {calc_avg(student)}입니다.')
    count += 1