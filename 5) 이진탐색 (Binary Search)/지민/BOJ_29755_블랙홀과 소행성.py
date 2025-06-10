import sys
input=sys.stdin.readline
def b_s(A,k):
    l,r=0,len(A)
    m=(l+r)//2
    if k<A[m]:
        r=m-1
    elif k>A[m]:
        l=m+1
    else:
        return m
    
N,M=map(int,input().split())

black=list(map(int,input().split()))

so_dis=[]
so_weight=[]

for _ in range(M):
    a,w=map(int,input().split())
    so_dis.append(a)
    so_weight.append(w)

List=[]
for i in range(N):
    for j in range(M):
        # if black[i]-so_dis[j]>=0:
        #     List.append(so_weight[j]*(black[i]-so_dis[j]))
        # else:
        #     List.append(so_weight[j]*(so_dis[j]-black[i]))
        List.append(so_weight[j]*abs(black[i]-so_dis[j]))


ll=sorted(List)

ppp=[]
for P in ll:
    pp=b_s(ll,P)
    if pp !=None:
        ppp.append(pp)

print(min(ppp))

