m,r=list(map(int,input().split()))
a=[int(i) for i in input().split()]
primes=[]
c=0
p=1
while(c<r):
    p=p+1
    f=0
    for j in range(1,p+1):
        if(p%j==0):
            f=f+1            
    if f==2:
        c=c+1
        primes.append(p)
del f,p,c,j

for prime in primes:
    b=[]
    for ele in a:
        if(ele%prime==0):
            print(ele)
        else:
            b.append(ele)
    a=b[::-1]
print(a)