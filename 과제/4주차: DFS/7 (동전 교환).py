def change(sum, cnt):
    global min
    if sum > M or cnt > min:
        return
    if sum == M:
        if cnt < min:
            min = cnt
    else:
        for i in coin:
            change(sum+i, cnt+1)


N = int(input())
coin = list(map(int, input().split()))
M = int(input())

sum = 0
cnt = 0
min = 100000000

change(0, 0)
print(min)
