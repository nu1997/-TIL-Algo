import sys
sys.stdin = open("ex_005_input.txt")

score = [88, 30, 61, 55, 95]
for i in range (0, 5):
    if score[i] >= 60:
        result = "합격"
    else:
        result = "불합격"
    print("%d번 학생은 %d점으로 %s입니다." % (i+1, score[i], result))