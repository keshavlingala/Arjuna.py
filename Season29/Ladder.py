def isequidistant(l):
    s=set()
    for i in range(len(l)-1):
        s.add(l[i+1]-l[i])
    return len(s) == 1
steps=[int(a) for a in input().split()] #input here
count=0
for k in range(3,len(steps)+1): #checking for all possible sizes from 3 to size of list (max)
    for j in range(len(steps)-k+1): # for each size-k list of size n has n-k+1 possible subsets
        if isequidistant(steps[j:j+k]): # if the sublist of size k is equisistant then count++
            count+=1
print(count)










# Question Correction and full Solution
# if there is a list 
# 2 3 4 5 6
# the possible ladders of equidistent are (2,3,4) (3,4,5) (4,5,6) (2,4,6)
#                                         (2,3,4,5) (3,4,5,6) (2,3,4,5,6) counted 7
# where (2,4,6) combination is ignored in the question and testcases also
# if that is also considered below is the correct answer
# =============================================================================
# import itertools
# def isequidistant(l):
#    s=set()
#    for i in range(len(l)-1):
#        s.add(l[i+1]-l[i])
#    return len(s) == 1
# l=[int(a) for a in input().split()]
# count=0
# for i in range(3,len(l)+1):
#     for j in itertools.combinations(l,i):
#         if equidistant(j): # if steps[j:k] is equidistint count++
#             count+=1
# print(count)
# =============================================================================
