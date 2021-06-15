def binarySearch(a, key):
    l = 1
    r = len(a) - 1
    cnt = 0
    while l <= r:
        c = int((l + r) / 2)
        if key == a[c]:
            cnt += 1
            return cnt
        elif key > a[c]:
            cnt += 1
            l = c
        else:
            cnt += 1
            r = c
    return False

T = int(input())
for t in range(1, T+1):
    book, a_key, b_key = map(int, input().split())
    book_list = list(range(book+1))

    if binarySearch(book_list, a_key) < binarySearch(book_list, b_key):
        win = 'A'
    elif binarySearch(book_list, a_key) == binarySearch(book_list, b_key):
        win = '0'
    else:
        win = 'B'

    print('#%d %s' % (t, win))