def binary(s,l,k):
    m=s+l//2
    
    if k<m:
        binary(s,m,k)
    elif k>m:
        binary(m,l,k)
    else:
        m=k
        return 1
        
    return 0       

N,M=map(int,input().split())
num=list(map(int,input().split()))

s=0
l=N

sum=[]

# for i in range(1,N+1):
#     s+=i
#     sum.append(s)
    
# s=sum[0]
# l=sum[N-1]
# k=
# binary(s,l,k)

# print(sum)

for i in num:
    s+=i

