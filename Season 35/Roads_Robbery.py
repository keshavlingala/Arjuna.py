from functools import lru_cache
n,conn=map(int,input().split())
diamonds=dict(zip(range(1,n+1),map(int,input().split())))
#taking diamonds of kingdoms in a dictionary of respective kingdom
adj={k:list([k]) for k in range(1,n+1)}
#creating an adjucency kingdoms list for all the kingdoms
#adding adjuscency list items below
for i in range(conn):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
#caching repediately calling function to implement dynamic programming  
@lru_cache(maxsize=128)
def removeDup(x):
    fil=[]
    for a in list(map(set,x)):
        if a not in fil:
            fil.append(a)
    return tuple(fil)
#applying lru caching to implement dynamic programming for a recursive function improves the effecency to maximum
@lru_cache(maxsize=128)
def findWays(selections,selected):
    #having a list of available selecetions and already selected kingdoms to rob
    #if there are nothing to select anymore returning a list of selected kingdoms
    if not any(selections):
        return [tuple(selected)]
    #for each kingdom applying recursively the same function to find the maximum value for robbery
    available=[]
    for k in selections:
        #for each selected kingdom remove it's adjucent kingdoms from the selections list and add the selected kingdom to selected list
        #continue with th recursion
        available.extend(findWays(tuple(set(selections)-set(adj[k])),selected+tuple([k])))
    #creating a dictionary for each availeble possibles and value as its key
    #then find the max key (max profit) then return the list of lists with max profit only
    d=dict({tuple(k):sum(diamonds[i] for i in k) for k in available })
    ans=[k for k,v in d.items() if v==max(d.values())]
    #remove duplicated as the order of the selected kingdoms doesn't matter
    del available,d,k
    return removeDup(tuple(ans))

ansList=findWays(tuple(range(1,n+1)),tuple([]))
# here we the list of all possible kingdoms list with max profit they can earn and max kingdoms
c=len(ansList)
#number of ways are the size of the list
c+=list(diamonds.values()).count(0)*2
#if there are any kingdoms with 0 diamonds then robbing it not robbing it are more possibilities weather it's available of not
print(sum(diamonds[k] for k in ansList[0]),c)
#finally calculating the profit of diamonds can be earned and number of ways
