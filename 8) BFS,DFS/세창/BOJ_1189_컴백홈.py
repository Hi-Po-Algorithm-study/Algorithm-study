import sys
input=sys.stdin.readline


# 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,d):
    global ans

    # 목적지에 도착
    if x==0 and y==c-1 and d==k: # 딱 k만큼 이동했을 때
        ans+=1
        return
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and graph[nx][ny]!='T':
                visited[nx][ny]=True
                dfs(nx,ny,d+1) # 다음으로 이동
                visited[nx][ny]=False


################################################################################################
            
r,c,k=map(int,input().split())
graph=[list(input().strip()) for _ in range(r)]

visited=[[False]*c for _ in range(r)]

ans=0 

visited[r-1][0]=True

# 출발
dfs(r-1,0,1)

print(ans)