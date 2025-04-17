# import sys

# for _ in range(int(sys.stdin.readline())) :
#     N = int(sys.stdin.readline())
#     day = list(map(int,sys.stdin.readline().split()))
#     mx = max(day)
#     cnt = 0
#     price = 0
#     ans = 0
#     for i in range(N) : 
#         if day[i] != mx :
#             cnt += 1
#             price += day[i]
#         else :
#             ans += (mx*cnt) - price
#             if i+1<N :
#                 n = day[i+1:]
#                 mx = max(n)
#                 cnt = 0
#                 price = 0
#     print(ans)


# import sys
# import heapq
# for _ in range(int(sys.stdin.readline())) :
#     N = int(sys.stdin.readline())
#     day = list(map(int,sys.stdin.readline().split()))
#     q = []
#     for i in range(N) :
#         heapq.heappush(q,[-day[i],i])
#     mx, index = heapq.heappop(q)
#     mx = -mx
#     cnt = 0
#     price = 0
#     ans = 0
#     for i in range(N) : 
#         if i<index :
#             cnt += 1
#             price += day[i]
#         else :
#             ans += (mx*cnt) - price
#             if index<N-1 :
#                 for j in range(len(q)) :
#                     mx, index = heapq.heappop(q)
#                     if i<index :
#                         mx = -mx
#                         cnt = 0
#                         price = 0
#                         break
#             else :
#                 break           
                
#     print(ans)



import sys
for _ in range(int(sys.stdin.readline())) :
    N = int(sys.stdin.readline())
    day = list(map(int,sys.stdin.readline().split()))
    mx = day[N-1]
    price = 0
 
    for i in range(N-1,-1,-1) : 
        if day[i] < mx :
            price += mx - day[i]
        elif day[i]>mx :
            mx = day[i]
    print(price)