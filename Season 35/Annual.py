ans=[]
for i in range(int(input())):
     N,T,S,U=[int(i) for i in input().split()]
     if(T<U):
         ans.append(-1)
     else:
         if U == 1:
             res = N*T
         else:
             res = 0
             for i in range(1,N+1):
                 m=S-1-i*(U-1)
                 if m < 0: break
                 v = max(0,T-((N-m)/i))
                 ln = (T-v)*i + m
                 if ln < N and v == 0: continue
                 total = (T-v)*(T-v+1)/2 * i - (T-v)*(N-m) + T*N
                 res = max(res, total)
         ans.append(res or -1)
for i in ans:
    print(i)