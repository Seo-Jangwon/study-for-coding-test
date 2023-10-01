n=int(input())

arr=[]
for i in range(n):
  inputdata=input().split()
  arr.append((inputdata[0],int(inputdata[1])))

arr = sorted(arr,key=lambda index:index[1])

for student in arr:
  print(student[0], end=' ')