import sys
def dfs(x,y,n) :
    global cnt
    if maps[x][y] == 'T':
        return
    if x == 0 and y == Y-1 :
        if n == N :
            cnt = cnt + 1
        return
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=x and nx<X and 0<=ny and ny<Y and check[nx][ny]==0 and n+1 <= N:
            check[nx][ny] = 1
            dfs(nx,ny,n+1)
            check[nx][ny] = 0

X, Y, N = map(int,sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(X)]
check = [[0 for _ in range(Y)] for _ in range(X)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0

check[X-1][0] = 1

dfs(X-1,0,1)

print(cnt)
            