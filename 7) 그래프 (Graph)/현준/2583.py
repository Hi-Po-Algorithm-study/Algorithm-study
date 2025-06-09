import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())

mapInfo = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    a,b,c,d = map(int, input().split())
    for i in range(a,c):
        for j in range(b,d):
            mapInfo[j][i] = 1
    
direction = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0 for _ in range(N)] for _ in range(M)]
cnt = 0
check = []
ansarea = []

for i in range(N):
    for j in range(M):
        if not visited[j][i]:
            # visited[j][i] = 1
            if mapInfo[j][i] == 1:
                continue
            else:
                area = 0
                check.append((i,j))
                
                while check:
                    x,y = check.pop()
                    if not visited[y][x]:
                        area += 1
                    visited[y][x] = 1
                    for dir in direction:
                        n_x, n_y = dir
                        if 0<=n_x + x<N and 0<=n_y+y<M:
                            if not visited[n_y+y][n_x+x]:
                                if mapInfo[n_y+y][n_x+x] == 0:
                                    check.append((n_x + x, n_y+y))
                ansarea.append(area)
                # for p in range(M):
                #     print(visited[p])
                # print()
                cnt += 1


print(cnt)
ansarea.sort()
print(*ansarea)