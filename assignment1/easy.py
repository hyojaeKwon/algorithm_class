import sys
Input = sys.stdin.readline

nums = list(map(int,Input().split()))
target = int(input())

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    leftArr = nums[:mid]
    rightArr = nums[mid:]
    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)
    return merge(leftArr,rightArr)

def merge(left,right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def findTarget(numsArr, target):
    for i in range(len(numsArr)):
        if target == numsArr[i] or target < numsArr[i]:
            return i + 1

def solve(nums, target):
    numsArr = mergeSort(nums)
    print(findTarget(numsArr, target))

solve(nums, target)