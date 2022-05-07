# 입력 없음

fruit = ['   apple    ','banana','  melon']


fruit_list = [(i.strip(' '), len(i.strip(' '))) for i in fruit]
fruit_dict = dict(fruit_list)
print(fruit_dict)