import sys
Input = sys.stdin.readline

n,m = map(int,Input().split())
money = []
for i in range(n):
    money.append(int(Input()))

money.sort(reverse=True)
count = 0
i=0
while(True):
    if m >= money[i]:
        m -= money[i]
        count+=1
    else:
        i+=1
    if i == n or m <= 0:
        break

print(count)
