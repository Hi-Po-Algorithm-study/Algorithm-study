#위상정렬

import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
indegree=[0 for _ in range(N+1)]

Q=[]
result=[]

for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    indegree[B]+=1
    
for i in range(1,N+1):
    if indegree[i]==0:
        heapq.heappush(Q,i)    

while Q:
    n=heapq.heappop(Q)    
    print(n,end=' ')
    for i in graph[n]:
        indegree[i]-=1
        if indegree[i]==0:
            heapq.heappush(Q,i)
    
    
    #graph[A].append(B)이렇게 그래프 순서 정하려했는데 어케하는지 모르겟음 A와 B는 값이라서 이걸 넣으면 안되잔슴
    #graph[A] 진입차수 0으로 하고 +=1


# Q=deque([])

# #진입차수가 0이면 que에 들어감 아니면 1부터 -1해서 들여보냄-반복
# for i in range(N):
#     if indegree[i]==0:
#             Q.append(i)
#     else: 
#         #indegree에 진입차수에 -1하고 0인거 append
#         indegree[i]-1
#         if indegree[i]==0:
#             Q.append(i)

        
# #가능한 최소 문제를 뽑아야하니까
