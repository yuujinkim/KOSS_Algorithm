import sys

def path(dep):
    global cnt
    
    if dep == N-1:
        cnt += 1
        for i in range(N):
            visit[i] = 0
        # break
    else:
        visit[dep] = 1
        for i in range(N):
            if graph[dep][i] == 1 and visit[i] == 0:
                path(i)


N, M = map(int, input().split())
graph = [[0]*N for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1

cnt = 0
visit = [0]*N
path(0)
print(cnt)
