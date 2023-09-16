# 1. 탐색 시작 노드를 스택에 삽입하고 방문처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 스택에 넣고 방문처리.
# -> 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드 꺼내기
# 3. 더이상 수행할 수 없을때까지 반복
# 방문하지 않은 인접노드가 여러개면 번호 낮은 순서로

def dfs(graph, v, visited):
  
  visited[v]=1 # 현재 노드를 방문 처리
  print("현재 노드 : ",v)
  print("graph[v] : ",graph[v])
  for i in graph[v]:
    if visited[i]!=1:
      print("not yet visited in graph[v] : ", i)
      print("visited : ",visited)
      print("")
      dfs(graph, i, visited)

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[0]*9
dfs(graph,1,visited)