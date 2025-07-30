import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

rock = list(map(int, input().split()))
temp = deque([])
now = int(input())
visited = [0 for _ in range(n)]
visited[now - 1] = 1
can = 1

def bfs():

    while temp:
        global can
        a = temp.popleft()
        b = rock[a-1]
        
        if 0 < a + b < n+1:
            if visited[a+b-1] == 0:
                can += 1
                visited[a+b-1] = 1
                temp.append(a+b)
                
        if 0 < a - b < n+1:
            if visited[a-b-1] == 0:
                can += 1
                visited[a-b-1] = 1
                temp.append(a-b)

temp.append(now)
bfs()
print(can)

# import sys
# input = sys.stdin.readline

# N = int(input())
# cnt = 0
# history = []

# def hanoi(n, a, b, c):

#     global cnt, history
    
#     if n == 1:
# 		cnt += 1
# 		history.append((a, b))
# 	else:
# 		hanoi(n-1, a, c, b)
# 		cnt += 1
# 		history.append((a,c))
# 		hanoi(n-1, c, b, a)

# hanoi(N, 1, 3, 2)
# print(cnt)
# for i in range(cnt):
# 	k, g = history[i]
# 	print(k, g, end=" ")
