from functools import lru_cache
#using dynamic programming approach
#cacheing the recursive functions results using LRU cache reduces the time complexity of recursion
n,levels,coins=map(int,input().split())
costs=[0]
costs.extend(list(map(int,input().split())))
prices=list(map(int,input().split()))
@lru_cache(maxsize=128)
def findMax(n,coins):
#    if he sold all the required idols
    if n<=0:
        return coins
#    in current position buy all the available level of idols if possible and continue to next idol
    available=[]
    for i in range(len(costs)):
        if coins>=sum(costs[:i+1]):
            available.append(findMax(n-1,coins-sum(costs[:i+1])+prices[i]))
#    return max profit of all the idols
    return max(available)
print(findMax(n,coins))