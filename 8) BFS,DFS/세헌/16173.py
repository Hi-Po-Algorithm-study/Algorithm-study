import sys
from collections import deque
N = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = deque()
q.append([0,0])

dx = [1,0]
dy = [0,1]
check = [[0]*N for _ in range(N)]
check[0][0] = 1
while q :
    x,y = q.popleft()
    jump = graph[x][y]
    if jump == -1 :
        check[x][y] = 100
        break
    for i in range(2) :
        nx = x
        ny = y
        for _ in range(jump) :
            nx += dx[i]
            ny += dy[i]
        if(0<=nx<N) and (0<=ny<N) and check[nx][ny]==0:
            check[nx][ny] = 1
            q.append([nx,ny])
if check[-1][-1] == 100 :
    print('HaruHaru')
else :
    print('Hing')