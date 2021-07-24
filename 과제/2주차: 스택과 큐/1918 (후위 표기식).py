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
