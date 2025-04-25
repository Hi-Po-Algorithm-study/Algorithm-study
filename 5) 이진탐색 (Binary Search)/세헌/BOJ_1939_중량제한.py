import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
weight = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M) :
    A, B, C = map(int, sys.stdin.readline().split())
    if weight[A][B] != 0:
        if weight[A][B]< C :
            weight[A][B] = C
            weight[B][A] = C
    else :
        weight[A][B]= C
        weight[B][A]= C
        

f1, f2 = map(int, sys.stdin.readline().split())
q = []

heapq.heappush(q,[-sys.maxsize,f1])
visited = [0] * (N+1)
visited[f1] = 1
mx = 0
while q :
    w, e = heapq.heappop(q)
    w = -w
    if e == f2 :
        if mx < w :
            mx = w
    for j in range(1,N+1) :
        if weight[e][j] != 0 :
            i = j
            l = weight[e][i]
        else :
            continue
        if visited[i] == 0 :
            visited[i] == 1
            if w<l :
                l = w
            if l>mx:
                q.append([-l,i])
print(mx)