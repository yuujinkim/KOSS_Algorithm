def P(level):
    global cnt
    if level == M:
        cnt += 1
        for i in answer:
            print(i, end=' ')
        print()
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


N, M = map(int, input().split())

answer = [0]*M
cnt = 0

P(0)
print(cnt)
