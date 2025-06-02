import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())

network = {i:[] for i in range(1, N+1)}
visited = [0 for _ in range(N+1)]
totalCost = 0

for i in range(M):
    a, b, c = map(int, input().split())
    network[a].append((c,b))
    network[b].append((c,a))

# 최소 스패닝 트리?
check = []

visited[1] = 1
for a in network[1]:
    heapq.heappush(check, a)


while(check):
    cost, dest = heapq.heappop(check)
    if visited[dest] == 0: 
        visited[dest] = 1
        totalCost += cost
        for a in network[dest]:
            heapq.heappush(check, a)
    else:
        continue

print(totalCost)