# 스택과 큐

* 스택: 후입선출 (LIFO: Last In First Out, FILO: First In Last Out)
```
import sys

N = int(input())

stack = []

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        x = order[1]
        stack.append(x)

    elif order[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif order[0] == "size":
        print(len(stack))

    elif order[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
```

* 큐: 선입선출 (FIFO: First In First Out)
```
import sys

N = int(input())

queue = []
front = 0

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        x = order[1]
        queue.append(x)

    elif order[0] == "pop":
        if len(queue) != front:
            print(queue[front])
            front += 1
        else:
            print(-1)

    elif order[0] == "size":
        print(len(queue)-front)

    elif order[0] == "empty":
        if len(queue) == front:
            print(1)
        else:
            print(0)

    elif order[0] == "front":
        if len(queue) != front:
            print(queue[front])
        else:
            print(-1)

    elif order[0] == "back":
        if len(queue) != front:
            print(queue[-1])
        else:
            print(-1)
```


---


# [1918번 (후위 표기식)](https://www.acmicpc.net/problem/1918)

#### 정답 코드
```
infix = input()
postfix = ''
stack = []

priority = {'(':0, '+':1, '-':1, '*':2, '/':2}

for i in infix:
    if i.isalpha():
        postfix += i
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while True:
            if stack and stack[-1] != '(':
                postfix += stack.pop()
            else:
                stack.pop()
                break
    else:
        while True:
            if stack and priority[stack[-1]] >= priority[i]:
                postfix += stack.pop()
            else:
                stack.append(i)
                break
while stack:
    postfix += stack.pop()

print(postfix)
```
## 중위 표기에서 후위 표기로의 변환
1. 피연산자는 push 하지 않고 출력
2. '('면 push
3. ')'면 stack[-1]가 '('가 될 때까지 pop 한 후 출력
4. stack[-1]이 '('이면 pop
5. 연산자는 스택이 비었을 경우 push
6. 연산자는 스택이 비어있지 않은 경우 stack[-1]의 우선순위와 비교하여 현재 연산자의 우선순위가 더 높으면 push, 더 낮거나 같으면 pop 한 후 출력
7. 수식 전체를 한 번 검사한 다음 스택이 빌 때까지 pop 한 후 출력
