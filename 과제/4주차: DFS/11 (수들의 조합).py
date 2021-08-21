def C(level, tmp):
    global cnt
    if level == K:
        sum = 0
        for i in answer:
            sum += i
        if sum % M == 0:
            cnt += 1
    else:
        for i in range(tmp, N+1):
            check = True
            for j in answer:
                if n[i-1] == j:
                    check = False
            if check is True:
                answer[level] = n[i-1]
                C(level+1, i+1)
                answer[level] = 0


N, K = map(int, input().split())
n = list(map(int, input().split()))
M = int(input())

answer = [0]*M
cnt = 0

C(0, 1)
print(cnt)
