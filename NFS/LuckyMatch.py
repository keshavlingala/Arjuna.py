K=input()
T=input()
print(sum(1 for x in T if x in K) if K.isalpha() and T.isalpha() and len(set(K))==len(K) else -1)