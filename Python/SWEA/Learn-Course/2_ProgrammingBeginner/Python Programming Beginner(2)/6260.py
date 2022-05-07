import sys
sys.stdin = open("ex_073_input.txt")

ex_input = input()
uppers = 0
lowers = 0

for i in ex_input:
    try:
        if 'a' <= i <= 'z':
            lowers += 1
        elif 'A' <= i <= 'Z':
            uppers += 1
    except:
        continue

print(f'UPPER CASE {uppers}')
print(f'LOWER CASE {lowers}')