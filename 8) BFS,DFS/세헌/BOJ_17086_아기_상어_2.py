import sys
N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

dx = [0, 0, 1, -1, 1, -1 ,1, -1]
dy = [1,-1, 0, 0, 1, -1, -1, 1]

cnt = 1
while(True) :
    check = True
    for i in range(N) :
        for j in range(M) :
            if maps[i][j] == cnt :
                for r in range(8) :
                    x = i + dx[r]
                    y = j + dy[r]
                    if 0<=x and x<N and 0<=y and y<M :
                        if maps[x][y] == 0 :
                            maps[x][y] = maps[i][j] + 1
            elif maps[i][j] == 0 :
                check = False
    if check : 
        break 
    cnt += 1

print(max(map(max,maps))-1)
