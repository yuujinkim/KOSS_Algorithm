N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1
L = int(input())
change = {}
for _ in range(L):
    X, C = input().split()
    change[int(X)] = C

x, y = 0, 0
snake = [[x, y]]
time = 0

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기방향 : 동
direction = 1

while(True):
    x += dx[direction]
    y += dy[direction]
    time += 1
    
    if time in change:
        if change[time] == "L":
            direction = (direction-1)%4
        else:
            direction = (direction+1)%4

    # 벽에 부딪힌 경우
    if x<0 or x>=N or y<0 or y>=N:
        print(time)
        quit()

    # 사과가 있는 경우 : 몸길이 증가
    if board[x][y] == 1:
        snake.append([x, y])
        board[x][y] = 2
    # 사과가 없는 경우 : 단순 이동
    elif board[x][y] == 0:
        snake.append([x, y])
        board[x][y] = 2
        tx, ty = snake.pop(0)
        board[tx][ty] = 0
    # 자신의 몸과 부딪힌 경우
    else:
        print(time)
        quit()
print(time)
