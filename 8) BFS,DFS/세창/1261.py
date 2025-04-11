import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split()) # n:세로, m:가로
miro=[list(map(int,input().strip())) for _ in range(n)]

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

cnt=[] # 벽 부순 횟수
cnt[0][0]=0 # 시작 위치는 벽 없음

q=deque()

def bfs(x,y):
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        
        # 미로 밖 나갈 경우
        if not (0 <= nx < n and 0 <= ny < m):
            continue

        # 벽이 없을 때(0)
        # 벽이 있을 때(1)

print(cnt[n-1][m-1])