#This is merge sort
# The time complexity of merge sort is O(NlogN)

#the initial list
arr = [2,5,1,6,4,8,7,9]
sortedArr = []

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  left = 0
  right = len(arr)
  mid = len(arr) // 2

  leftArr = arr[left:mid]
  rightArr = arr[mid:] 
  leftArr = mergeSort(leftArr)
  rightArr = mergeSort(rightArr)
  return merge(leftArr,rightArr)



def merge(leftArr,rightArr):
  ansList = []
  while len(leftArr) > 0 or len(rightArr) > 0:
    if len(leftArr) > 0 and len(rightArr) > 0:
      if leftArr[0] < rightArr[0]:
        ansList.append(leftArr[0])
      else:
        ansList.append(rightArr[0])
    elif len(leftArr) > 0:
      ansList.append(leftArr[0])
      leftArr = leftArr[1:]
    elif len(rightArr) > 0:
      ansList.append(rightArr[0])
      rightArr = rightArr[1:]
  return ansList


print(mergeSort(arr))
