n=int(input())
d=dict()
for i in range(n):
    k,v=map(int,input().split())
    d[k]=v

d1={}
for key,value in d.items():
    if value in d1:
       d1[value]=min(d1[value],key)
    else:
        d1[value]=key
        
for k in sorted(d1):
    print(k,d1[k])