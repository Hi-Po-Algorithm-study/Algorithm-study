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
        x = x + dx[i]
        y = y + dy[i]
        if 0<=x and x<X and 0<=y and y<Y and check[x][y]==0 and n+1 <= N:
            check[x][y] == 1
            dfs(x,y,n+1)
            check[x][y] == 0

X, Y, N = map(int,sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(X)]
check = [[0 for _ in range(Y)] for _ in range(X)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0

check[X-1][0] = 1

dfs(X-1,0,1)

print(cnt)
            