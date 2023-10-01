n,k=map(int,input().split())
arr_a=list(map(int,input().split()))
arr_b=list(map(int,input().split()))
maxa=0
temp_arr=[]

arr_a.sort()
arr_b.sort(reverse=True)

for i in range(k):
  if arr_a[i]<arr_b[i]:
    arr_a[i],arr_b[i]=arr_b[i], arr_a[i]
    if(sum(arr_a)>maxa):
      maxa=sum(arr_a)
print(maxa)