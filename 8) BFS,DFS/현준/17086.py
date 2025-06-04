import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

babyShark = []
direction = [(-1, 0), (1,0), (0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
check = deque([])
maxLen = 0
totalMax = 0


for i in range(N):
    temp = list(map(int, input().split()))
    babyShark.append(temp)


def bfs(visited, check):
    maxLen = 0
    flag = 0
    while check:
        x, y, safe_len = check.popleft()
        maxLen = max(maxLen, safe_len)

        for dir in direction:
            n_x, n_y = dir
            if 0<=x+n_x<N and 0<=y+n_y<M:
                if not visited[x+n_x][y+n_y]:
                    if babyShark[x+n_x][y+n_y] == 0:
                        visited[x+n_x][y+n_y] = 1
                        check.append((x+n_x, y+n_y, safe_len+1))
                    else:
                        maxLen = safe_len
                        flag = 1
                        break
        if flag == 1:
            break
    
    return maxLen


for i in range(N):
    for j in range(M):
        if babyShark[i][j] == 1: # 체크 할 필요 없음
            continue


        else: # 체크!
            visited = [[0 for _ in range(M)] for _ in range(N)]
            
            check.append((i,j,0))
            visited[i][j] = 1
            kk = bfs(visited, check)
            print(kk)
            totalMax = max(totalMax, kk)
            # for dir in direction:
            #     n_x, n_y = dir
            #     if 0<=i+n_x<N and 0<=j+n_y<N:
            #         if babyShark[i+n_x][j+n_y] == 0:
            #             check.append((i+n_x, j+n_y, 1))

            # while check:
            #     check.popleft


print(totalMax)



# dfs 는 재귀로 푸는거고
# bfs 는 큐로 다 집어 넣고 큐 끝날 때 까지 while 돌린다

