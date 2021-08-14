def subset(x, n):
    if n == x:
        for i in range(n):
            if check[i] == 1:
                print(i+1, end=' ')
        print()
    else:
        check[x] = 1
        subset(x+1, n)
        check[x] = 0
        subset(x+1, n)


N = int(input())
check = [0]*N
subset(0, N)
