#insertion sorting
#O(n^2)

arr = [2,5,1,6,4,8,7,9]

for i in range(1,len(arr)):
  key = arr[i]
  j = i - 1
  #finding the point to insertion
  while j>=0 and key<arr[j]:
    arr[j+1] = arr[j]
    j = j - 1

  #assignment the value of key  
  arr[j+1] = key

print(arr)
