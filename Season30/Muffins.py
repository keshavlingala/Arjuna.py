def muffin(M,S):
    d=0
    floors=[0]*M+1
    while floors[M]<S:
        for i in list(range(M,0,-1)):
            floors[i]+=floors[i-1]+1
        d+=1
    return d
M,S=list(map(int,input().split()))
print(muffin(M,S))
