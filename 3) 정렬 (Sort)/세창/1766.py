import sys
import heapq
input=sys.stdin.readline


# n=문제의 수, m=정보의 개수
n,m=map(int,input().split())  # 4 2

# 인접 리스트
graph=[[] for _ in range(n)] 

# 진입 차수
indegree=[0]*(n+1) 

# 간선 정보
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)  
    indegree[b]+=1


heap=[]

# 진입 차수 0
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)


result=[]

# 위상정렬
# 큐 빌 때까지
while heap:
    now=heap.heapq.heappop(heap)
    result.append(now)


