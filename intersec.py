l=[1,2,3,4]
m=[2,3,4,5]

print(list(set(l).intersection(m)))

r=set(l)-(set(l)-set(m))

print(list(r))


for i in l:
    if i in m:
        print(i)
        
kk=[i for i in l if i in m]
print(kk)
