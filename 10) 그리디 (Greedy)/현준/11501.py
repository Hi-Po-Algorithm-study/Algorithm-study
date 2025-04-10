import sys
input = sys.stdin.readline
import heapq

T = int(input())
for _ in range(T):
    N = int(input())
    cost = list(map(int, input().split()))
    # daychange = []
    # for i in range(N-1):
    #     daychange.append(cost[i+1]- cost[i])
    # # print(daychange)

    # stack = 1
    # profit = 0
    # for i in range(N-1):
    #     if daychange[i] < 0:
    #         stack = 1
    #         continue
    #     else:
    #         profit += (daychange[i] * stack)
    #         stack += 1
    # print(profit) 

    # 시간 초과
    # profit = 0
    # for i in range(len(cost)):
    #     if i != (len(cost) -1):    
    #         current = cost[i]
    #         sellpoint = max(cost[i+1:])
    #         if sellpoint >= current:
    #             profit += (sellpoint - current)
    #         else:
    #             continue
    # print(profit)

    # # queue 실패
    # queue = []
    # heapq.heappush(queue, cost[0])
    # num = 1
    # profit = 0

    # for _ in range(N-1):
    #     if len(queue) > 0:
    #         check = queue[-1]
    #         while queue:
    #             if cost[num] <= check:
    #                 heapq.heappush(queue,cost[num])
    #                 break
    #             else:
    #                 profit += (cost[num] - check)
    #                 heapq.heappop(queue)
    #     else:
    #         heapq.heappush(queue,cost[num])
        
    #     num +=1
    
    # print(profit)
    check = cost[-1] 
    profit = 0
    for i in range(N-2, -1, -1):
        if cost[i] >= check:
            check = cost[i]
        else:
            profit += (check - cost[i])

    print(profit)
            