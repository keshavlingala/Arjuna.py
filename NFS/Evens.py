n=input()
p=[int(d) for d in str(n)]
for j in range(len(p)):
    count=0
    f=0
    for i in range(j,len(p)):
        if(p[i]<0):
            f=1
            break
        elif(p[i]%2==0):
            count=count+1
    if(f==1):
        print(-1)
        break
    else:
        print(count,end=" ")