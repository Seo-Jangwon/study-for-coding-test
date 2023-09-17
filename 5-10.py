n,m=map(int, input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False # 범위를 벗어나면 종료

  if graph[x][y]==0:
    graph[x][y]=1 # 방문처리
    dfs(x+1,y) #상, 하, 좌, 우 모두 방문
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

result=0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result+=1
print(result)
