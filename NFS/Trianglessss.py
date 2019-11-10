import functools as f
n=int(input())
@f.lru_cache(maxsize=128)
def isTri(sides):
    a,b,c=sides
    return (a < b + c) and (b < a + c) and (c < a + b)
import itertools as tool
items=list(map(int,input().split()))
sol=0
for sides in tool.combinations(items,3):
    if isTri(sides):
        sol+=1
print(sol)