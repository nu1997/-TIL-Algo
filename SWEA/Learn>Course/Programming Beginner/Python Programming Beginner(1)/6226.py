import sys
sys.stdin = open("ex_062_input.txt")

result = []
for a in range (1, 201):
    # 7로 나누었을 때 나머지가 0이고 and 5로 나누었을 때 나머지가 0이 아니다
    if (a % 7 == 0) and (a % 5 != 0):
        result += [str(a)]

print(','.join(result))