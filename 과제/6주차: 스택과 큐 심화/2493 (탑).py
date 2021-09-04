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
