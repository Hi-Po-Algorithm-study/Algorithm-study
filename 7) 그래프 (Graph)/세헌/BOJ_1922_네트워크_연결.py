import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
net  = [[]for _ in range(N+1)]
for i in range(M) :
    s, e, c = map(int, sys.stdin.readline().split())
    net[s].append([c,e])
    net[e].append([c,s])

q = []
check = [0 for _ in range(N+1)] 

heapq.heappush(q,[0,1])
cnt = 0
ans = 0

while(q and cnt<N) :
    c, n = heapq.heappop(q)
    if check[n] == 0 :
        ans += c
        cnt += 1
        check[n] = 1
        for a,e in net[n] :
            if check[e] == 0:
                heapq.heappush(q,[a,e])
    
print(ans)