# Quick Sort
# Devide and counqer in recursion


#key middle version
list = [3, 2, 4, 2, 1, 5, 7, 6]


def quickSort(list, start, end):
    # 종료조건
    if not (start < end):
        return

    key = (start+end)//2
    i = start
    j = end

    while i <= j:
        # key보다 큰 값을 찾는다.
        while (i <= end and list[key] >= list[i]):
            i += 1
        # key보다 작은 값을 찾는다.
        while j > start and list[key] <= list[j]:
            j -= 1

        if i > j:
            if i < key:
                temp = list[i]
                list[i] = list[key]
                list[key] = temp
            elif j > key:
                temp = list[j]
                list[j] = list[key]
                list[key] = temp
        else:
            # 엇갈리지 않았더라면 i와 j교체
            temp = list[j]
            list[j] = list[i]
            list[i] = temp


    quickSort(list, start, j - 1)
    quickSort(list, j + 1, end)


quickSort(list, 0, len(list) - 1)
print(list)