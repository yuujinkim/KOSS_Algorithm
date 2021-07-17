# 이분탐색
[(이코테) 이진탐색](https://youtu.be/94RC-DsGMLo)

이진 탐색: 정렬되어 있는 리스트에서 __탐색 범위를 절반씩 좁혀가며 데이터를 탐색__ 하는 방법
 (시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정)
 
 ```
 # 이진 탐색 소스코드 구현 (반복문)
 def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
            
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid-1
            
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid+1
            
    return None
```

## 파이썬 이진 탐색 라이브러리
* bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
* bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

## 값이 특정 범위에 속하는 데이터 개수 구하기
```
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
```


---


# [3079번 (입국심사)](https://www.acmicpc.net/problem/3079)

#### 시간 초과
```
N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]

start = 0
end = min(T)*M

while start <= end:
    total = 0
    mid = (start+end)//2
    for i in T:
        total += mid//i

    if total >= M:
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)
```
line 12, 
__int(input())을 이용하여 입력을 받아서 시간 초과__

## 파이썬 입력 받기 (sys.stdin.readline)
### input() 대신 sys.stdin.readline()을 사용하는 이유
한두 줄 입력받는 문제들과 달리, 반복문으로 여러 줄을 입력받아야 할 때는 input()으로 입력받는다면 시간초과가 발생할 수 있다.

#### 정답 코드
```
import sys

N, M = map(int, input().split())
T = [int(sys.stdin.readline()) for _ in range(N)]

start = 0
end = min(T)*M

while start <= end:
    total = 0
    mid = (start+end)//2
    for i in T:
        total += mid//i

    if total >= M:
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)
```
