types,pairs=map(int,input().split())
nstones=list(map(int,input().split()))
# if solution exists only when it reaches the target 
# total pairs can be formed is less than target print -1 else
#the solution is simply pairs*2 + number of types-1
print(-1 if sum(stone//2 for stone in nstones)<pairs else pairs*2+types-1)