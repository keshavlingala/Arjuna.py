# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:44:50 2019

@author: sanjana
"""
m,r=list(map(int,input().split()))

a=[int(g)for g in input().split()]
a.reverse()

c=0
p=1
prime=[]
d=[]
nd=[]

while(c<r):
    p=p+1
    f=0
    for j in range(1,p+1):
        if(p%j==0):
            f=f+1            
    if f==2:
        c=c+1
        prime.append(p)

for i in prime:
    e=[]
    f=[]
    print('check prime ',i)
    for j in range(len(a)):
        print('checing ',j)
        if(j%i==0):
            e.append(a[j])
            a.remove(a[j])
            j-=1
            print('e',e)
            print('a',a)
    e.reverse()
    d.extend(e)
print(d)
print(a)