n=int(input())
strlist=list(input().split())
x=0
y=0
for i in strlist:
  if i == "L":
    if x>0:
      x-=1
  elif i == "R":
    if x<(n-1):
      x+=1
  elif i == "U":
    if y>0:
      y-=1
  elif i == "D":
    if y<(n-1):
      y+=1
print(y+1,x+1)