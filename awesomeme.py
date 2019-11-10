import itertools
def equidistant(l):
    d=l[1]-l[0]
    s={d}
    for i in range(len(l)-1):
        s.add(l[i+1]-l[i])
    del d
    return len(s) == 1
l=[int(a) for a in input().split()]
count=0
for i in range(3,len(l)+1):
    for j in itertools.combinations(l,i):
        if equidistant(j): # if steps[j:k] is equidistint count++
            count+=1
print(count)