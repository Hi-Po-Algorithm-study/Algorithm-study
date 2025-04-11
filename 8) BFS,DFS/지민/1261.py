#죄송 ㅋㅋ#############

import heapq
# inf=int(le9)

n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(m)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

graph=[[]*(m) for _ in range(n)]
# distance=[[inf] for _ in range(m)]
cnt=0

for i in range(n):
    x=dx[i]
    y=dy[i]

start=lst[0][0]
print(start)

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