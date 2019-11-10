r=int(input())
c=int(input())
park=[[int(j) for j in input().split()[:c]] for i in range(r)]
print(park)