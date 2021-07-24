from collections import deque
import sys

N = int(input())

buffer = deque()

while True:
    input = int(sys.stdin.readline())
    if input == -1:
        break
    elif input != 0 and len(buffer) < N:
        buffer.append(input)
    elif input == 0:
        buffer.popleft()

if buffer:
    for i in buffer:
        print(i)
else:
    print("empty")
