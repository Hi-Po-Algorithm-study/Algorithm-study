import sys
import heapq
N, M = map(int,sys.stdin.readline().split())
indgree = [0] * (N+1)
Quiz = [[]for _ in range(N+1)]
for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    Quiz[a].append(b)
    indgree[b] += 1

q= []
for i in range(1,N+1) :
    if indgree[i]==0 :
        heapq.heappush(q,i)
ans = []
while q:
    n = heapq.heappop(q)
    print(n, end=' ')
    for i in Quiz[n] :
        indgree[i]-=1
        if indgree[i] == 0 :
            heapq.heappush(q,i)

