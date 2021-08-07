# 런타임 에러 (RecursionError)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def preorder(first, last):
    if first != last:
        root = last
        print(last)
        if postorder.index(first) < inorder.index(root)-1:
            preorder(first, postorder[inorder.index(root)-1])
        elif postorder.index(first) == inorder.index(root)-1:
            print(first)
            inorder.remove(first)
            postorder.remove(first)
        if inorder.index(root) < postorder.index(root)-1:
            preorder(postorder[inorder.index(root)], postorder[postorder.index(root)-1])
        elif inorder.index(root) == postorder.index(root)-1:
            print(postorder[inorder.index(root)])
            inorder.remove(postorder[inorder.index(root)])
            postorder.remove(postorder[inorder.index(root)])
    else:
        print(first)
    inorder.remove(last)
    postorder.remove(last)

preorder(postorder[0], postorder[-1])
