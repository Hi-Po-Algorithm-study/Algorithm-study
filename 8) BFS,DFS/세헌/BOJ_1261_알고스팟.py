import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(M)]


q = []
heapq.heappush(q,[0,0,0])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph[0][0] = 100

while q:
    cnt, x, y = heapq.heappop(q)
    if x==M-1 and y==N-1 :
        print(cnt)
        break
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<M and 0<=ny<N and graph[nx][ny]!=100:
            if graph[nx][ny] == 1 :
                heapq.heappush(q,[cnt+1,nx,ny])
            else :
                heapq.heappush(q,[cnt,nx,ny])
            graph[nx][ny] = 100
