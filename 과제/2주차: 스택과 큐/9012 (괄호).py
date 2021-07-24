T = int(input())

for _ in range(T):
    PS = input()

    left = 0
    right = 0
    check = True

    for i in PS:
        if i == '(':
            left += 1
        else:
            right += 1

        if left < right:
            check = False
            break

    if left != right:
        check = False

    if check:
        print("YES")
    else:
        print("NO")
