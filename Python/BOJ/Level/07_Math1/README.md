``` python
# fibonacci recursive function memoization (재귀함수 메모화)

# 변수 정의
count = 0 # 계산 카운트
fibo = 7 # fibonacci 7번째 값
dictionary = { # 이미 계산한 값을 저장할 딕셔너리
    1: 1,
    2: 1
}

# 함수 정의
def fibo_memo(n):
    global count
    count += 1
    print(f'fibo_memo({n}) 호출, count: {count}')
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fibo_memo(n-1) + fibo_memo(n-2)
        print(dictionary)
        return dictionary[n]

# 결과 출력
print('-'*10+f'\nfibo_memo({fibo}): {fibo_memo(fibo)} 계산에 활용된 함수 호출 횟수는 {count}번입니다.\n'+'-'*10)
print()
```

https://devinus.tistory.com/38