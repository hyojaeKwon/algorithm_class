import sys
Input = sys.stdin.readline

list = [3,2,4,2,1,5,7,6]

for i in range(len(list) -2):
    min = i
    for j in range(i+1,len(list)):
        if list[j] < list[min]:
            min = j
    if min != i:
        temp = list[i]
        list[i] = list[min]
        list[min] = temp

print(list)



