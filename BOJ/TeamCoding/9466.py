# 텀 프로젝트

'''
이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다. 심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다. 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단, 단 한 명만 선택할 수 있다.) 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.

학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나, s1이 s2를 선택하고, s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다.

예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.

1	2	3	4	5	6	7
3	1	3	7	3	4	6
위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.

주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)

각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.

'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split())) # 인덱스 번호 + 1 = 학생의 번호
    visited = [[] for _ in range(N + 1)]
    for i in range(N): # 0123456
        visited[students[i]].append(i+1)


    # [[], [2], [], [1, 3, 5], [6], [], [7], [4]]
    # [[], [1], [2], [3], [4], [5], [6], [7], [8]]

"""

    첫번째 경우의 수: 내가 정한 루프의 시작이 start를 만났을
    두번째 경우의 수: 내가 정한 루프의 시작부터 루프가 완성되었을 때 (재귀를 들어가다가 start를 만날때까지의 방문 list를 만든다)
        그 루프 안에 origin이 있을 때
            True
        그 루프 안에 origin이 없을 때
            False
    세번째 경우의 수: 내가 정한 루프의 시작부터 루프가 완성되지 못했을 때 (재귀를 돌다가 start를 만나기 전에 방문 list에 있는 수를 만났을 때)

def check(n):
    global self
    if students[n-1] == n:
        self += [students[n-1]]
        return True
    elif students[n-1] == start or students[n-1] == origin:
        return True
    elif students[n-1] in self:
        return False
    else:
        global visited
        if students[n-1] not in visited:
            visited += [students[n-1]]
            check(students[n-1])
        else:
            return False
    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split())) # 인덱스 번호 + 1 = 학생의 번호
    cnt = 0
    # i 학생(그 학생번호는 i+1) 부터 체크를 할건데
    for i in range(N):
        # i 가 지목한 학생부터 루프 시작
        origin = i + 1
        start = students[i]
        if check(start) == False: # 3 1 3 7 3 4 6
            cnt += 1
    # print(cnt)


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.insert(0, 0)
    result = 0
    
    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        # 현재 조회하고 있는 숫자
        number = numbers[i]
        # 현재 숫자와 인덱스가 같지 않다면
        while number != i:
            if visited[number] == 0:
                # 방문처리
                visited[number] = 1
                # 현재 숫자를 교체
                number = numbers[number]
                if number == i:
                    result += 1
                    break
            else:
                break
    
    print(result)
"""