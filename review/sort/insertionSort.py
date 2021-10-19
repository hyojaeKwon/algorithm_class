list = [5,2,4,7,1,3,2,6]


for i in range(1,len(list)-1):
    j = i - 1
    key = list[i]

    while j >= 0 and key < list[j]:
        list[j+1] = list[j]
        j-=1

    list[j+1] = key

print(list)