arr=[7,4,5,3,8,1,0,2,3,6,3]
for i in range(len(arr)):
  min_index=i
  for j in range(i+1,len(arr)):
    if arr[min_index]>arr[j]:
      min_index=j
  arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)