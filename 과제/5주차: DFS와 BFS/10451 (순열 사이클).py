import sys
sys.setrecursionlimit(10000)


def cycle(i):
    global cnt
    global check
    if check[i] == 1:
        cnt += 1
    else:
        check[i] = 1
        cycle(P[i-1])


T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    check = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if check[i] == 0:
            cycle(i)
    print(cnt)
