
pos=input()
y=['1','2','3','4','5','6','7','8']
x=['a','b','c','d','e','f','g','h']
posx=0
posy=0
count=0
for i in range(len(y)):
  if y[i] in pos:
    posy=i

for i in range(len(x)):
  if x[i] in pos:
    posx=i 

if posx<=5 and posy>=1: #오른2 위1
  count+=1
if posx<=5 and posy<=6: #오른2 아래1
  count+=1
if posx>=2 and posy>=1: #왼2 위1
  count+=1
if posx>=2 and posy<=6: #왼2 아래1
  count+=1
if posx<=6 and posy>=2: #오른1 위2
  count+=1
if posx<=6 and posy<=5: #오른1 아래2
  count+=1
if posx>=1 and posy>=2: #왼1 위2
  count+=1
if posx>=1 and posy<=5: #왼1 아래2
  count+=1
print(count)
"""
input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
result=0
for step in steps:
  next_row=row+step[0]
  next_column=column+step[1]
  if next_row >=1 and next_row<=8 and next_column>=1 and next_column<=8:
    result +=1
print(result)
"""