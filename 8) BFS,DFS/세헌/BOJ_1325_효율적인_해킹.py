import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
com = [[] for _ in range(N+1)]

for _ in range(M) :
    A, B = map(int, sys.stdin.readline().split())
    com[B].append(A)



def bfs(n) :
    check = [0] * (N+1)
    cnt = 1
    q = deque()
    q.append(n)
    check[n] = 1
    while q : 
        cur = q.popleft()
        if not com[cur] :
            continue 
        for i in com[cur] :
            if check[i] == 0 :
                q.append(i)
                cnt+=1
                check[i] = 1
    return cnt

com_n = [0] * (N+1)
for i in range(1,N+1) :
    if com[i] :
        com_n[i] = bfs(i)

mx = max(com_n)
ans = []
for i in range(1,N+1) :
    if com_n[i] == mx :
        ans.append(i)
print(*ans)


    