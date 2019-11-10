# =============================================================================
# # =============================================================================
import numpy as np
# # a=np.array([[1,2,3],[4,5,6]])
# # print(a.shape) # size of the matrix
# # print(a.strides) # 
# # print(a.ndim) # number of dimentions
# # print(a.data) #address
# # print(a.size) #size
# # print(a.itemsize) #each item sizze
# # print(a.nbytes) # number of bytes of the object
# # print(a.flags) # information flags
# # print(a.T) #transpose
# # print(a.dtype) # data typeL
# # 
# # =============================================================================
# 
# a=np.array([[1,2],[4,5]])
# b=np.array([[1,0],[0,1]])
# #print(a)
# #print(b)
# #print('a+b',a+b,sep='\n')
# #print('a-b',a-b,sep='\n')
# #print('a * b',a*b,sep='\n')
# #print('a dot b',a.dot(b))
# #print('a.sum',a.sum())
# #print('a.sum(1)',a.sum(1))
# #print('a.sum(0)',a.sum(0))
# #print('a.max(0)',a.max(0))
# #print('a.max(1)',a.max(1))
# #print('a.cumsum()',a.cumsum())
# #print('a.mean()',a.mean())
# #print('a.var()',a.var())
# #print('b.all()',b.all())
# #print('a.all()',a.all())
# #print('b.any()',b.any())
# #print('a.any()',a.any())
# a=np.arange(9).reshape(3,3).T
# print(a)
# print('sorted a',a.sort())
# print(a)
# print(np.sort(a))
# 
# =============================================================================
A=np.matrix([[1,2,3],[-5,4,2],[7,-9,8]])
B=np.matrix([[2,3,4],[5,6,1],[2,4,5]])
m1=np.matrix(A)
m2=np.matrix(A).T
print(m1)
# =============================================================================
# print(m1)
# print(A[1])
# print(m1[:,1])
# 
# 
# =============================================================================
print(m1*m2)
print(m1.I * m1)
print(np.linalg.matrix_rank(m1))
print(np.linalg.det(m1))
print(A.I*B)

Ax=B

x=np.linalg.solve(A,B)
print(x)