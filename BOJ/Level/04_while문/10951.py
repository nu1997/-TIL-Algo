# A+B - 4

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except: break

# EOF이란?
# try - except 문을 완전히 까먹고 있었다
# 예외처리를 어떻게 해야할까? -> try except문을 기억하자.