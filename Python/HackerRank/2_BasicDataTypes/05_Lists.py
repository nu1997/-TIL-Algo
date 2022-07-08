if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        try:
            command, val, idx = input().split()
            if command == 'insert':
                arr.insert(idx, val)
        except:
            try:
                command, val = input().split()
                if command == 'append':
                    arr.append(val)
                elif command == "remove":
                    arr.remove(val)
            except:
                try:
                    command = input()
                    if command == "print":
                        print(arr)
                    elif command == "sort":
                        arr.sort()
                    elif command == "pop":
                        arr.pop()
                    elif command == "reverse":
                        arr.sort(reverse=True)
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    N = int(input())
    lst = []
    arr = []
    for _ in range(N):
        lst.append(input().split())
    for el in lst:
        if el[0] == "insert":
            arr.insert(int(el[1]), int(el[2]))
        elif el[0] == "print":
            print(arr)
        elif el[0] == "remove":
            arr.remove(int(el[1]))
        elif el[0] == "append":
            arr.append(int(el[1]))
        elif el[0] == "sort":
            arr.sort()
        elif el[0] == "pop":
            arr.pop()
        elif el[0] == "reverse":
            arr.sort(reverse=True)