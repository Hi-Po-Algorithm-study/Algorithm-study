import sys
input = sys.stdin.readline

n,p=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

graph=[[] for _ in range(n)]

# 인접리스트
for _ in range(n-1):
    u,v=map(int,input().split())
    # 무방향 
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

print(graph)

visit=[False]*n

cost=0

def dfs(p):
    global cost
    



print(cost)
