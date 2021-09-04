# [2493번 (탑)](https://www.acmicpc.net/problem/2493)

#### 시간 초과
```
N = int(input())
tower = list(map(int, input().split()))

rec = 0
answer = [0]
for i in range(1, N):
    for j in range(1, N):
        if tower[i-j] > tower[i]:
            rec = i-j+1
            break
    answer.append(rec)
    rec = 0
for i in answer:
    print(i, end=' ')
```
__이중 for문으로 풀면 시간 복잡도가 O(N²)이기 때문에 시간초과 발생 -> stack으로 해결__  
자신의 왼쪽 탑의 높이가 자신의 높이보다 작으면 왼쪽 탑은 어떤 탑이 보낸 레이저 신호도 수신하지 못함.

#### 정답 코드
```
N = int(input())
tower = list(map(int, input().split()))

stack = [[1, tower[0]]]
print(0, end=' ')
for i in range(1, len(tower)):
    if stack[-1][1] < tower[i]:
        while stack and stack[-1][1] < tower[i]:
            stack.pop()
        if stack:
            print(stack[-1][0], end=' ')
            stack.append([i+1, tower[i]])
        else:
            print(0, end=' ')
            stack.append([i+1, tower[i]])
    else:
        print(stack[-1][0], end=' ')
        stack.append([i+1, tower[i]])
```
