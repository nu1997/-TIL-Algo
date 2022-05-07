import sys
sys.stdin = open("ex_071_input.txt")

result  = ""

for i in range (100, 301):
    if i // 100 % 2 == 0 and i // 10 % 2 == 0 and i % 2 == 0:
        result += str(i) + ','
print(result.rstrip(","))
