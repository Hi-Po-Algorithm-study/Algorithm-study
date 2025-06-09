import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(sy,sx):
    q=deque()
    q.append((sy,sx))
    visited[sy][sx]=True
    ans=1

    while q:
        y,x=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[ny][nx] and graph[ny][nx]==0:
                visited[ny][nx]=True
                q.append((sy,sx))
                ans+=1

###################################################################################

m,n,k=map(int,input().split())
graph=[[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())

    for y in range(y1,y2):
        for x in range(x1,x2):
            graph[y][x]=1


visited=[[False]*n for _ in range(m)]

area=[] # 빈 곳 넓이들 리스트

for y in range(m):
    for x in range(n):
        if graph[y][x]==0 and not visited[y][x]:
            result=bfs(y,x)

area.sort()

print(len(area))
# print()