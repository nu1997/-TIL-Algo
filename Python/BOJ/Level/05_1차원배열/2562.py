maximum = 0
order = 0
for i in range(1, 10):
    num = int(input())
    if num > maximum:
        maximum = num
        order = i
print(maximum)
print(order)