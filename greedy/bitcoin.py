import sys
Input = sys.stdin.readline

def bitCoin(price):
    result = 0

    maxPrice = price[-1]
    for i in range(len(price)-1,0,-1):
        if maxPrice < price[i-1]:
            maxPrice = price[i-1]
        else:
            result += (maxPrice - price[i-1])
            maxPrice = price[i-1]

    return result


bit = list(map(int,Input().split()))
print(bitCoin(bit))