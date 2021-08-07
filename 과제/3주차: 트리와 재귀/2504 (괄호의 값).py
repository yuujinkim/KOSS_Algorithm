# 시간초과

string = list(input())

stack = []

for i in string:
    if i == ")":
        while stack:
            if stack[-1] == "(":
                stack.pop()
                stack.append(2)
            elif stack[-1] == "[":
                print(0)
                quit()
            else:
                while len(stack)>1 and type(stack[-2]) == int:
                    temp = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                if len(stack)>1 and stack[-2] == '(':
                    temp = stack[-1] * 2
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
    elif i == "]":
        while stack:
            if stack[-1] == "[":
                stack.pop()
                stack.append(3)
            elif stack[-1] == "(":
                print(0)
                exit()
            else:
                while len(stack)>1 and type(stack[-2]) == int:
                    temp = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                if len(stack)>1 and stack[-2] == '[':
                    temp = stack[-1] * 3
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
    else:
        stack.append(i)

while len(stack)>1 and type(stack[-1]) == int and type(stack[-2]) == int:
    temp = stack[-1] + stack[-2]
    stack.pop()
    stack.pop()
    stack.append(temp)

if len(stack) == 1 and type(stack[0]) == int:
    print(stack[0])
else:
    print(0)
    exit()
