c=[]
for i in range(int(input())):
    c.append(list(map(int,input().split())))
c.sort(key=lambda x:x[1])
s=0
coupons=0
for x in c:
    if x[0]+s<=x[1]:
        s+=x[0]
        coupons+=1
print(coupons)