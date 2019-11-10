suspects,talks=map(int,input().split())

kp={}
for i in range(talks):
    k,v=map(int,input().split())
    kp[k]=v
    
murder=[i for i in range(1,suspects+1) if i not in kp]
#print(murder)
if any(murder):
    print(murder[0])
else:
    print('-1')