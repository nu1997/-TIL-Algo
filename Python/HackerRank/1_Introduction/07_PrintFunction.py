def solution(n):
    ans = ''
    for i in range(1, n+1):
        ans += str(i)
    return ans

if __name__ == '__main__':
    n = int(input())
    print(solution(n))