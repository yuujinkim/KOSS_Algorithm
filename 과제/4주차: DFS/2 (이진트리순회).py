def preorder(x):
    if x > 0 and x < 8:
        print(x, end=' ')
        preorder(2*x)
        preorder(2*x+1)


def inorder(x):
    if x > 0 and x < 8:
        inorder(2*x)
        print(x, end=' ')
        inorder(2*x+1)


def postorder(x):
    if x > 0 and x < 8:
        postorder(2*x)
        postorder(2*x+1)
        print(x, end=' ')


print("전위순회 : ", end='')
preorder(1)
print("\n중위순회 : ", end='')
inorder(1)
print("\n후위순회 : ", end='')
postorder(1)
