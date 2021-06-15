# 입력 없음

beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
new_price = {}

for k, v in beer.items():
    new_price[k] = (v * 1.05)

print(beer)
print(new_price)