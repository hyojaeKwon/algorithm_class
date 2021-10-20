#Selection Sort


#time complexity O(n^2)
#n is the length of input list

list = [3,2,4,2,1,5,7,6]


#
for i in range(len(list)-1):
    min = i

    #find the smaller value
    for j in range(i+1,len(list)):
        if list[min] > list[j]:
            min = j

    # if i is not min -> interchange
    if min != i:
        temp = list[i]
        list[i] = list[min]
        list[min] = temp

print(list)



