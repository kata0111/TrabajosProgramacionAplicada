import math
A=[1,2,3]
B=[4,5,6]
C=[5,7,9]
n=len(A)
total=sum((A[i]*B[i])+C[i]for i in range(n))+n**2
print (total)
