N,P=map(int,input().split())
A=list(map(int,input().split()) )
B=list(map(int,input().split()) )

visited=[False]*N
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    u,v=map(int,input().split())

    graph[u].append(v)
    graph[v].append(u)
print(graph)

S=[]
for i in S:
    S.append(P)
    visited[i]=True
    # for j in range(N):
    #     if visited[i]==False and graph[i][j]!=True:
        