#mergssort
#time complexity => O(nlogn)

list = [3,4,6,8,7,1,9,2,0]

def mergeSort(list):
    if len(list) <= 1:
        return

    mid = len(list) // 2
    leftArr = list[:mid]
    rightArr = list[mid:]

    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)

    return merge(leftArr,rightArr)

def merge(left,right):
    result = []

    while len(left) >0 or len(right) > 0 :
        if len(left) > 0 and len(right) >0:
            if left[0] >= right[0]:
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]

        elif len(left) >0:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    return result

mergeSort(list)

print(list)