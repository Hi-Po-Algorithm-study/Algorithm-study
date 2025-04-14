import sys
input=sys.stdin.readline

dx=[1,0] # 아래
dy=[0,1] # 오른쪽

goal=False

def dfs(x,y):
    
    global goal # 전역변수

    # 도착
    if board[x][y]==-1: 
        goal=True
        return
    
    move=board[x][y]

    # 방향이동
    # 아래,오른쪽만 가능
    for i in range(2):
        nx=x+(dx[i]*move)
        ny=y+(dy[i]*move)
        # move는 현재 밟고 있는 칸에 쓰여 있는 수

        # 범위 안에 있고 아직 방문안했으면
        if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
            # 방문처리
            visit[nx][ny]=True

            # 도착까지 반복
            dfs(nx,ny) 

###################################################################

n=int(input()) 
board=[list(map(int,input().split())) for _ in range(n)]

# 일단 방문은 False
visit=[[False]*n for _ in range(n)]

# 시작은 방문
visit[0][0]=True

# 시작
dfs(0,0)

if goal:
    print('HaruHaru')
else:
    print('Hing')
