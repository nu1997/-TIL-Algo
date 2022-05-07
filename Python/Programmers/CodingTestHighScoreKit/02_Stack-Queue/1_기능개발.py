def solution(progresses, speeds):
    queue = []
    dates = []
    for i in range(len(progresses)):
        day = 0
        work = progresses[i]
        while work < 100:
            day += 1
            work += speeds[i]
            # print(day, work)
        if len(queue) < 1:
            dates.append(day)
            queue.append(1)
        else:
            if dates[-1] >= day:
                queue[-1] += 1
            else:
                queue.append(1)
                dates.append(day)
    return queue


########## 다른 사람의 풀이 ############
### BEST 1
def solution(progresses, speeds):
    Q=[]
    # zip 사용 !
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

### BEST 2
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer