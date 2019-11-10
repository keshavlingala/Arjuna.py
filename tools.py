import sys
import itertools as t

fruits=[int(a) for a in input().split()]
noff=int(input())
p={}
for i in range(noff):
    p[i]=[int(a) for a in input().split()]

for x in range(len(fruits)):
    lastIndex=len(p.keys())
    p[lastIndex]=[0]*(len(fruits)+1)
    p[lastIndex][x]=1
    p[lastIndex][len(fruits)]=fruits[x]

reqd=[int(a) for a in input().split()]

def sati(l):
    check=[0]*len(reqd)
    cost=0
    for i in range(len(reqd)):
        for pe in l:
            check[i]+=p[pe][i]
        if check[i] != reqd[i]:
            return False
    for j  in l:
        cost+=p[j][-1]
    return cost
        
g=[]
for offeri in p:
    m=sys.maxsize
    for j in range(len(reqd)):
        try:
            if (reqd[j]/p[offeri][j])<m:
                m=int(reqd[j]/p[offeri][j]) 
        except ZeroDivisionError:
            pass
   
    g.extend([offeri]*m)

def max_frequent(List): 
    max_freq = 0
    for i in List: 
        curr_max_frequency = List.count(i) 
        if(curr_max_frequency> max_freq): 
            max_freq = curr_max_frequency 
    return max_freq

minCost=sys.maxsize
k=[]
for i in range(max_frequent(g)+1):
    for combi in t.combinations(g,i):
#        print(list(combi))
        if sati(combi)!=False:
            k.append(sati(combi))
        
print(min(k))