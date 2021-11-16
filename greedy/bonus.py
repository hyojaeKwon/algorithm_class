import sys
Input = sys.stdin.readline

def bouns(eva):
    pay = 0
    payTable = [1]*len(eva)
    minValue=0
    for i in range(len(eva)-1):
        if eva[i+1]>eva[i]:
            payTable[i+1]=payTable[i]+1

        elif eva[i+1]==eva[i]:
            if payTable[i+1]-1 < minValue:
                payTable[i + 1] = payTable[i]
                minValue = payTable[i+1]
            else:
                payTable[i + 1] = payTable[i] - 1
        else:
            payTable[i+1]=payTable[i]-1
            if minValue > payTable[i+1]:
                minValue = payTable[i+1]

    minValue = 1-minValue
    for i in range(len(eva)):
        pay+=1000*(payTable[i]+minValue)
    return pay


eva = list(map(int,Input().split()))
print(bouns(eva))


