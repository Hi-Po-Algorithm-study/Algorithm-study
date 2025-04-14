import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().split())))

direction = [(1, 0), (0, 1)]

queue = deque([(0, 0)])

while queue:

    cur_x, cur_y = queue.popleft()
    jump = graph[cur_x][cur_y]

    for dir_x, dir_y in direction:
        next_x = cur_x + jump * dir_x
        next_y = cur_y + jump * dir_y

        if 0 <= next_x < N and 0 <= next_y < N:
            if not visited[next_x][next_y]:
                visited[next_x][next_y] = 1
                queue.append((next_x, next_y))

if visited[N - 1][N - 1] == 1:
    print("HaruHaru")
else:
    print("Hing")
