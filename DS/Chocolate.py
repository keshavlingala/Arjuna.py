c=[int(a) for a in input().split()]
while len(c)>=2:
    c.sort()
    a=c.pop()
    b=c.pop()
    diff=a-b
    if diff !=0:
        c.append(diff)
        c.sort()
print(c.pop())