import sys
Input = sys.stdin.readline

n = int(Input())

for _ in range(n):
    day = int(Input())
    price = list(map(int,Input().split()))

    earn = 0
    high = price[-1]

    for i in range(day, 0, -1):
        if price[i-1] > high:
            high = price[i-1]
        else:
            earn += ( high - price[i-1] )

    print(earn)