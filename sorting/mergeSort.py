#This is merge sort
# The time complexity of merge sort is O(NlogN)

#the initial list
arr = [2,5,1,6,4,8,7,9]
sortedArr = []

def merging(arr,left,mid,right):
  i = left
  j = mid+1
  
  #Select the small value
  while((i<=mid) and ( j <= right)):
    if(arr[i]<=arr[j]):
      sortedArr.append(arr[i])
      i+=1
    else:
      sortedArr.append(arr[j])
      j+=1

  if(i>mid):
    for k in range(j,right):
      sortedArr.append(arr[k])
  else:
    for k in range(i,right):
      sortedArr.append(arr[k])
  
  print(sortedArr,left,right)
  for k in range(left,right):
    arr[k] = sortedArr[k]
      
def mergeSort(arr,left,right):
  if(left<right):
    #Finding the middle site
    mid = int((left + right)/2)
    
    #Dividing the list
    mergeSort(arr,left,mid)
    mergeSort(arr,mid+1,right)
    merging(arr,left,mid,right)


mergeSort(arr,0,len(arr)-1)
print(arr)
  