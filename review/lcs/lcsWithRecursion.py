import sys
Input = sys.stdin.readline


def find(x,y,n,m):
    if not n or not m:
        return 0

    if x[n] == y[m]:
        return 1+find(x,y,n-1,m-1)
    else:
        return max(find(x,y,n-1,m),find(x,y,n,m-1))

x = Input()
y = Input()

print(find(x,y,len(x)-1,len(y)-1))

