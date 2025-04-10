# T=int(input())
N=int(input())
Stock=list(map(int,input().split()))

P=[0 for _ in range(N-1)]
# P=[]
for i in range(N-1,-1,-1):
    if i==N-1:
        continue
    if Stock[i-1]<Stock[i] and i!=N-1:
        P[i-1]=Stock[i]
        
    # elif Stock[i-1]>Stock[i]:
        
    else:
        # P.append(0)
        continue
    # P.append(Stock[i-1])
print(P)