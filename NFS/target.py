import itertools as t
input()
target=int(input())
batsman=[int(a) for a in input().split()]

def findtarget():
    for i in t.combinations(batsman,2):
        print(i)
        if(i[0]+i[1]==target):
            a=batsman.index(i[0])
            del batsman[i[0]]
            batsman.index(i[1]+1)
            print(a,b)
            return False
    return True
if findtarget():
    print('-1')