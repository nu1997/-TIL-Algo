btype = {'A': 0, 'B': 0, 'O': 0, 'AB': 0}
data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for i in data:
    btype[i] += 1
print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" % (btype['A'], btype['O'], btype['B'], btype['AB']))