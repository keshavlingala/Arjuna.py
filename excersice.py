ns=int(input())
nsub=int(input())
marks=[]
names=[]
for j in range(ns):
    names.append(input())
    for i in range(nsub):
        marks.append(int(input()))
    print(' marks are:')
    print(marks)
    marks.clear()
 