### 10진수 -> N진수
def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    
    return rev_base[::-1]

### 최대공약수와 최소공배수 그리고 유클리드 호제법

x, y의 최대공약수는 y, r의 최대공약수와 같다. (r은 x를 y로 나눈 나머지 값)
즉, 계속해서 x에 y값을, y에는 r값을 대입하다보면 언젠가는 x % y == 0일 때가 있다. 이때의 y값이 최대공약수이다.

최소공배수는 x * y 를 최대공약수로 나눈 몫이다.