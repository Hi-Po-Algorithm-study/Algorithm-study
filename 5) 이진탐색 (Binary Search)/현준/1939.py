import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

max_weight = 0

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A][B] = max(graph[A][B], C)
    graph[B][A] = max(graph[B][A], C)


factory1 , factory2 = map(int, input().split()) 

print(graph)

queue =deque([])

for i in range(1, N+1):
    if graph[factory1][i] != 0:
        queue.append((i, graph[factory1][i])) #(도착지, 무게)

print(queue)
# while queue:
