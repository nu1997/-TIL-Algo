import sys
sys.stdin = open("ex_072_input.txt")

ex_input = input()
letters = 0
digits = 0

for i in ex_input:
    try:
        if int(i):
            digits += 1
    except:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            letters += 1

print(f'LETTERS {letters}')
print(f'DIGITS {digits}')