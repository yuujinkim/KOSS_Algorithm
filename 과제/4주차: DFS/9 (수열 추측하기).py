def P(level):
    global cnt
    if level == N:
        cnt += 1
        sum = 0
        for i in range(N):
            sum += answer[i]*p[i]
        if sum == F:
            for i in range(N):
                print(answer[i], end=' ')
            quit()
    else:
        for i in range(1, N+1):
            check = True
            for j in answer:
                if i == j:
                    check = False
            if check is True:
                answer[level] = i
                P(level+1)
                answer[level] = 0


N, F = map(int, input().split())

answer = [0]*N
p = [1]*N
for i in range(1, N):
    p[i] = p[i-1]*(N-i)/i
cnt = 0

P(0)
print(cnt)
