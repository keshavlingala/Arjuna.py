trucks=[int(i) for i in input().split()]
if(sum(trucks)%len(trucks)!=0):
    print(-1)
else:
    target=sum(trucks)//len(trucks)
    reqmoves=0
    for i in trucks:
        print('diff',target-i)
        reqmoves+=abs(target-i)
        print('moves',reqmoves)
    print(reqmoves//2)