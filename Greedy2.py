n,m,k=map(int, input().split())
num=list(map(int, input().split()))
num.sort(reverse=True)
sum=0
while m:
  for _ in range(0,k):
    sum += num[0]
    m-=1
  sum += num[1]
  m-=1
print(sum)