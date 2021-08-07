# 런타임 에러 (IndexError)

preorder = list(map(int, input().split()))

root = []

root.append(preorder[0])

for i in range(1, len(preorder)-1):
    if preorder[i] < root[-1]:
        root.append(preorder[i])
    else:
        if preorder[i] > root[-2]:
            print(root.pop())
            if preorder[i] < preorder[i+1]:
                print(preorder[i])
            elif preorder[i] > preorder[i+1]:
                root.append(preorder[i])
            else:
                print(preorder[i])
                while(len(root) != 0):
                    print(root.pop())
        elif preorder[i] < root[-2]:
            if preorder[i] < preorder[i+1]:
                print(preorder[i])
            elif preorder[i] > preorder[i+1]:
                root.append(preorder[i])
            else:
                print(preorder[i])
                while(len(root) != 0):
                    print(root.pop())
if preorder[-1] < root[-1]:
    root.append(preorder[-1])
else:
    if preorder[-1] > root[-2]:
        print(root.pop())
        print(preorder[i])
        while(len(root) != 0):
            print(root.pop())
    elif preorder[-1] < root[-2]:
        print(preorder[-1])
        while(len(root) != 0):
            print(root.pop())
