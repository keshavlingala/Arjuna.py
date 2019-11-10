def isSafe(i,j): # checking if a land can be bought or not
    l=[]
    r=[]
    for k in range(0,i):
        if matrix[k][j]==1:
            l.append(matrix[k][j]) 
    for k in range(i,width):
        if matrix[k][j]==1:
            r.append(matrix[k][j])
    # it's left side and right side should contain aleast one 1 i.e block then safe to buy
    return any(l) and any(r)
        
        
heights=[ int(a) for a in input().split() ] #input
width=len(heights) #max width of bars
maxheight=max(heights) # max height of bars
land=0 #land more to be evaluated
matrix=[[1  if j in range(maxheight-heights[i],maxheight) else 0 for j in range(maxheight)] for i in range(width)]
# creating a matrix with bought land and 1 and non non bought land as 0
for i in range(width):
    for j in range(maxheight): # iterating throught 2d matrix (list of lists)
        if matrix[i][j]==0 and isSafe(i,j): #if the land is not bought and is good be bought then count ++
            land+=1

print(land)
