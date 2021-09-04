string = input()
explosion = list(input())
stack = []

for i in string:
    stack.append(i)
    if len(stack)>=len(explosion) and stack[-len(explosion):] == explosion:
        for _ in range(len(explosion)):
            stack.pop()
if stack:
    for i in stack:
        print(i, end='')
else:
    print("FRULA")
