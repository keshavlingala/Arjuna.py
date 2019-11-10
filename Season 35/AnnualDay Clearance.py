result=[]
for i in range(int(input())):
     N,T,S,U=list(map(int,input().split()))
     if(T<U):
         result.append(-1)
     else:
         if(U==1):
             result.append(N*T)
         else:
             maxresult=-1
             for o in range((S-1)//(U-1),0,-1):
                 h=S+(o-1)-o*(U-1)
                 rest=(N-h)//o
                 l=(N-h)%o
                 if(rest>T-1) or (rest==T-1 and l>0):
                     break
                 res=h*T+o*(2*T-rest-1)*rest//2+l*(T-rest-1)
                 if(maxresult>=res):
                     break
                 maxresult=res
             result.append(maxresult)
for x in result:
    print(x)