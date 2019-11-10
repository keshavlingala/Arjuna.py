# =============================================================================
# import numpy as np
# a=np.array([16,10,15,12,11])
# print(a)
# print('mean',np.mean(a))
# print('std',np.std(a))
# print('var',np.var(a))
# 
# =============================================================================
import numpy as np
import statistics as ss
a=np.array([5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,7])
print('Mean',a.mean())
print('Median',np.median(a))
print('Mode',ss.mode(a))
print('Variance',np.var(a))
print('Standard Deviation',np.std(a))
