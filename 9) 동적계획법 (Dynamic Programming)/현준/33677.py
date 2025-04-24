import sys
# from collections import deque # 우선순위 큐가 필요하지 않나?
import heapq
input = sys.stdin.readline

N = int(input())
dp_day = [float('inf') for _ in range(N+2)]
dp_water = [float('inf') for _ in range(N+2)]

queue = []
heapq.heappush(queue, (1, 1, 1)) #(일수, 물양, 높이)
dp_day[1] = 1
dp_water[1] = 1

if N == 0:
    print('0 0')
    
else:

    while queue:
        day, water, height = heapq.heappop(queue)

        w1_height = height + 1
        w3_height = height * 3
        w5_height = height * height

        if w1_height <= N:
            if dp_day[w1_height] >= day+1 and dp_water[w1_height] >= water+1:
                dp_day[w1_height] = day+1
                dp_water[w1_height] = water+1
                heapq.heappush(queue, (day+1,water+1, w1_height))

        if w3_height <= N:
            if dp_day[w3_height] >= day+1 and dp_water[w3_height] >= water+3:
                dp_day[w3_height] = day+1
                dp_water[w3_height] = water+3
                heapq.heappush(queue, (day+1, water+3,w3_height))

        if w5_height <= N:
            if dp_day[w5_height] >= day+1 and dp_water[w5_height] >= water+5:
                dp_day[w5_height] = day+1
                dp_water[w5_height] = water+5
                heapq.heappush(queue, (day+1, water+5, w5_height))

    print(dp_day[N],dp_water[N])