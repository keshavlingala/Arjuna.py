from functools import lru_cache
n=int(input())
coins=int(input())
golds=list(map(int,input().split()))
reqd=list(map(int,input().split()))
#caching recursive functions to apply memorizing technique using lru_cahce decorator in python
@lru_cache(maxsize=128)
def MaxCoins(n,coins,golds,reqd):
    if n==0:
        return coins
#    finding all the available boxes and proceed to next box by handling with current situations
    available=[]
    for i in range(len(reqd)):
        if(coins>=reqd[i]):
            g=list(golds)
            r=list(reqd)
            g.pop(i)
            r.pop(i)
#            when open a box removeing that box and reqd from the existing list and proceeding to next recursive function to find max
            available.append(MaxCoins(n-1,coins+golds[i],tuple(g),tuple(r)))
#    out of all availble profits return the max profits
    return max(available) if any(available) else coins
print(MaxCoins(n,coins,tuple(golds),tuple(reqd)))
