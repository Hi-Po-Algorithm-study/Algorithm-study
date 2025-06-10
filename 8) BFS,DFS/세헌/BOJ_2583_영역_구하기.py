import sys
sys.setrecursionlimit(10000)
N, M, K = map(int, sys.stdin.readline().split())
maps = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K) :
    xl, yl, xr, yr = map(int, sys.stdin.readline().split())
    for i in range(xl,xr) :
        for j in range(yl,yr) :
            maps[i][j] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y) : 
    area = 1
    maps[x][y] = 2
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N and maps[nx][ny] == 0 :
            
            area = area + dfs(nx,ny)
    return area


cnt = 0
ans = []
for i in range(M) :
    for j in range(N) :
        if maps[i][j] == 0 :
            ans.append(dfs(i,j))
            cnt += 1
ans.sort()
print(cnt)
print(*ans)





