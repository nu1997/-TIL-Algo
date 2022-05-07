# 입력없음

# [[2단],[3단],[4단], ..., [9단]] 만드는데 3의 배수 / 7의 배수 빼고
# 리스트 표현식으로 2차원 리스트 만들기

result = [[i * v for v in range(1, 10) if (i * v) % 3 != 0 and (i * v) % 7 != 0] for i in range(2, 10)]

print(result)