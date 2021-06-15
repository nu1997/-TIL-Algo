result = ""
for i in range (1, 101):
    if i % 2:
        result += str(i) + ', '
print(result.rstrip(", "))