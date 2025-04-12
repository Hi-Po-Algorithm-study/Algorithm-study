import sys
import heapq
input = sys.stdin.readline

M,N = map(int, input().split())
maze = []
visited = [[0 for _ in range(M)]for _ in range(N)]
for _ in range(N):
    maze.append(list(map(int, input().strip())))

queue = []
heapq.heappush(queue,(0, 0, 0)) #(부신개수, x좌표, y좌표)
direction = [(1,0),(-1,0),(0,1),(0,-1)]
answer = 0
visited[0][0] = 1

while queue:
    # print(queue)
    k = heapq.heappop(queue)
    wall, cur_x, cur_y = k
    
    if cur_x == M-1 and cur_y == N-1:
        answer = wall
        break
    else:
        for a,b in direction:
            if 0<=cur_x+a<M and 0<=cur_y+b<N:
                if visited[cur_y+b][cur_x+a] == 0:
                    if maze[cur_y+b][cur_x+a] == 0:
                        heapq.heappush(queue, (wall, cur_x+a, cur_y+b))
                        visited[cur_y+b][cur_x+a] = 1
                    else:
                        heapq.heappush(queue,(wall+1, cur_x+a, cur_y+b))
                        visited[cur_y+b][cur_x+a] = 1

print(answer)

# import sys
# import heapq
# input = sys.stdin.readline

# M,N = map(int, input().split())
# maze = []
# visited = [[0 for _ in range(M)]for _ in range(N)]
# for _ in range(N):
#     maze.append(list(map(int, input().strip())))
# direction = [(1,0),(-1,0),(0,1),(0,-1)]

# n_x = 0, n_y = 0
# while (n_x == M-1 and n_y == N-1):
#     for a,b in direction:
#         if 0<=n_x+a<N and 0<=n_y+b<M:
#             if maze[n_x+a][n_y+b] == 1:
#                 visited[n_x+a][n_y+b] =visited[n_x][n_y] + 1
#     for a,b in direction:
#         if 0<=n_x+a<N and 0<=n_y+b<M:

# #다익스트라가 뭐쓰는거더라