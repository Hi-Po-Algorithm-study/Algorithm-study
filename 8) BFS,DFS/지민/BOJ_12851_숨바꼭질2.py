import heapq
N,K=map(int,input().split())
S=[]
visit=[[False]*(K)]
cnt=0
Time=[]

while N!=K:
    

    if visit[N]==False and 2*N<K:  
        N=2*N
        visit[N]==True
    elif visit[N]==False and N>K:
        N=N-1
        visit[N]==True
    else:
        N=N+1
        visit[N]==True

        
    cnt+=1
heapq.heappush(Time,cnt)
print(heapq.heappop())


def bfs():
    S=[]
    heapq.heappush(S,N)
    while S:
        a=heapq.heappop()
        if visit[a]==False and graph[a]==True:
            visit[a]==True

        heapq.heappush(S,N)    

            