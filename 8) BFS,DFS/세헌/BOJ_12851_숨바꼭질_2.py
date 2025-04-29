import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

if N == M:
    print(0)
    print(1)
elif N > M:
    print(N - M)
    print(1)
else:
    q = []
    visited = [sys.maxsize] * 100001 
    heapq.heappush(q, (0, N))
    visited[N] = 0

    mn = sys.maxsize
    cnt = 0

    while q:
        time, cur = heapq.heappop(q)

        if time > mn:
            break

        if cur == M:
            if mn == sys.maxsize:
                mn = time
            if time == mn:
                cnt += 1

        if 0 <= cur - 1 and visited[cur - 1] >= time + 1:
            visited[cur - 1] = time + 1
            heapq.heappush(q, (time + 1, cur - 1))

        if cur + 1 <= 100000 and visited[cur + 1] >= time + 1:
            visited[cur + 1] = time + 1
            heapq.heappush(q, (time + 1, cur + 1))

        if cur * 2 <= 100000 and visited[cur * 2] >= time + 1:
            visited[cur * 2] = time + 1
            heapq.heappush(q, (time + 1, cur * 2))

    print(mn)
    print(cnt)
