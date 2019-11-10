import itertools
x=int(input())
for i in range(25):
    for k in itertools.product("LD",repeat=i):
        dp=0;lf=1
        for j in k:
            if(j=="L"):
                dp+=lf
                lf*=2
            elif(j=="D"):
                if(lf>0): lf=-1
                else: lf=1
        if(dp==x):
            print(len(k))
            exit(0)