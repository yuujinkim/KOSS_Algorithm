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
