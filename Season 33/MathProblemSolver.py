import itertools as it
n=map(int,input().split()[0])
digits=list(map(int,input().split()))
t=int(input().split()[0])
def findNumber():
    soln=None
    for i in range(n):
        for c in it.combinations_with_replacement(digits,i):
            for item in list(it.permutations(c)):
                num=int(''.join(map(str,item)))
                if num%t==0:
                    if soln:
                        soln=min(soln,num)
                    else:
                        soln=num
            if soln:
                return soln
def divisible(digits,t):
    if t==5 and (0 or 5) in digits:
        print(-1)
        exit(0)
#        TODO Check all the combinations best method
    return True
if divisible(digits,t):
    soln=findNumber()
    if soln:
        print(soln,soln//t)
    else:
        print(-1)