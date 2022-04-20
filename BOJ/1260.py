N, M, V = map(int, input().split())
graph = {n: [0, []] for n in range(1, N+1)}
for i in range(M):
    a, b = map(int, input().split())
    graph[a][1].append(b)
    # graph[b].append(a)
print(graph)

def DFS(v, graph):
    stack = [v]
    graph[v][0] = 1
    res = [v]
    while stack:
        stack[0]

    pass

def BFS(v, graph):
    queue = [v]
    pass




'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''