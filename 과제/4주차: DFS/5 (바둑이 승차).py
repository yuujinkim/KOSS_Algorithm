import sys


def max_weight(sum, level):
    if level == N:
        if sum <= C:
            sum_list.append(sum)
    else:
        max_weight(sum + W[level], level+1)
        max_weight(sum, level+1)


C, N = map(int, input().split())
W = [int(sys.stdin.readline()) for _ in range(N)]

sum_list = []
max_weight(0, 0)
print(max(sum_list))
