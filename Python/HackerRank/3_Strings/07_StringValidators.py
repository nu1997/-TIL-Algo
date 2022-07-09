def solution(string):
    for sy in string:
        if sy.isalnum():
            print(True)
            break
    else:
        print(False)
    for sy in string:
        if sy.isalpha():
            print(True)
            break
    else:
        print(False)
    for sy in string:
        if sy.isdigit():
            print(True)
            break
    else:
        print(False)
    for sy in string:
        if sy.islower():
            print(True)
            break
    else:
        print(False)
    for sy in string:
        if sy.isupper():
            print(True)
            break
    else:
        print(False)

if __name__ == '__main__':
    s = input()
    solution(s)