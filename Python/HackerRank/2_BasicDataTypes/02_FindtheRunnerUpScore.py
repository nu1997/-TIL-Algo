def runnerup(arr):
    arr.sort(reverse=True)
    for el in arr:
        if el < max(arr):
            return el

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(runnerup(arr))