# 5607. 조합

num = 1234567891

T = int(input())
for tc in range(1, T+1):
    N, R = map(int, input().split())
    b = 1 #분자
    a = 1 #분모
    for i in range(R):
        b *= (N-i)
        a *= (i+1)
    ans = (b // a) % num
    print('#%d' % tc, ans)
