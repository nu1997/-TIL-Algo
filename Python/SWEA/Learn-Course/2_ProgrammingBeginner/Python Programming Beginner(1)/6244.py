result = 0
score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
while len(score):
    i = score.pop()
    if i >=80:
        result += i
print(result)  