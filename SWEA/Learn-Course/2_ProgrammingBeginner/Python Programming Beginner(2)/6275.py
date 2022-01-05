# 입력없음
# 리스트 내포 기능이 뭐야?

sentence = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowels = 'aeiou'
new_list = [i for i in sentence if i not in vowels]

print(''.join(new_list))