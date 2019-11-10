n=int(input())
s=[int(i) for i in input().split()]
tot=0
s=sorted(s,reverse=True)
for i in range(len(s)):
    p=pow(2,i)*s[i]
    tot=tot+p
print(tot)