import sys
Input = sys.stdin.readline

table = []
n = int(input())
for i in range(n):
    temp = list(map(int,Input().split()))
    temp.append(0)
    table.append(temp)

table.sort(key=lambda x: (x[1], x[2]))

classRoom = 0
classCount = 0


while classCount < n:
    classCount += 1
    table.pop(0)
    end = table[0][2]
    for i in range(1,len(table)):
        if end < table[i][1] and not table[i][3]:
            end = table[i][2]
            table[i][3] = 1
            classCount += 1

    classRoom+=1

print(classRoom)




