import heapq

N=int(input())
limit=list(map(int,input().split()))
M=int(input())
W=list(map(int,input().split()))

lim=[]
min_w=[]
W.sort()
cnt=0

for ii in W:
    heapq.heappush(min_w,ii)


while min_w:
    # a=heapq.heappop(min_w)
    for k in range(N):
        a=heapq.heappop(min_w)
        if limit[k]>a :
            cnt+=0
        else:
            print(-1)
        if len(min_w) ==0:
            break
        
    # heapq.heappush(min_w,M)

    cnt+=1    

print(cnt)       
