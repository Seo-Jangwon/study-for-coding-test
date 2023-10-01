array=[1,5,6,7,9,3,2,44,23,6,3,2,7,1,4,6,8,1,0,7,6]
count=[0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]]+=1
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
