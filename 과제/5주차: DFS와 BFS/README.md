# [10451번 (순열 사이클)](https://www.acmicpc.net/problem/10451)

#### 시간 초과
```
import sys
sys.setrecursionlimit(10000)


def cycle(i):
    global cnt
    global visit
    global check
    if check[i] == 1:
        cnt += 1
        check = [0 for _ in range(N+1)]
    else:
        visit[i] = 1
        check[i] = 1
        cycle(P[i-1])


T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    visit = [0] * (N+1)
    check = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if visit[i] == 0:
            cycle(i)
    print(cnt)
```
__전체 for문을 수행할 때 방문했는지 체크하는 visit 리스트와 한 사이클을 돌 때 방문했는지 체크하는(방문한 경우 하나의 사이클 완성) check리스트를 사용__  
중복된 기능을 하는 리스트 2개를 하나의 리스트만으로 구현하여 시간 단축

#### 정답 코드
```
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
```
