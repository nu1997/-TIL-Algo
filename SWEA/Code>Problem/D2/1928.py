
T = int(input())
for tc in range(1, T+1):
    s = input()
    _bin = ''
    for each in s:
        if 'A' <= each <= 'Z':
            _bin += format(ord(each) - 65, 'b').zfill(6)
        elif 'a' <= each <= 'z':
            _bin += format(ord(each) - 71, 'b').zfill(6)
        elif each == '+':
            _bin += format(ord(each) + 19, 'b').zfill(6)
        elif each == '/':
            _bin += format(ord(each) + 16, 'b').zfill(6)
        else:
            _bin += format(ord(each) + 4, 'b').zfill(6)
    res = ''
    for i in range(len(_bin)//8):
        res += chr(int(_bin[i*8:i*8+8], 2))
    print('#%d' % tc, res)

