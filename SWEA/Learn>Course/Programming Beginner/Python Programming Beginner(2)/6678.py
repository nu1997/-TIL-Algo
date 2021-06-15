import sys
sys.stdin = open("ex_069_input.txt")

def upper_case(x):
    
    return x.upper()

count = 0
while True:
    x = input()
    print(f'>> {upper_case(x)}')
    
    if x == '':
        break

    count += 1
    if count == 3:
        break