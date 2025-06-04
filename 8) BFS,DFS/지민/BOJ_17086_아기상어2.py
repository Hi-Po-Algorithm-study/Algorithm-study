import heapq
N,M=map(int,input().split())
for _ in range(N):
    lst=list(map(int,input().split()))
    # print(lst)
dx=[0,1,1,0,0,1,-1,-1]
dy=[0,0,1,1,-1,-1,0,1]

for i in range(8):
    nx=dx[i]
    ny=dy[i]

L=[]
visited=[[0]*M for _ in range(N)]
L.append(lst[0])
visited[0][0]=1
print(visited)
while(L):
    shark=heapq.heappop(L)
    if shark==0 and visited[]:
        

    