import itertools
n=int(input())
t=int(input())
l=list(map(int,input().split()))
f=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    l3=[l[i],f[i]]
    l1.append(l3)
c=0
for i in range(1,len(l1)+1):
    comb=list(itertools.combinations(l1,i))
    for i in comb:
        ans=0;ans1=0
        for j in i:
            ans+=j[0];ans1+=j[1]
        if(ans<=n and ans1>=t):
            print('satified',j)
            c+=1
print(c)