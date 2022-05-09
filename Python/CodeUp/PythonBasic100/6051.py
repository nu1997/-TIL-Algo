'''
두 정수(a, b)를 입력받아
a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.
'''

def solution(a, b):
    if a != b:
        return True
    else:
        return False

a, b = map(int, input().split())
print(solution(a, b))