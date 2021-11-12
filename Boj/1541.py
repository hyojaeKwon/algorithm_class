import sys
Input = sys.stdin.readline

calStr = Input().split('-')

minus = []
#마이너스를 기준으로 계산, 즉 더하기 값들을 미리 계산한 후 마지막에 빼준다.
for i in calStr:
    cnt = 0
    str = i.split('+')
    for j in str:
        cnt+=int(j)
    minus.append(int(cnt))

for i in range(1,len(minus)):
    minus[0] -= minus[i]

print(minus[0])
