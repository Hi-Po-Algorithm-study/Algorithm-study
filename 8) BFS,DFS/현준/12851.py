import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
q = []
heapq.heappush(q, (0, N))  # (초, 위치)
visitMinSec = [float('inf') for _ in range(100001)] # 방문체크 느낌

minSec = float('inf') # 최소 시간
way = 0 # 방법 수


while q:

    sec, s_now = heapq.heappop(q)

    if sec > minSec:
        break

    if s_now == K:
        minSec = min(minSec, sec)
        if minSec == sec:
            way += 1

    if 0 <= s_now-1 <= 100000:
        visitMinSec[s_now-1] = min(visitMinSec[s_now-1], sec+1)
        if visitMinSec[s_now-1] == sec+1:
            heapq.heappush(q, (sec + 1, s_now - 1))

    if 0 <= s_now+1 <= 100000:
        visitMinSec[s_now+1] = min(visitMinSec[s_now+1], sec+1)
        if visitMinSec[s_now+1] == sec+1:
            heapq.heappush(q, (sec + 1, s_now + 1))

    if 0 <= 2*s_now <= 100000:   
        visitMinSec[s_now*2] = min(visitMinSec[s_now*2], sec+1)
        if visitMinSec[s_now*2] == sec+1:
            heapq.heappush(q, (sec + 1, 2 * s_now))

print(minSec)
print(way)


# visit[N] = 1
# q.append(N)

# def find():

#     while q:
#         check = q.popleft()

#         if 0 <= check - 1 <= 100000 :  
#             visit[check - 1] += 1
#             q.append(check-1)

#         if 0 <= check + 1 <= 100000 :
#             visit[check + 1] += 1
#             q.append(check+1)

#         if 0 <= 2 * check <= 100000 :
#             visit[2 * check] += 1
#             q.append(2*check)

#         if visit[K] != 0:
#             break

# find()
# print(visit[K])