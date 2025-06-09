from collections import deque
M,N,K=map(int,input().split())

l=[list(map(int,input().split()))for _ in range(K)]

d=[(0,1),(1,0),(0,-1),(-1,0)]

def bfs(y,x):
    q=deque()
    visit=[[0]*N for _ in range(M)]

    while q:
        y,x=q.pop(left)
        for dy,dx in d:
            X=x+dx
            Y=y+dy
        if 0<=X<N and 0<=Y<M and visit[Y][X]==0:
            q.append((Y,X))
            visit[Y][X]==1

cnt=0
for i in range(K):
    if l[i][0]==0 :
        cnt+=1
    elif l[i][2]==N :
        cnt+=1
    elif l[i][1] ==0:
        cnt+=1
    elif l[i][3]==M:
        cnt+=1

print(cnt)

for i in range(M):
    