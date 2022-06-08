import sys

lst = list(sys.stdin.readline().rstrip())
lst.sort(reverse=True)
print(''.join(lst))
