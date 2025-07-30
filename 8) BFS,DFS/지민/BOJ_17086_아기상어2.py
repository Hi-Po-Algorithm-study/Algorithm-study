import sys
from collections import deque

input=sys.stdin.readline
N,M=map(int,input().split())
lst= [list(map(int, input().split())) for _ in range(N)]

d=[(-1,-1),(-1,0), (-1,1),(0,1),(1,1),(1,0) ,(1,-1), (0,-1)]

def bfs(y,x):
    q=deque()
    visited=[[0]*M for _ in range(N)]
    is_shark=0
    while q:
        y,x=q.pop(left)
        for dy,dx in d:
            Y=y+dy
            X=x+dx
            if 0<=X<m and 0<=Y<n and visited[Y][X]==0:
                if lst[Y][X]==0:
                    q.append((Y,X))
                    visited[Y][X]=visited[y][x]+1
                else:
                    ans=visited[y][x]+1
                    is_shark=1
        if is_shark:
            break
    return ans

ans=0
for y in range(n):
    for x in range(m):
        if lst[]

# import heapq
# N,M=map(int,input().split())
# for _ in range(N):
#     lst=list(map(int,input().split()))
#     # print(lst)
# dx=[1,1,0,0,1,-1,-1,-1]
# dy=[0,1,1,-1,-1,0,1,-1]



# for i in range(8):
#     nx=dx[i]
#     ny=dy[i]

# L=[]
# visited=[[0]*M for _ in range(N)]
# L.append(lst[0])
# visited[0][0]=1
# print(visited)
# while(L):
#     shark=heapq.heappop(L)
#     if shark==0 and visited[]:
        
    