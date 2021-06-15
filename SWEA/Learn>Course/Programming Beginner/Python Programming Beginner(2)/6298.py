# 입력없음
# 주어진 튜플의 앞 절반 뒤 절반 출력

nums = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
nums_list = list(nums)
cut = len(nums_list) // 2 # 5
front = nums_list[0:cut]
back = nums_list[cut:]
t_front = tuple(front)
t_back = tuple(back)
print(t_front)
print(t_back)