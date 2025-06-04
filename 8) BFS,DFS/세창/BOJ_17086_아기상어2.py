import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

# 상하좌우, 대각선
dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]

# 가장 안전한 거리
res=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            visited=[[-1]*m for _ in range(n)] # -1은 방문x
            q=[]
            q.append((i,j))
            visited[i][j]=0


            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]


                if graph[nx][ny]==1:
            

        
print(res)
