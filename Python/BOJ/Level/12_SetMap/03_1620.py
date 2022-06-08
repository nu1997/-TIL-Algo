# 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int, input().split())

pokemon_idx = dict()
pokemon_name = dict()

for i in range(N):
    x = sys.stdin.readline().rstrip()
    pokemon_idx[i+1] = x
    pokemon_name[x] = i+1

# print(pokemon_idx, pokemon_name)

quiz = []
for _ in range(M):
    quiz.append(sys.stdin.readline().rstrip())

for q in quiz:
    if q.isdigit():
        print(pokemon_idx[int(q)])
    else:
        print(pokemon_name[q])