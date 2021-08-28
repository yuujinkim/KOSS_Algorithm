M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

area = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            cnt = 1
            board[i][j] = 1
            tmp = [(i, j)]
            while tmp:
                x, y = tmp.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                        cnt += 1
                        board[nx][ny] = 1
                        tmp.append((nx, ny))

            area.append(cnt)

print(len(area))
area.sort()
for i in area:
    print(i, end=' ')
