S = input().upper()
count_dict = dict()
for i in range(len(S)):
    try:
        count_dict[S[i]] += 1
    except:
        count_dict[S[i]] = 1
ans = []
for k, v in count_dict.items():
    if v == max(count_dict.values()):
        ans += k
if len(ans) > 1:
    print('?')
else:
    print(ans[0])

'''
words = input().upper()
letters = [words.count(chr(c)) for c in range(65, 91)]
m = max(letters)
if letters.count(m) == 1:
    print(chr(letters.index(m) + 65))
else:
    print('?')
'''