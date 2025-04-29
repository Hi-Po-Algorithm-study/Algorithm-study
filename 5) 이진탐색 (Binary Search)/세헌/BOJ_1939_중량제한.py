import sys
from collections import deque
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
q = deque()

q.append([-sys.maxsize,f1])
visited = [0] * (N+1)
visited[f1] = 1
mx = 0
while q :
    w, e = q.popleft()
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





import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y,c = map(int, input().split())
    graph[x].append((y,c))
    graph[y].append((x,c))
start, end = map(int, input().split())
def bfs():
    que = deque()
    que.append(graph[start][0])
    que.append(graph[start][1])
    max_cost = 0
    while que:
        t, cost = que.popleft()
        if cost >= max_cost:
            que.append(graph[t][0])
            que.append(graph[t][1])
            max_cost = cost
        if t == end:
                break
    return max_cost
print(bfs())









from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = defaultdict(list)
weights = list()
for _ in range(m):
    a, b, c  = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))
    if c not in weights:
        weights.append(c)
s, e = map(int, input().split())
weights.sort()

left = 0
right = len(weights) - 1
answer = 0
while (left <= right):
    mid = (left + right) // 2
    avbw = weights[mid]
    queue = deque()
    queue.append(s)
    visited = [False] * (n+1)
    visited[s] = True
    flag = False
    while queue:
        v = queue.popleft()
        if v == e:
            answer = max(answer, avbw)
            flag = True
            break
        for c, nv in adj[v]:
            if not visited[nv] and c <= avbw:
                if nv != e: visited[nv] = True
                queue.append(nv)
    if not flag: right -= 1
    else: left += 1
print(answer)