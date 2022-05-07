import sys
sys.stdin = open("ex_024_input.txt")

num_list = [int(input()) for i in range(5)]
num_avg = sum(num_list) / len(num_list)
print(f'입력된 값 {num_list}의 평균은 {num_avg}입니다.')