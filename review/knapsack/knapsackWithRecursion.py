#Knapsack with recursion
import sys
Input = sys.stdin.readline

# P means profit and W means Weight
P = [1, 2, 5, 6]
W = [0, 3, 4, 5]

#Max capacity of the backpack is m


def knapsack(P,W,m,n):
    #n is index

    #stop condition
    if n == 0 or m == 0:
        return 0

    if W[n-1] <= m:
        return max(P[n-1] + knapsack(P,W,m-W[n-1],n-1),knapsack(P,W,m,n-1))
    else:
        return knapsack(P,W,m,n-1)


