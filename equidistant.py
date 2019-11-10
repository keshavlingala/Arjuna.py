l=[1,2,3,4,5,7]
d=l[1]-l[0]
s={d}
for i in range(len(l)-1):
    print('i',i)
    s.add(l[i+1]-l[i])
if len(s) == 1:
    print('single')
else:
    print(s)
    print('not single')