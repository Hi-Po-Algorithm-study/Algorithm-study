import heapq
import sys
input=sys.stdin.readline
INF = int(1e9) 

n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
distance=[[INF] for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dijkstra():
    q=[]
    heapq.heappush(q,(0,0,0))
    distance[0][0]=0
    while q:
        cost,r,c=heapq.heappop(q)
        
        if cost > distance[r][c]:
            continue
        for i in range(4):
            nx=r+dx[i]
            ny=c+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny >=m:
                continue
            if cost + lst[nx][ny] < distance[nx][ny]:
                distance[nx][ny]=cost+lst[nx][ny]
                heapq.heappush(q,(distance[nx][ny],nx,ny))
                
dijkstra()
print(distance[n-1][m-1])







# graph=[[]*(m) for _ in range(n)]

# cnt=0

# for i in range(n):
#     x=dx[i]
#     y=dy[i]

# start=lst[0][0]
# print(start)

# for i in range(n):
#     for ii in range(m):
#         if lst[i][ii]==0:
#             graph.append((x,y))
#         else:
#             graph.append((x,y))
#             cnt+=1
# print(graph)


# def dijkstra(start):
#     q=[]
#     heapq.push(q,start)
    
    
# start=graph[1][1]


#시작 (1,1)
#0이면 벽 안부셔도됨, 1이면 cnt+=1
#다익스트라로 최소경로 구하고 벽 세기