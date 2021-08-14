# DFS/BFS: 그래프 탐색 알고리즘
[(이코테) DFS & BFS](https://youtu.be/7C9RgOcvkvo)

탐색: 많은 양의 데이터 중에서 __원하는 데이터를 찾는 과정__

## 재귀 함수
재귀 함수: 자기 자신을 다시 호출하는 함수
* 재귀 함수의 종료 조건을 반드시 명시해야 함
* 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
* 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓이게 됨.  
그래서 스택을 사용해야 할 때 구현상 __스택 라이브러리 대신에 재귀 함수를 이용__ 하는 경우가 많다.

## DFS (Depth-First-Search)
DFS: 깊이 우선 탐색 (그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘)  
스택 자료구조(혹은 재귀 함수)를 이용
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리.  
방문하지 않은 인접 노트가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복.

```
# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
```

## BFS (Breadth-First-Search)
DFS: 너비 우선 탐색 (그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘)  
큐 자료구조를 이용
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복.

```
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력하기
    v = queue.popleft()
    print(v, end=' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in  graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
```
