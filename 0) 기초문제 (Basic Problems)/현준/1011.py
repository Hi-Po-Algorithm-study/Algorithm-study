import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    # visited = [0 for _ in range(y)]
    q = []
    heapq.heappush(q, (1, 1, x+1)) #(횟수, 이동거리, 현재위치)
    # visited[x] = 1 # x+1에대한 방문처리
    visitedjump = {i : [] for i in range(y)}
    visitedjump[x].append(1) #x+1에 온 점프
    ans = 0

    while q:
        cnt, jump, now = heapq.heappop(q)
        
        if now == y:
            if jump == 1:
                ans = cnt
                break
        canjump1 = jump-1
        canjump2 = jump
        canjump3 = jump+1
        next1 = now+canjump1
        next2 = now+canjump2
        next3 = now+canjump3

        if canjump1 != 0:
            if next1 <= y:
                if canjump1 not in visitedjump[next1-1]:
                    # 여기에 점프로 도달한 적 없으면 추가
                    # visited[next1-1] = 1
                    visitedjump[next1-1].append(canjump1)
                    heapq.heappush(q, (cnt+1, canjump1, next1))

        if next2 <= y:
            if canjump2 not in visitedjump[next2-1]:
                # visited[next2-1] = 1
                visitedjump[next2-1].append(canjump2)
                heapq.heappush(q, (cnt+1, canjump2, next2))

        if next3 <= y:
            if canjump2 not in visitedjump[next3-1]:
                # visited[next3-1] = 1
                visitedjump[next3-1].append(canjump3)
                heapq.heappush(q, (cnt+1, canjump3, next3))
    
    print(ans)