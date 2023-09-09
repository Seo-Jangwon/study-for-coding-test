n, m= map(int, input().split())
result=0
for i in range(n):
  data=list(map(int, input().split()))
  if result<min(data):
    result=min(data)

print(result)
  
