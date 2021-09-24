import sys
Input = sys.stdin.readline

nums = list(map(int,Input().split()))
target = int(input())

nums.sort()

#선형 탐색으로 위치 찾기
for i in range(len(nums)):
    if target == nums[i] or target < nums[i]:
        print(i + 1)
        break

