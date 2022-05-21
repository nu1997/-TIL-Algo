import os

files_path = "./"
num = 100
for i in range(1, 100):
    filename = str(1000 + i) + '.c'
    f = open(filename, 'a')
    f.close()