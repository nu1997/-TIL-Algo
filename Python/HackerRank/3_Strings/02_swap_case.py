def swap_case(s):
    ans = ''
    for sy in s:
        if sy.isupper():
            ans += sy.lower()
        elif sy.islower():
            ans += sy.upper()
        else:
            ans += sy
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)