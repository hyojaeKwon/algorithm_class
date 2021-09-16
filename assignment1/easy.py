#Programing assignment Plan EASY
import sys
Input = sys.stdin.readline
arr = list(map(int,Input().split()))
target = int(input())
arr.sort()

print(arr)
#Preparing Binary Search
left = 0
right = len(arr) - 1
while left<=right:
  mid = int(right // 2)
  if (arr[mid] == target):
    print(mid+1)
    break
  elif (arr[mid] > target):
    right = mid - 1
  else:
    left = mid + 1

  if arr[left] > target:
    print(left)
    break
  elif (arr[left+1] > target) and (arr[left] < target):
    print(arr[left+1])
    print(left+1)
    break

  if arr[right] < target:
    print(right+1)
    break
  elif (arr[right+1] < target and arr[right] > target):
    print(right)
    break