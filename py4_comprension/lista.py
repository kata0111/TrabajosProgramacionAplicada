A=[4,6,8,2]
B=[2,1,0,-1]
n=len(A)//2
[A[i]*(A[2*i]-B[2*i+1])+B[n+i] for i in range(n)]