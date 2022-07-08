def split_and_join(line):
    lst = line.split()
    ans = "-".join(lst)
    return ans

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)