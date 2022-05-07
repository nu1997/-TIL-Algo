T = int(input())
for tc in range(1, T+1):
    N = int(input())
    text = ''
    for _ in range(N):
        C, K = input().split()
        text += C * int(K)

    print('#%d' % tc)
    for i in range(len(text)//10):
        print(text[i*10:i*10+10])
    if len(text) % 10 != 0:
        print(text[len(text)//10*10:])