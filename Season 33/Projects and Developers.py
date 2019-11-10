import itertools as tool
nDev=int(input())
met=int(input())
estiD=[int(i) for i in input().split()]
worths=[int(i) for i in input().split()]
d=dict(zip(range(len(estiD)),zip(estiD,worths)))
soln=0
for i in range(1,len(d)+1):
    for j in tool.combinations(d.keys(),i):
        dev=sum(d[k][0] for k in list(j))
        earn=sum(d[k][1] for k in list(j))
        if dev<=nDev and earn>=met:
            soln+=1
print(soln)