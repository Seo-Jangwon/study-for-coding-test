arr=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
  #리스트의 원소가 하나 이하면 종료
  if len(arr) <= 1:
    return arr

  pivot = arr[0] # 피벗은 첫 번째 원소
  tail = arr[1:] # 피벗을 제외한 리스트
  
  left_side = [x for x in tail if x<=pivot]
  right_side = [x for x in tail if x>pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(arr))