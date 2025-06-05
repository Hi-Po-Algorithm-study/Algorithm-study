import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())

mapInfo = []
dir = [(1,0), (0,1), (-1,0), (0,-1)]
ans = 0

for _ in range(R):
    mapInfo.append(list(map(str, input().strip())))

visited = [[0 for _ in range(C)] for _ in range(R)]

def dfs(x, y, len):
    global ans
  
    if x == 0 and y == C-1 and len == K:
        ans += 1

    for d in dir:
        n_x, n_y = d
        if 0<=x+n_x<R and 0<= y+n_y<C:
            if mapInfo[x+n_x][y+n_y] != 'T':
                if not visited[x+n_x][y+n_y]:
                    visited[x+n_x][y+n_y] = 1
                    dfs(x+n_x, y+n_y, len+1)
                    visited[x+n_x][y+n_y] = 0

visited[R-1][0] = 1
dfs(R-1, 0, 1)

print(ans)
