# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 2를 더이상 수행할 수 없을때까지 반복
# 방문하지 않은 인접노드가 여러개면 번호 낮은 순서로
# 최단거리 문제
from collections import deque

def bfs(graph, start, visited):
  
  queue=deque([start]) # queue 구현을 위해 deque 라이브러리 사용
  visited[start]=1 # 현재 노드 방문 처리
  while queue: # 큐가 빌 때까지
    v=queue.popleft() # 큐의 원소 하나씩 뽑기
    print(v,end=' ')
    for i in graph[v]: # 해당 원소와 연결 
      if visited[i] != 1: # 되지 않은 원소들을
        queue.append(i) # 큐에 삽입
        visited[i]=1


graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[0]*9
bfs(graph,1,visited)
