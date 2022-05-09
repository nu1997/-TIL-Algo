# 기초 100제 개념 정리

### 100제를 위한 파일 한번에 생성

``` python
import os

files_path = "./"
num = 100
for i in range(101):
    filename = str(6000 + i) + '.py'
    f = open(filename, 'a')
    f.close()
```

### 이스케이프 문자

| 이스케이프 문자 | 설명 |
| --- | --- | 
| \n | 줄바꿈 |
| \t | 탭 |
| \b | 백스페이스 |
| \000 | NULL 문자 |
| \ \ | \ |
| \ ' | 작은따옴표 |
| \ " | 큰따옴표 |
| \r | 줄 바꿈, 커서를 앞으로 이동 |
| \f | 줄 바꿈, 커서를 다음 줄로 이동 |
| \a | 벨소리 |
| \v | 수직 탭 |


### HEX
#### hex(x)

``` python
hex(255)
'0xff'
hex(-42)
'-0x2a'
```

> If you want to convert an integer number to an uppercase or lower hexadecimal string with prefix or not, you can use either of the following ways:

``` python
'%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
```

### 최대공약수 - 반복문
```python
for i in range(min(a, b, c), 0, -1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        print(i)
        break
```
### 최소공배수 - 반복문
```python
for i in range(max(a, b, c), (a*b*c)+1):
    if i % a == 0 and i % b == 0 and i % c == 0:
        print(i)
        break
```

### 최소공배수 - 유클리드 호제법 
> x와 y의 최대공약수 == y 와 r의 최대공약수 (x % y = r)
? 변수 3개에도 쓸 수 있는가?

```python
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

print(LCM(a, b, c))
```

### reverse() / reversed() ?!

변수에 할당할 수 있는가 없는가의 차이이다.
```python
a = [1, 2, 3, 4, 5]
a.reverse()
print(a) # [5, 4, 3, 2, 1]
```

```python
a = [1, 2, 3, 4, 5]
b = a.reversed()
print(b) # [5, 4, 3, 2, 1]
```