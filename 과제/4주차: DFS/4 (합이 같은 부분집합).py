def subset(sum, level):
    global result
    if level == N:
        if sum == total/2:
            result = 1
    else:
        subset(sum+set[level], level+1)
        subset(sum, level+1)


N = int(input())
set = list(map(int, input().split()))

total = sum(set)
result = 0

subset(0, 0)

if result == 1:
    print("YES")
else:
    print("NO")
