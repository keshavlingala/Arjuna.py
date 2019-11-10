p,q=map(int,input().split()[:2])
#d=dict(zip(range(1,p+1),[0]*p))
tot=0
for i in range(q):
    s,e,v=map(int,input().split())
    tot+=v*(e-s+1)
#    for j in range(s,e+1):
#        d[j]=d[j]+v
#print(sum(d.values())//p)
print(tot//p)