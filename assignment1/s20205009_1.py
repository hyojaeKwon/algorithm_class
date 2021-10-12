
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    lArr = nums[:m]
    rArr = nums[m:]
    lArr = mergeSort(lArr)
    rArr = mergeSort(rArr)
    return merge(lArr,rArr)

def merge(l,r):
    result = []
    while len(l) > 0 or len(r) > 0:
        if len(l) > 0 and len(r) > 0:
            if l[0] >= r[0]:
                result.append(r[0])
                r = r[1:]
            else:
                result.append(l[0])
                l = l[1:]
        elif len(l) > 0:
            result.append(l[0])
            l = l[1:]
        elif len(r) > 0:
            result.append(r[0])
            r = r[1:]
    return result

def findTarget(numsArr, target):
    for i in range(len(numsArr)):
        if target == numsArr[i] or target < numsArr[i]:
            return i + 1
    return len(numsArr) + 1

def solve(nums, target):
    numsArr = mergeSort(nums)
    print(findTarget(numsArr, target))

