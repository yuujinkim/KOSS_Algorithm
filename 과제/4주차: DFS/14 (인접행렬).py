import sys
N, M = map(int, input().split())
matrix = [[0]*(N) for _ in range(N)]

for i in range(M):
    u, v, edge = map(int, input().split())
    matrix[u-1][v-1] = edge

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=' ')
    print()
